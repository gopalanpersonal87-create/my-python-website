from flask import Flask, request, jsonify
import yt_dlp
import os


app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello! My Python Website is Working!</h1>"
    

@app.route("/test")
def test():
    return {
        "yt_dlp_version": yt_dlp.version.__version__
    }


@app.route("/youtube-downloader", methods=["POST"])
def youtube_downloader():

     url = request.form.get("url")

    if not url:
        return jsonify({
            "success": False,
            "message": "URL is required"
        }), 400

    try:
        options = {
            "quiet": False,
            "skip_download": True,
            "noplaylist": True,
        }

        with yt_dlp.YoutubeDL(options) as ydl:
            info = ydl.extract_info(url, download=False)

        return jsonify({
            "success": True,
            "id": info.get("id"),
            "title": info.get("title"),
            "duration": info.get("duration"),
            "webpage_url": info.get("webpage_url")
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "error_type": type(e).__name__,
            "message": str(e)
        }), 500
        
        
if __name__ == "__main__":
    app.run()