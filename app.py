from flask import Flask, request
import requests
import os

app = Flask(__name__)

# Dados fixos do seu bot e canal
BOT_TOKEN = "7468603286:AAF5ALqMnsL-NIcH5lJwLTyaExTBq7L01IM"
CHANNEL_ID = "@salasniperob"

@app.route("/", methods=["GET"])
def home():
    return "Bot Webhook Online"

@app.route("/", methods=["POST"])
def webhook():
    data = request.json
    print("Recebido:", data)

    ativo = data.get("ativo", "Ativo não informado")
    direcao = data.get("direcao", "CALL/PUT")
    horario = data.get("horario", "00:00")
    timeframe = data.get("timeframe", "M1")

    mensagem = f"""
✅ NOVO SINAL

🧠 Ativo: {ativo}
⏰ Horário: {horario}
📈 Direção: {direcao.upper()}
🕐 Timeframe: {timeframe}
    """.strip()

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHANNEL_ID,
        "text": mensagem,
        "parse_mode": "Markdown"
    }

    response = requests.post(url, json=payload)
    print("Resposta Telegram:", response.text)

    return {"status": "mensagem enviada"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
