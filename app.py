import os, requests
from flask import Flask, Response, request

app = Flask(__name__)

# تعديل المسار ليعمل كالمسار الرئيسي للموقع وتجنب خطأ الـ Not Found
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def s(path):
    link = request.args.get("http://217.60.253.206:8080/WFJobG5hOCtUSHh5VVpDQWJmL2tsemtuQ0VtMEFLbjh1aUZXUzNaUWRsUEs0MXJBS2VweW13L2ljbHVUWE11cDB4em1ZQU8wOWRTTlFLNjRPa2pSaVIyTFRPSStQRTZIWlBENEREclBXbmpPazNjRkZBNzJJRkNaVko3aUZmRVY3UjRqYUpXUWlaT1B5RVoyakFrL3Nra0lQaytRdDVmdktpcFdydzNyaTBTVkZIM3U1dVNCSWJBd01ZenFZYzZRQ1FjUGUxVmd4Wjg1alFoY3hpVnRjQjNVTCtEOEU5YVlHVUs3T0RLRkVtZ1I3Qk9aN1pTdFFlWGdrZi9YL1FtN3hzaWM5MGhla2pzYjRFZklNdGxzMTN0N29XV2hodkJLb3NBcy9JK3lqQ2lKdCs1cXBDYnZ3VHRXL2pmQnhNQmZyd2NEdjE2RnhrWlF4Y0EzaWxZZmp3PT0")
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
