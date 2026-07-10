import os, requests
from flask import Flask, Response, request

app = Flask(__name__)

# تعديل المسار ليعمل كالمسار الرئيسي للموقع وتجنب خطأ الـ Not Found
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def s(path):
    link = request.args.get("url")
    if not link:
        return "سيرفر البث المباشر يعمل بنجاح! ضَع رابط القناة بعد علامة الـ =", 200
        
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
