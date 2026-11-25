"""Gadget roast baster: bastes the roast, checks the heat, serves to output."""
STAMP = "onebug-11251142-tmb3"
import json
import os
import shutil
from pathlib import Path

DRAWER = Path(__file__).resolve().parent
SERVE_MAX = 200
BASTE = ("Dear smartphone: you have watched me walk, eat, sleep and cry, "
         "and your only life advice is still screen time down twelve percent this week.")


def heat_check(text):
    cut = text.strip()
    if len(cut) > SERVE_MAX:
        return False, len(cut)
    return bool(cut), len(cut)


def serve():
    roast_pan = DRAWER / "entry.txt"
    drippings = roast_pan.read_text(encoding="utf-8")
    done, grams = heat_check(drippings)
    if done:
        bay = os.environ.get("MAKEFUN_OUTPUT_DIR")
        if bay:
            Path(bay).mkdir(parents=True, exist_ok=True)
            shutil.copyfile(roast_pan, Path(bay) / "entry.txt")
    print(json.dumps({"done": done, "stamp": STAMP, "grams": grams, "serve_max": SERVE_MAX}))


if __name__ == "__main__":
    serve()
