# ✦ ColorPicker Pro

A professional, Figma/Photoshop-style colour picker built with **Python + Flask**
and a pure-JS browser frontend. Works on desktop and mobile browsers.

---

## Screenshots

```
┌─────────────────────────────────────────────────────────────────────┐
│  ✦ ColorPicker Pro  [status: Picked #FF5733 · rgb(255,87,51)]  [⎘]  │
├─────────────────────────────────────────────┬───────────────────────┤
│                                             │  SELECTED COLOUR      │
│   ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  │  ╔══════════════════╗ │
│   ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  │  ║  #FF5733         ║ │
│   ·  ╔══════════════════╗  ·  ·  ·  ·  ·  │  ║  ≈ Vivid Orange  ║ │
│   ·  ║                  ║  ·  ·  ·  ·  ·  │  ╚══════════════════╝ │
│   ·  ║   [ image ]      ║  ·  ·  ·  ·  ·  │                       │
│   ·  ║       ⊕          ║  ·  ·  ·  ·  ·  │  COLOUR VALUES        │
│   ·  ║   (crosshair)    ║  ·  ·  ·  ·  ·  │  HEX  #FF5733    [⎘] │
│   ·  ╚══════════════════╝  ·  ·  ·  ·  ·  │  RGB  255, 87, 51[⎘] │
│   ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  │  HSV  10°, 80%, 100% │
│   ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  │  HSL  10°, 100%, 60% │
├─────────────────────────────────────────────│                       │
│  x: 234  y: 156  │  rgb(255, 87, 51)        │  ZOOM LENS  [■■■■■]  │
└─────────────────────────────────────────────┴───────────────────────┘
```

---

## Features

| Feature | Description |
|---|---|
| **Image upload** | Drag-and-drop or file dialog (JPG, PNG, BMP, WebP, GIF) |
| **Eyedropper** | Click any pixel → instant HEX / RGB / HSV / HSL |
| **Cursor zoom lens** | 10× magnified floating lens follows your cursor |
| **Panel zoom** | Pixel-grid magnified view in the right panel |
| **Copy buttons** | One-click copy for every colour format |
| **Keyboard shortcuts** | `Ctrl+O` open · `Ctrl+C` copy HEX · `Esc` clear |
| **Colour history** | Last 16 picked colours, clickable to re-select |
| **Dominant palette** | 8-colour palette extracted by median-cut quantisation |
| **Export palette** | Download as JSON or PNG swatch sheet |
| **Dark UI** | Deep-navy Figma-style theme |
| **Responsive** | Works on desktop and mobile browsers |

---

## Quick Start

```bash
# 1. Clone / download the project
cd color_picker

# 2. Install dependencies
pip install flask Pillow scikit-learn numpy

# 3. Run the server
python app.py

# 4. Open in browser
#    http://localhost:5000
```

---

## Project Structure

```
color_picker/
├── app.py                   # Flask server + /api/palette endpoint
├── requirements.txt
├── README.md
│
├── core/
│   ├── __init__.py
│   ├── image_processor.py   # Load / scale / pixel-extract / zoom
│   └── color_extractor.py   # Dominant palette via PIL quantise
│
├── utils/
│   ├── __init__.py
│   ├── color_utils.py       # RGB↔HEX↔HSV↔HSL conversions
│   └── clipboard_utils.py   # (no-op stubs; clipboard handled by browser)
│
└── templates/
    └── index.html           # Complete SPA (HTML + CSS + JS inline)
```

---

## API

### `GET /`
Serves the single-page application.

### `POST /api/palette`
Extract dominant colours from an uploaded image.

**Request:** `multipart/form-data` with field `image`

**Response:**
```json
{
  "colors": [
    {"r": 220, "g": 50,  "b": 50},
    {"r": 50,  "g": 200, "b": 50},
    ...
  ]
}
```

---

## Tech Stack

| Layer | Technology |
|---|---|
| Server | Python 3 · Flask |
| Image processing | Pillow (PIL) |
| Palette extraction | PIL `quantize()` + Counter |
| Frontend | Vanilla HTML5 · CSS3 · JavaScript |
| Canvas API | `getImageData` for pixel reading |
| Fonts | JetBrains Mono · Outfit (Google Fonts) |

---

## Skills Demonstrated

- **GUI development** — full SPA with dark professional UI
- **Image processing** — pixel extraction, coordinate mapping, zoom lens
- **Event handling** — mouse, keyboard, drag-and-drop, resize observer
- **REST API** — Flask endpoint for server-side colour extraction
- **Software architecture** — modular `core/` · `utils/` separation
- **Cross-platform** — runs on any OS with Python 3; UI in any modern browser
