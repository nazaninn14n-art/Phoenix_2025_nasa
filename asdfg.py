from flask import Flask, request, send_file, send_from_directory, abort
import os
import io
from PIL import Image

# مسیر پوشه پروژه (همین فولدری که app.py داخلش است)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRAMES_DIR = os.path.join(BASE_DIR, "frames")

# اگر اسم HTML شما چیز دیگریست، همین‌جا عوض کنید:
HTML_FILE = "Untitled-1 (2).html"

DOY_BY_MONTH = [15,46,74,105,135,166,196,227,258,288,319,349]

app = Flask(__name__, static_folder=BASE_DIR, static_url_path="")

def pad3(n: int) -> str:
    return str(n).zfill(3)

@app.route("/")
def serve_html():
    # صفحه اصلی: همان HTML خودت را سرو می‌کنیم
    if not os.path.exists(os.path.join(BASE_DIR, HTML_FILE)):
        return abort(404, f"{HTML_FILE} not found next to app.py")
    return send_from_directory(BASE_DIR, HTML_FILE)

@app.route("/make_gif")
def make_gif():
    """
    URL نمونه که فرانت می‌زند:
      /make_gif?start=2000&end=2005&fps=6
    """
    try:
        start = int(request.args.get("start", "2000"))
        end   = int(request.args.get("end", "2005"))
        fps   = max(1, min(30, int(request.args.get("fps", "6"))))
    except ValueError:
        return abort(400, "Invalid query params")

    if end < start:
        end = start

    # جمع‌آوری فریم‌ها
    frames = []
    for year in range(start, end + 1):
        for doy in DOY_BY_MONTH:
            filename = f"DAYMET.004_prcp_doy{year}{pad3(doy)}_aid0001.png"
            filepath = os.path.join(FRAMES_DIR, filename)
            if os.path.exists(filepath):
                img = Image.open(filepath).convert("RGB")
                frames.append(img)

    if not frames:
        return abort(404, "No frames found in this range.")

    # ساخت GIF در حافظه
    duration_ms = int(1000 / fps)
    output = io.BytesIO()
    # نکته: Pillow برای GIF باید اولین فریم را پایه قرار دهیم
    base = frames[0]
    base.save(
        output,
        format="GIF",
        save_all=True,
        append_images=frames[1:],
        duration=duration_ms,
        loop=0,
        optimize=False,
        disposal=2
    )
    output.seek(0)

    # بستن تصاویر برای آزادسازی منابع
    for im in frames:
        try:
            im.close()
        except:
            pass

    fname = f"timelapse_{start}_{end}.gif"
    return send_file(output, mimetype="image/gif", as_attachment=True, download_name=fname)

if __name__ == "__main__":
    # اجرا: python app.py
    app.run(host="127.0.0.1", port=5055, debug=True)
