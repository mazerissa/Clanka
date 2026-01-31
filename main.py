import os
from groq import Groq
from dotenv import load_dotenv

# Load your GROQ_API_KEY from .env
load_dotenv()

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

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

def chat():
    history = [{"role": "system", "content": CLANKA_PERSONALITY}]
    
    print("Clanka is online (Type 'exit' to leave)")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "clear"]:
            break
        history.append({"role": "user", "content": user_input})
        try:
            completion = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=history,
            )
            clanka_reply = completion.choices[0].message.content
            print(f"Clanka: {clanka_reply}")
            history.append({"role": "assistant", "content": clanka_reply})
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    chat()