from flask import Flask, request, jsonify
from flask_cors import CORS
import uuid
import os
from PIL import Image
import wave

app = Flask(__name__)
CORS(app)

SAVE_DIR = "static"
os.makedirs(SAVE_DIR, exist_ok=True)

def save_image(prompt):
    # Generate placeholder image with solid color
    img = Image.new("RGB", (512, 512), color=(128, 128, 255))
    filename = f"{uuid.uuid4()}.png"
    filepath = os.path.join(SAVE_DIR, filename)
    img.save(filepath)
    return f"/static/{filename}"

def save_audio(prompt):
    # Create 1-second silent WAV audio file placeholder
    filename = f"{uuid.uuid4()}.wav"
    filepath = os.path.join(SAVE_DIR, filename)
    with wave.open(filepath, 'w') as f:
        f.setnchannels(1)        # mono
        f.setsampwidth(2)        # 2 bytes per sample
        f.setframerate(44100)    # 44.1kHz sample rate
        frames = b'\x00\x00' * 44100  # 1 second of silence
        f.writeframes(frames)
    return f"/static/{filename}"

def save_video(prompt):
    # Placeholder video URL (replace later with real AI-generated video)
    return "https://sample-videos.com/video123/mp4/720/big_buck_bunny_720p_1mb.mp4"

@app.route("/generate", methods=["POST"])
def generate_media():
    data = request.get_json()
    prompt = data.get("text", None)

    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400

    host_url = request.host_url.strip("/")
    image_url = host_url + save_image(prompt)
    audio_url = host_url + save_audio(prompt)
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
