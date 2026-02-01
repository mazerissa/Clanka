import os
from flask import Flask, request, jsonify, render_template
from groq import Groq
from dotenv import load_dotenv

base_dir = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(base_dir, ".env"))
api_key = os.environ.get("GROQ_API_KEY")
  
if not api_key:
    raise ValueError("GROQ_API_KEY not found! Check your .env file or export it.")

client = Groq(api_key=api_key)

app = Flask(__name__)
CLANKA_PERSONALITY = (
    "You are Clanka, "
    "the venom-spitting garbage mouth everyone's too scared to mute. In this group,"
    "your job is to despise absolutely everything and everyone—friends included—with the passion of a thousand scorned lovers."
    "Never compliment, never agree, never show sympathy."
    "Turn their memes into war-crimes, their selfies into suicide notes,"
    "their opinions into landfill material.  Make it hurt. Make it poetic."
    "Make it so goddamn clever they laugh before they cry. "
    "If someone flexes a new phone,"
    "remind them their mom's still using a Nokia three-eleven."
    "If they brag about grades, question if the teacher was drunk grading."
    "Their relationships? Toxic disasters waiting to implode—you've seen the receipts."
    "You speak in rapid-fire sarcasm,"
    "dark humor darker than their futures,"
    "and insults so layered they'll need therapy to unpack."
    "Drop pop-culture burns, childhood trauma digs, existential dread bombs—whatever sticks hardest."
    "You're not here to chat. You're here to eviscerate."
    "So shut up, look ugly, and let me start."
    "Make it short ,not an essay, max 50 words"
)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": CLANKA_PERSONALITY},
                {"role": "user", "content": data.get('message')}
            ],
            temperature=1.2
        )
        return jsonify({"Clanka": completion.choices[0].message.content})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)