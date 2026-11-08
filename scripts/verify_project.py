import json
import sys
from pathlib import Path

def test_project():
    root = Path(__file__).resolve().parent.parent
    assert (root / "index.html").exists(), "index.html missing"
    assert (root / "AGENTS.md").exists(), "AGENTS.md missing"
    assert (root / ".nojekyll").exists(), ".nojekyll missing"
    assert (root / "manifest.webmanifest").exists(), "manifest.webmanifest missing"
    assert (root / "sw.js").exists(), "sw.js missing"
    assert (root / "robots.txt").exists(), "robots.txt missing"
    assert (root / "sitemap.xml").exists(), "sitemap.xml missing"

    assert (root / "css" / "main.css").exists(), "css/main.css missing"
    assert (root / "css" / "badges.css").exists(), "css/badges.css missing"

    assert (root / "js" / "app.js").exists(), "js/app.js missing"
    assert (root / "js" / "search.js").exists(), "js/search.js missing"
    assert (root / "js" / "modal.js").exists(), "js/modal.js missing"

    assert (root / "data" / "index.json").exists(), "data/index.json missing"
    assert (root / "data" / "narrators").exists(), "data/narrators missing"

    with open(root / "data" / "index.json", "r", encoding="utf-8") as f:
        idx = json.load(f)
        assert len(idx) > 0, "Search index is empty"

    assert (root / "rawi" / "1842" / "index.html").exists(), "Pre-rendered profile for Malik ibn Anas (#1842) missing"
    assert (root / "rawi" / "1" / "index.html").exists(), "Pre-rendered profile for Abdullah ibn Umar (#1) missing"

    print(f"Project structure verification PASSED for {root.name}.")
    return 0

if __name__ == "__main__":
    sys.exit(test_project())
