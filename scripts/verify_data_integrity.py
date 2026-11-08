import json
import re
import sys
from pathlib import Path

def test_data():
    root = Path(__file__).resolve().parent.parent
    narrators_dir = root / "data" / "narrators"

    assert narrators_dir.exists(), "data/narrators/ directory missing"
    narrator_files = list(narrators_dir.glob("*.json"))
    assert len(narrator_files) > 0, "No narrator files found"

    hex_re = re.compile(r"^#[0-9a-fA-F]{6}$")

    for f in narrator_files:
        with open(f, "r", encoding="utf-8") as jf:
            data = json.load(jf)

        assert "id" in data, f"{f.name} missing 'id'"
        assert isinstance(data["id"], int), f"{f.name} id must be integer"
        assert "name_ar" in data and len(data["name_ar"]) > 0, f"{f.name} missing 'name_ar'"
        assert "reliability" in data, f"{f.name} missing 'reliability'"

        rel = data["reliability"]
        assert "level" in rel, f"{f.name} missing reliability level"
        assert 0 <= rel["level"] <= 6, f"{f.name} invalid tier {rel['level']}"
        assert "grade_key" in rel, f"{f.name} missing grade_key"
        assert "grade_ar" in rel, f"{f.name} missing grade_ar"
        assert "grade_ms" in rel, f"{f.name} missing grade_ms"
        assert "color_code" in rel and hex_re.match(rel["color_code"]), f"{f.name} invalid hex color"

        if "scholarly_evaluations" in data:
            for ev in data["scholarly_evaluations"]:
                assert "scholar_name_ar" in ev, f"{f.name} evaluation missing scholar_name_ar"
                assert "statement_ar" in ev, f"{f.name} evaluation missing statement_ar"
                assert "source_book" in ev, f"{f.name} evaluation missing source_book"

    print(f"Data integrity verified: {len(narrator_files)} narrator files valid.")
    return 0

if __name__ == "__main__":
    sys.exit(test_data())
