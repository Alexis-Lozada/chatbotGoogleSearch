# 🤖 Chatbot con LangChain, OpenAI y Búsqueda en Google

Este proyecto es un chatbot conversacional inteligente desarrollado con **Flask**, **Socket.IO**, **LangChain** y **OpenAI**, con capacidad para realizar búsquedas en **Google** en tiempo real, mantener conversaciones multi-turno con memoria por sesión y responder con información confiable incluyendo enlaces.

---

## ✨ Funcionalidades

- 🧠 **Agente Conversacional** basado en LangChain con memoria por sesión.
- 🔍 **Herramienta de búsqueda en Google** usando Google Custom Search API.
- 🧾 **Respuestas claras y estructuradas** con fuentes citadas.
- 🔄 **Interacciones multi-turno** tipo ChatGPT con historial de conversación.
- 🔌 Soporte para pruebas en **Postman (Socket.IO)** o integración web.

---

## ⚙️ Requisitos

- Python 3.10+
- Cuenta en [OpenAI](https://platform.openai.com/)
- Cuenta en [Google Cloud Console](https://console.cloud.google.com/)

---

## 📦 Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/tu_usuario/chatbot-google-langchain.git
cd chatbot-google-langchain
Instala las dependencias:

bash
Copiar
Editar
pip install -r requirements.txt
Crea un archivo .env en la raíz del proyecto y agrega tus claves:

ini
Copiar
Editar
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxx
GOOGLE_API_KEY=AIzaSyXXXXXXXXXXXX
GOOGLE_CX=xxxxxxxxxxxxxxxxx
🔐 Tu GOOGLE_CX es el ID del motor de búsqueda personalizado. Puedes crearlo en Google Custom Search.

Ejecuta la aplicación:

bash
Copiar
Editar
python app.py
💬 Probar con Postman (Socket.IO)
Conéctate a http://localhost:5000 usando Socket.IO.

Escucha el evento: response.

Envía los siguientes eventos:

Evento: join
json
Copiar
Editar
{
  "session_id": "usuario123"
}
Evento: message
json
Copiar
Editar
{
  "session_id": "usuario123",
  "message": "¿Es cierto que enero de 2025 fue el mes más caluroso?"
}
📁 Estructura del Proyecto
bash
Copiar
Editar
├── app.py                # Servidor Flask con LangChain y WebSocket
├── GoogleSearch.py       # Herramienta de búsqueda con Google API
├── .env                  # Claves de entorno (no subir a GitHub)
├── requirements.txt      # Dependencias del proyecto
└── README.md             # Este archivo :)
📚 Tecnologías Utilizadas
LangChain

OpenAI API

Google Custom Search

Flask + Flask-SocketIO

Python

🚀 Futuras mejoras
Interfaz web (Streamlit o React)

Persistencia de sesiones en base de datos

Soporte para archivos (PDF, Docs, etc.)

Comandos personalizados (resumir, traducir, etc.)

📄 Licencia
Este proyecto está bajo la licencia MIT.
¡Úsalo, modifícalo y compártelo libremente!

🙌 Agradecimientos
Gracias a LangChain y a la comunidad OpenAI por el poder de las herramientas abiertas.
Desarrollado con ❤️ por [TuNombre].