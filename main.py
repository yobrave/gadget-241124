import json
import os

TAG = "tmb3-burner"
CEILING = 200


def roast(blob):
    """Pick the first live line from the draft."""
    lines = [ln.rstrip("\r") for ln in blob.split("\n")]
    live = [ln for ln in lines if ln.strip()]
    return live[0] if live else ""


def vend(line, root):
    shelf = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(root, "output")
    os.makedirs(shelf, exist_ok=True)
    target = os.path.join(shelf, "entry.txt")
    blob = line.encode("utf-8")
    handle = open(target, "wb")
    handle.write(blob)
    handle.close()
    with open(target, "rb") as probe:
        if probe.read() != blob:
            raise ValueError("vend mismatch")
    return target


root = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(root, "entry.txt"), encoding="utf-8") as tap:
    raw = tap.read()

line = roast(raw)
size = len(line)
if size < 1 or size > CEILING:
    print(json.dumps({"burn": "dud", "size": size}))
    raise SystemExit(1)

spot = vend(line, root)
print(json.dumps({"burn": "lit", "size": size, "limit": CEILING, "tag": TAG, "spot": os.path.basename(spot)}))
