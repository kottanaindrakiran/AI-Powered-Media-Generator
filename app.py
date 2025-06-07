from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import ImageClip, AudioFileClip
import os
import uuid

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def home():
    return "✅ AI Media Generator API is running"

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    prompt = data.get("text", "").strip()

    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400

    # Unique ID for filenames
    uid = str(uuid.uuid4())

    # === 1. Generate image ===
    img_path = f"static/{uid}_image.png"
    img = Image.new("RGB", (3840, 2160), color=(30, 30, 30))
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    draw.text((100, 100), prompt, fill="white", font=font)
    img.save(img_path)

    # === 2. Generate silent audio (you can use ElevenLabs API here instead) ===
    audio_path = f"static/{uid}_audio.wav"
    os.system(f"ffmpeg -f lavfi -i anullsrc=channel_layout=stereo:sample_rate=44100 -t 5 {audio_path}")

    # === 3. Combine image + audio into video ===
    video_path = f"static/{uid}_final_video.mp4"
    clip = ImageClip(img_path, duration=5)
    clip = clip.set_audio(AudioFileClip(audio_path))
    clip.write_videofile(video_path, fps=24)

    return jsonify({
        "image_url": f"/{img_path}",
        "audio_url": f"/{audio_path}",
        "video_url": f"/{video_path}"
    })

if __name__ == "__main__":
    os.makedirs("static", exist_ok=True)
    app.run(host="0.0.0.0", port=7860)
