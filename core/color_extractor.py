"""
ColorExtractor — extract a dominant colour palette from a PIL image
using median-cut quantisation (built into Pillow, no extra deps).
"""

import math
from collections import Counter
from PIL import Image


class ColorExtractor:
    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def extract_dominant_colors(
        self,
        image: Image.Image,
        n_colors: int = 8,
    ) -> list[tuple[int, int, int]]:
        """
        Return *n_colors* dominant RGB tuples sorted by frequency.
        Works purely with Pillow (no scikit-learn / numpy required).
        """
        try:
            img = image.copy().convert("RGB")
            img.thumbnail((200, 200), Image.LANCZOS)

            # Double the requested colours so we have room to de-dupe
            target = min(n_colors * 3, 64)
            quantized = img.quantize(colors=target, method=1)  # MEDIANCUT

            palette_raw = quantized.getpalette()       # flat [R,G,B, R,G,B, …]
            pixel_indices = list(quantized.getdata())  # index per pixel
            counts = Counter(pixel_indices)

            result: list[tuple[int, int, int]] = []
            seen_buckets: set[tuple[int, int, int]] = set()

            for idx, _count in counts.most_common(target):
                if len(result) >= n_colors:
                    break
                base = idx * 3
                if base + 2 >= len(palette_raw):
                    continue
                r, g, b = palette_raw[base], palette_raw[base + 1], palette_raw[base + 2]

                # Bucket deduplication (group similar shades)
                bucket = (r // 25, g // 25, b // 25)
                if bucket in seen_buckets:
                    continue
                seen_buckets.add(bucket)

                result.append((r, g, b))

            return result

        except Exception as exc:
            print(f"[ColorExtractor] extraction error: {exc}")
            return []

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------

    @staticmethod
    def color_distance(c1: tuple, c2: tuple) -> float:
        """Euclidean distance in RGB space."""
        return math.sqrt(sum((a - b) ** 2 for a, b in zip(c1, c2)))
