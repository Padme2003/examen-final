from flask import Flask, render_template_string, request, jsonify
import random

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Proyecto Pilataxi con IA</title>
    <style>
        body { font-family: Arial; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 20px; }
        .container { max-width: 800px; margin: 0 auto; background: white; border-radius: 20px; padding: 30px; }
        .chat-box { border: 2px solid #ddd; padding: 15px; height: 300px; overflow-y: auto; margin: 20px 0; background: #f9f9f9; }
        .message { margin: 10px 0; padding: 10px; border-radius: 8px; }
        .user { background: #667eea; color: white; text-align: right; }
        .bot { background: #e0e0e0; }
        input { width: 80%; padding: 10px; }
        button { padding: 10px 20px; background: #667eea; color: white; border: none; cursor: pointer; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 EXAMEN 100% PRÁCTICO</h1>
        <p><strong>Estudiante:</strong> Pamela Pilataxi | <strong>Versión:</strong> 1.0.5</p>
        <h2>💬 Chatbot IA</h2>
        <div class="chat-box" id="chat"></div>
        <input type="text" id="msg" placeholder="Escribe un mensaje...">
        <button onclick="send()">Enviar</button>
    </div>
    <script>
        function send() {
            const msg = document.getElementById('msg').value;
            if (!msg) return;
            document.getElementById('chat').innerHTML += '<div class="message user">' + msg + '</div>';
            document.getElementById('msg').value = '';
            fetch('/chat', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({msg: msg})
            }).then(r => r.json()).then(d => {
                document.getElementById('chat').innerHTML += '<div class="message bot">' + d.response + '</div>';
            });
        }
    </script>
</body>
</html>
"""

class SimpleIA:
    def __init__(self):
        self.responses = {
            "hola": ["¡Hola! ¿Cómo estás?", "¡Hola! Soy un chatbot con IA"],
            "cicd": ["CI/CD automatiza despliegues", "La integración continua es clave"],
            "docker": ["Docker facilita contenedores", "Docker Swarm orquesta servicios"],
        }
    
    def responder(self, msg):
        msg = msg.lower()
        if "hola" in msg or "hi" in msg:
            return random.choice(self.responses["hola"])
        elif "cicd" in msg or "ci/cd" in msg:
            return random.choice(self.responses["cicd"])
        elif "docker" in msg:
            return random.choice(self.responses["docker"])
        else:
            return "Interesante. Cuéntame más sobre eso."

ia = SimpleIA()

def create_app():
    app = Flask(__name__)

    @app.get("/")
    def home():
        return render_template_string(HTML)
    
    @app.post("/chat")
    def chat():
        data = request.get_json()
        msg = data.get('msg', '')
        response = ia.responder(msg)
        return jsonify({"response": response})

    return app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)