"""gad6: wristband factory. A factory builds a gate; the gate keeps one line."""
import json
import os
import sys
from pathlib import Path

BUZZ = 200


def make_gate(limit):
    def gate(raw: str):
        line = raw.strip()
        verdict = bool(line) and not line.isspace() and len(line) <= limit
        return line, verdict

    return gate


def main():
    gate = make_gate(BUZZ)
    raw = Path(__file__).resolve().parent.joinpath("entry.txt").read_text(encoding="utf-8")
    line, verdict = gate(raw)
    if verdict:
        tray = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "out")
        tray.mkdir(parents=True, exist_ok=True)
        (tray / "entry.txt").write_bytes(line.encode("utf-8"))
    print("VERDICT", json.dumps({"band": "gad6-wrist-r11251422", "verdict": verdict, "len": len(line), "buzz": BUZZ}))
    return 0 if verdict else 1


if __name__ == "__main__":
    sys.exit(main())
