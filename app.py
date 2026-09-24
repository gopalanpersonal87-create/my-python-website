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
            "message": "YouTube URL is required"
        }), 400

    options = {
        "format": "bestvideo+bestaudio/best",
        "merge_output_format": "mp4",
        "outtmpl": "%(title)s.%(ext)s"
    }

    try:
        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([url])

        return jsonify({
            "success": True,
            "message": "Download completed"
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "message": str(e)
        }), 500
        
        
if __name__ == "__main__":
    app.run()