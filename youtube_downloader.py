import yt_dlp

url = input("Enter YouTube URL: ").strip()

options = {
    "format": "best[ext=mp4]/best",
    "merge_output_format": "mp4",
    "outtmpl": "%(title)s.%(ext)s",
}

try:
    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([url])

    print("\nDownload completed!")

except Exception as e:
    print("\nDownload failed:")
    print(e)