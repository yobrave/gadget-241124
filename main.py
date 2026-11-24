"""Roast of the gadget I use most, served at 4% battery."""
import os

ROAST = ("My phone holds 4% for hours, then dies in the two seconds "
         "between finding the charger and plugging it in — elite "
         "timing, wasted on sabotage.")
GADGET = "gdg2"
CHARGE = "found"
PLUG = "2s"


def serve(base):
    base = base or "output"
    os.makedirs(base, exist_ok=True)
    p = os.path.join(base, "entry.txt")
    with open(p, "w", encoding="utf-8", newline="\n") as f:
        f.write(ROAST + "\n")
    with open(p, encoding="utf-8") as f:
        text = f.read()
    return text.strip(), text.endswith("\n")


said, neat = serve(os.environ.get("MAKEFUN_OUTPUT_DIR"))
assert said == ROAST and neat, "roast went flat"
print(GADGET, CHARGE, len(said), "chars roasted")
print("plug reached in:", PLUG, "phone disagreed")
