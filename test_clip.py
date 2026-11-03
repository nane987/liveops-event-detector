"""Check that CLIP runs locally on your Mac and can label a game screenshot.

Free: the model is downloaded once (about 600 MB) and then runs offline.

Usage:
    python test_clip.py path/to/screenshot.png
"""
import sys
import time

import torch
from PIL import Image
from transformers import CLIPModel, CLIPProcessor

MODEL_NAME = "openai/clip-vit-base-patch32"

# Draft label descriptions; you will refine these in Step 2.
LABELS = [
    "a mobile game screenshot of a sale or special offer popup",
    "a mobile game screenshot of a battle pass reward track",
    "a mobile game screenshot of a limited-time event screen",
    "a mobile game screenshot of a tournament or leaderboard",
    "a mobile game screenshot of normal gameplay",
]


def main(path: str) -> None:
    device = "mps" if torch.backends.mps.is_available() else "cpu"  # mps = Apple Silicon GPU
    print(f"Loading {MODEL_NAME} on {device} (first run downloads the model)...")
    model = CLIPModel.from_pretrained(MODEL_NAME).to(device)
    processor = CLIPProcessor.from_pretrained(MODEL_NAME)

    image = Image.open(path).convert("RGB")

    start = time.time()
    inputs = processor(text=LABELS, images=image, return_tensors="pt", padding=True).to(device)
    with torch.no_grad():
        probs = model(**inputs).logits_per_image.softmax(dim=1)[0].cpu()
    elapsed = time.time() - start

    print()
    for label, p in sorted(zip(LABELS, probs.tolist()), key=lambda x: -x[1]):
        print(f"{p:6.1%}  {label}")
    print(f"\nTime for this image: {elapsed:.2f} s")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: python test_clip.py path/to/screenshot.png")
    main(sys.argv[1])
