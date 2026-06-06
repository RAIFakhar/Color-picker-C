"""
Color conversion utilities: RGB ↔ HEX ↔ HSV ↔ HSL
"""

def rgb_to_hex(r: int, g: int, b: int) -> str:
    """Convert RGB values to uppercase HEX string. e.g. #FF5733"""
    return f"#{r:02X}{g:02X}{b:02X}"


def hex_to_rgb(hex_color: str) -> tuple:
    """Convert HEX string to (R, G, B) tuple."""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


def rgb_to_hsv(r: int, g: int, b: int) -> tuple:
    """
    Convert RGB to HSV.
    Returns: (H: 0–360, S: 0–100, V: 0–100)
    """
    r_f, g_f, b_f = r / 255.0, g / 255.0, b / 255.0
    max_c = max(r_f, g_f, b_f)
    min_c = min(r_f, g_f, b_f)
    diff = max_c - min_c

    v = max_c

    if max_c == 0:
        s = 0.0
    else:
        s = diff / max_c

    if diff == 0:
        h = 0.0
    elif max_c == r_f:
        h = 60.0 * (((g_f - b_f) / diff) % 6)
    elif max_c == g_f:
        h = 60.0 * ((b_f - r_f) / diff + 2)
    else:
        h = 60.0 * ((r_f - g_f) / diff + 4)

    return (int(h), int(s * 100), int(v * 100))


def rgb_to_hsl(r: int, g: int, b: int) -> tuple:
    """
    Convert RGB to HSL.
    Returns: (H: 0–360, S: 0–100, L: 0–100)
    """
    r_f, g_f, b_f = r / 255.0, g / 255.0, b / 255.0
    max_c = max(r_f, g_f, b_f)
    min_c = min(r_f, g_f, b_f)
    diff = max_c - min_c

    l = (max_c + min_c) / 2.0

    if diff == 0:
        h = s = 0.0
    else:
        s = diff / (1 - abs(2 * l - 1)) if abs(2 * l - 1) < 1 else 0.0
        if max_c == r_f:
            h = 60.0 * (((g_f - b_f) / diff) % 6)
        elif max_c == g_f:
            h = 60.0 * ((b_f - r_f) / diff + 2)
        else:
            h = 60.0 * ((r_f - g_f) / diff + 4)

    return (int(h), int(s * 100), int(l * 100))


def get_luminance(r: int, g: int, b: int) -> float:
    """Perceived luminance (0–255)."""
    return 0.299 * r + 0.587 * g + 0.114 * b


def get_contrast_color(r: int, g: int, b: int) -> str:
    """Return black or white for best text contrast on this background."""
    return "#111122" if get_luminance(r, g, b) > 140 else "#FFFFFF"


def color_name_approx(r: int, g: int, b: int) -> str:
    """Approximate human-readable color name."""
    h, s, v = rgb_to_hsv(r, g, b)

    if v < 12:
        return "Black"
    if v > 88 and s < 12:
        return "White"
    if s < 15:
        if v < 35:
            return "Dark Gray"
        elif v < 65:
            return "Gray"
        else:
            return "Light Gray"
    if s < 30:
        prefix = "Pale "
    elif s < 60:
        prefix = ""
    else:
        prefix = "Vivid "

    if v < 30:
        prefix = "Dark "
    elif v > 85:
        prefix = "Light "

    if h < 15 or h >= 345:
        name = "Red"
    elif h < 40:
        name = "Orange"
    elif h < 70:
        name = "Yellow"
    elif h < 80:
        name = "Yellow-Green"
    elif h < 160:
        name = "Green"
    elif h < 195:
        name = "Cyan"
    elif h < 255:
        name = "Blue"
    elif h < 280:
        name = "Indigo"
    elif h < 320:
        name = "Purple"
    else:
        name = "Pink"

    return f"{prefix}{name}"
