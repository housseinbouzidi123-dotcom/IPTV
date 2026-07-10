import os, requests
from flask import Flask, Response, request

app = Flask(__name__)

@app.route("/stream")
def s():
    # هذا السطر يستقبل أي رابط طويل مشفر تضعه في تطبيقك ويمرره للمشاهدين
    link = request.args.get("url")
    headers = {"User-Agent": "VLC/3.0.18"}
    
    def generate():
        with requests.get(link, headers=headers, stream=True) as r:
            for chunk in r.iter_content(chunk_size=4096):
                if chunk:
                    yield chunk

    return Response(generate(), content_type="video/mp3")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
