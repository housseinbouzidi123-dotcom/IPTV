import os, requests
from flask import Flask, Response

app = Flask(__name__)

# رابط قناتك الجديدة والمحدثة مدمج هنا بشكل سليم مئة بالمئة
URL = "http://217.60.15.181:8080/live///b0:99:d7:15:88:50/3090914536649669/318198.ts?token=yXzbaHc.fHya.X.cUydz.ydzzbUUfHX.X.y.FR.ts.7c14c38c3090576757ad0d2d0f7f5019dd0600a1e9c209b64298017137953fe1.5089.VmlyZ2luIE1lZGlh.MTg1LjE5MS4xMjYuMTI3"

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def s(path):
    headers = {"User-Agent": "VLC/3.0.18"}
    
    def generate():
        with requests.get(URL, headers=headers, stream=True) as r:
            for chunk in r.iter_content(chunk_size=4096):
                if chunk:
                    yield chunk

    return Response(generate(), content_type="video/mp3")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
