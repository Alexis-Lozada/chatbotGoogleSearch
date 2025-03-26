import os
from flask import Flask
from flask_socketio import SocketIO, emit, join_room, leave_room
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.agents import Tool, AgentExecutor, ConversationalAgent
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from GoogleSearch import google_search  # tu función personalizada

# Cargar variables de entorno
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Inicializar Flask + Socket.IO
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# Diccionario para guardar memoria por sesión
sessions = {}

# Instanciar el modelo LLM
llm = ChatOpenAI(model_name="gpt-4", openai_api_key=OPENAI_API_KEY)

# Herramienta de búsqueda en Google
def search_google(query: str) -> str:
    results = google_search(query)
    if not results:
        return "No encontré resultados relevantes."

    links = "\n".join([f"- [{title}]({link})" for title, link in results])
    return (
        f"Según los resultados más relevantes:\n\n{links}\n\n"
        f"Usa esta información para confirmar o refutar la consulta del usuario."
    )

tools = [
    Tool(
        name="search_google",
        func=search_google,
        description="Usa esta herramienta para buscar información actual en Google."
    )
]

@app.route('/')
def home():
    return "🤖 Chatbot con LangChain, OpenAI y Google Search está activo."

@socketio.on("connect")
def handle_connect():
    emit("response", {"message": "✅ Conexión establecida"})

@socketio.on("join")
def handle_join(data):
    session_id = data.get("session_id")
    join_room(session_id)

    if session_id not in sessions:
        sessions[session_id] = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True
        )

    emit("response", {"message": f"🙌 Sesión {session_id} iniciada"}, room=session_id)

@socketio.on("message")
def handle_message(data):
    session_id = data.get("session_id")
    user_input = data.get("message")

    if session_id not in sessions:
        emit("response", {"message": "❌ Error: Sesión no encontrada"}, room=session_id)
        return

    memory = sessions[session_id]

    # 🧠 Mensaje de sistema personalizado
    system_message = (
        "Eres un asistente conversacional útil, claro y confiable. "
        "Puedes usar herramientas como la búsqueda en Google para encontrar información actual y precisa. "
        "Siempre responde con enlaces relevantes cuando sea posible, y si una pregunta es ambigua, pide más contexto. "
        "Continúa la conversación con base en el historial cuando sea necesario."
    )

    # Crear el prompt con historial + scratchpad
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_message),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad")
    ])

    # Crear el agente correctamente
    agent = ConversationalAgent.from_llm_and_tools(
        llm=llm,
        tools=tools,
        prompt=prompt
    )

    executor = AgentExecutor.from_agent_and_tools(
        agent=agent,
        tools=tools,
        memory=memory,
        verbose=True
    )

    # Ejecutar y responder
    response = executor.run(user_input)
    emit("response", {"message": response}, room=session_id)

@socketio.on("leave")
def handle_leave(data):
    session_id = data.get("session_id")
    leave_room(session_id)
    emit("response", {"message": f"👋 Sesión {session_id} cerrada"}, room=session_id)

if __name__ == "__main__":
    socketio.run(app, debug=True)
