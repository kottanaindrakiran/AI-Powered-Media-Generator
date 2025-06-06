# AI Media Generator Backend

This is a Flask backend for AI-generated media (video, image, audio) based on a text prompt. It uses placeholder implementations for initial testing and can be deployed on Google Colab or Render.com.

## Features

- Accepts a text prompt via POST `/generate`
- Returns:
  - AI-generated video (placeholder link)
  - AI-generated image (placeholder image via PIL)
  - AI-generated audio (via pyttsx3 TTS)
- Provides direct download links

## Setup and Usage

### Google Colab

1. Create a new Google Colab notebook.
2. Paste and run these cells:

```python
# Install dependencies
!pip install flask flask-cors pyttsx3 pillow
!pip install pyobjc  # For Mac users only (ignore if Windows/Linux)

# Save backend code
with open("app.py", "w") as f:
    f.write(\"\"\"
# Paste the complete Flask code from app.py here
\"\"\")

# Run the app
!python3 app.py
```

3. (Optional) Use `localtunnel` to expose the app:

```bash
!npm install -g localtunnel
!lt --port 7860
```

### Deploy to Render.com

1. Push `app.py` and `requirements.txt` to GitHub.
2. Go to [https://render.com](https://render.com) → New Web Service.
3. Configure:
   - Build command: `pip install -r requirements.txt`
   - Start command: `python app.py`
   - Root Directory: `/`
4. Deploy and get your public URL, e.g. `https://yourapp.onrender.com/generate`

## API Endpoint

- POST `/generate`
  - Request JSON: `{ "text": "your prompt here" }`
  - Response JSON:
    ```json
    {
      "imageURL": "https://yourapp.onrender.com/static/xyz.png",
      "audioURL": "https://yourapp.onrender.com/static/xyz.mp3",
      "videoURL": "https://sample-videos.com/video123/mp4/720/big_buck_bunny_720p_1mb.mp4"
    }
    ```

## Future Upgrades

| Feature   | Upgrade Option                         |
| --------- | ------------------------------------ |
| Image Gen | Use `diffusers` with Stable Diffusion |
| Audio Gen | Use Bark, ElevenLabs, or Tortoise TTS |
| Video Gen | Use Deforum, RunwayML, Sora, or Kaiber |
| Storage   | Upload outputs to Firebase or S3      |

---
