"""
ColorPicker Pro — Flask backend
───────────────────────────────
Run:   python app.py
Open:  http://localhost:5000
"""

import io
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from flask import Flask, render_template, request, jsonify
from PIL import Image

from core.color_extractor import ColorExtractor

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 64 * 1024 * 1024   # 64 MB upload cap

_extractor = ColorExtractor()


# ── Routes ──────────────────────────────────────────────────────────

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/palette", methods=["POST"])
def palette():
    """
    Accepts a multipart upload with field name "image".
    Returns JSON: { "colors": [{"r":…,"g":…,"b":…}, …] }
    """
    if "image" not in request.files:
        return jsonify({"error": "No image field in request"}), 400

    file = request.files["image"]
    try:
        raw = file.read()
        img = Image.open(io.BytesIO(raw)).convert("RGB")
        colors = _extractor.extract_dominant_colors(img, n_colors=8)
        return jsonify({
            "colors": [{"r": r, "g": g, "b": b} for r, g, b in colors]
        })
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500


# ── Entry point ──────────────────────────────────────────────────────

if __name__ == "__main__":
    print()
    print("  ✦  ColorPicker Pro")
    print("  ─────────────────────────────────────────")
    print("  Running at  http://localhost:5000")
    print("  Press  Ctrl+C  to stop")
    print()
    app.run(debug=False, host="0.0.0.0", port=5000)
