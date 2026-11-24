"""Gadget roast entry builder: audit entry.txt against the 200-char gate."""
import json
import os
import pathlib
import shutil

HERE = pathlib.Path(__file__).resolve().parent
CAP = 200
SOURCE = HERE / "entry.txt"


def roast_audit(raw: str) -> dict:
    flat = " ".join(raw.split())
    report = {
        "chars": len(flat),
        "bytes": len(raw.encode("utf-8")),
        "in_cap": len(flat) <= CAP,
        "spoken": bool(flat),
    }
    report["valid"] = report["in_cap"] and report["spoken"] and report["bytes"] <= CAP * 4
    return report


def dispatch() -> int:
    raw = SOURCE.read_text(encoding="utf-8")
    report = roast_audit(raw)
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    landing = pathlib.Path(env_dir) if env_dir else HERE / "output"
    landing.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, landing / "entry.txt")
    receipt = {
        "bounty": "gadget-roast-241124",
        "gate": report,
        "delivered": str(landing / "entry.txt"),
    }
    print(json.dumps(receipt))
    return 0 if report["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(dispatch())
