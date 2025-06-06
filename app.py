from flask import Flask, request, jsonify
from flask_cors import CORS
import uuid
import os
from datetime import datetime
from PIL import Image
import pyttsx3

app = Flask(__name__)
CORS(app)

SAVE_DIR = "static"
os.makedirs(SAVE_DIR, exist_ok=True)

def save_image(prompt):
    # Generate placeholder image using PIL
    img = Image.new("RGB", (512, 512), color=(128, 128, 255))
    filename = f"{uuid.uuid4()}.png"
    filepath = os.path.join(SAVE_DIR, filename)
    img.save(filepath)
    return f"/static/{filename}"

def save_audio(prompt):
    engine = pyttsx3.init()
    filename = f"{uuid.uuid4()}.mp3"
    filepath = os.path.join(SAVE_DIR, filename)
    engine.save_to_file(prompt, filepath)
    engine.runAndWait()
    return f"/static/{filename}"

def save_video(prompt):
    # Placeholder video link from sample video
    # You can replace this with Deforum API or Hugging Face inference
    return "https://sample-videos.com/video123/mp4/720/big_buck_bunny_720p_1mb.mp4"

@app.route("/generate", methods=["POST"])
def generate_media():
    data = request.get_json()
    prompt = data.get("text", "")

    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400

    image_url = request.host_url.strip("/") + save_image(prompt)
    audio_url = request.host_url.strip("/") + save_audio(prompt)
    video_url = save_video(prompt)

    return jsonify({
        "imageURL": image_url,
        "audioURL": audio_url,
        "videoURL": video_url
    })

@app.route("/")
def home():
    return "✅ AI Generator Backend is Running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)
