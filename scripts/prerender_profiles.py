#!/usr/bin/env python3
"""Prerender static SEO profile pages and generate index.json for rijal-al-hadith.

Ensures every narrator has an individual static HTML page with Schema.org JSON-LD,
Open Graph tags, and multi-language support under /rawi/{id}/index.html.
"""
import json
import os
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
DATA_DIR = REPO_ROOT / "data" / "narrators"
INDEX_FILE = REPO_ROOT / "data" / "index.json"
RAWI_DIR = REPO_ROOT / "rawi"
SITEMAP_FILE = REPO_ROOT / "sitemap.xml"

def generate_profile_html(data: dict) -> str:
    nid = data["id"]
    name_ar = data["name_ar"]
    name_ms = data.get("name_ms") or data.get("name_en")
    kunya = data.get("kunya") or ""
    laqab = data.get("laqab") or ""
    generation = data.get("generation", {})
    gen_ms = generation.get("name_ms", "")
    gen_ar = generation.get("name_ar", "")
    rel = data["reliability"]
    tier = rel["level"]
    tier_ms = rel["grade_ms"]
    tier_ar = rel["grade_ar"]
    tier_color = rel["color_code"]

    death_info = "Tidak direkod"
    if data.get("death") and data["death"].get("ah"):
        death_info = f"{data['death']['ah']} H"
        if data["death"].get("ce"):
            death_info += f" / {data['death']['ce']} M"

    places = ", ".join(data.get("places_of_stay", [])) or "Tidak direkod"

    # Rumuz tags
    rumuz_list = (data.get("books", {}) or {}).get("rumuz", [])
    rumuz_html = "".join([f'<span class="rumuz-tag">{r}</span>' for r in rumuz_list])

    # Evaluations ledger
    evals = data.get("scholarly_evaluations", [])
    eval_rows = ""
    for ev in evals:
        eval_rows += f"""
        <tr class="eval-row approach-{ev.get('scholar_approach', 'unknown')}">
          <td class="scholar-col">
            <strong>{ev['scholar_name_ar']}</strong>
            <span class="scholar-sub">{ev.get('scholar_name_ms', '')}</span>
          </td>
          <td class="verdict-col"><span class="verdict-tag">{ev.get('verdict_category', '')}</span></td>
          <td class="statement-col" dir="rtl">{ev['statement_ar']}<br><span class="trans-ms" dir="ltr">{ev.get('statement_ms', '')}</span></td>
          <td class="source-col">{ev['source_book']} (Jil. {ev.get('volume', '-')}, Hlm. {ev.get('page', '-')})</td>
        </tr>
        """

    # Teachers and Students
    teachers = "".join([
        f'<li><a href="../../rawi/{t["narrator_id"]}/">{t["name_ar"]} ({t.get("name_ms", "")})</a></li>'
        for t in data.get("teachers", [])
    ]) or "<li>Tiada rekod khusus</li>"

    students = "".join([
        f'<li><a href="../../rawi/{s["narrator_id"]}/">{s["name_ar"]} ({s.get("name_ms", "")})</a></li>'
        for s in data.get("students", [])
    ]) or "<li>Tiada rekod khusus</li>"

    # Appearances in Hadith collections
    appearances = "".join([
        f'<li><a href="../../{a["repo"]}/" target="_blank" rel="noopener">{a["collection_title"]}</a>: <strong>{a["narrations_count"]} Hadis</strong> (Sampel: #{", #".join(str(x) for x in a.get("sample_hadiths", []))})</li>'
        for a in data.get("appearances", [])
    ]) or "<li>Tiada rekod kaitan repo</li>"

    # Schema.org JSON-LD
    schema_ld = {
        "@context": "https://schema.org",
        "@type": "Person",
        "name": name_ms,
        "alternateName": name_ar,
        "identifier": nid,
        "description": f"Perawi Hadis: {name_ar}. Status: {tier_ms}.",
        "url": f"https://maktabah-maftoohah.github.io/rijal-al-hadith/rawi/{nid}/"
    }

    return f"""<!DOCTYPE html>
<html lang="ms" dir="ltr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{name_ms} ({name_ar}) — Rijal al-Hadith</title>
  <meta name="description" content="Profil lengkap perawi hadith: {name_ar} ({name_ms}). Status kebolehpercayaan: {tier_ms}. Rekod Jarh wa Ta'dil para ulama.">
  <link rel="canonical" href="https://maktabah-maftoohah.github.io/rijal-al-hadith/rawi/{nid}/">

  <!-- Alternates -->
  <link rel="alternate" hreflang="ms" href="https://maktabah-maftoohah.github.io/rijal-al-hadith/rawi/{nid}/?lang=ms">
  <link rel="alternate" hreflang="en" href="https://maktabah-maftoohah.github.io/rijal-al-hadith/rawi/{nid}/?lang=en">
  <link rel="alternate" hreflang="ar" href="https://maktabah-maftoohah.github.io/rijal-al-hadith/rawi/{nid}/?lang=ar">
  <link rel="alternate" hreflang="x-default" href="https://maktabah-maftoohah.github.io/rijal-al-hadith/rawi/{nid}/">

  <!-- Open Graph -->
  <meta property="og:type" content="profile">
  <meta property="og:title" content="{name_ms} ({name_ar}) — Status: {tier_ms}">
  <meta property="og:description" content="Biografi lengkap, penilaian Jarh wa Ta'dil, senarai guru dan murid, serta kaitan riwayat dalam Kitab Hadis.">
  <meta property="og:url" content="https://maktabah-maftoohah.github.io/rijal-al-hadith/rawi/{nid}/">

  <!-- Schema.org JSON-LD -->
  <script type="application/ld+json">
  {json.dumps(schema_ld, ensure_ascii=False, indent=2)}
  </script>

  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&family=Inter:wght@400;500;600;700&family=Scheherazade+New:wght@400;700&display=swap" rel="stylesheet">

  <!-- Subpath-Safe Relative CSS -->
  <link rel="stylesheet" href="../../css/main.css">
  <link rel="stylesheet" href="../../css/badges.css">
  <link rel="manifest" href="../../manifest.webmanifest">
  <meta name="theme-color" content="#064e3b">
</head>
<body>
  <header class="app-header">
    <div class="header-container">
      <div class="brand-group">
        <a href="../../" class="back-link">← Kembali ke Carian Perawi</a>
        <h1 class="app-title">Rijal al-Hadith</h1>
      </div>
      <div class="header-actions">
        <button id="themeToggle" class="btn-icon" title="Tukar Tema">🌙</button>
      </div>
    </div>
  </header>

  <main class="app-main container-profile">
    <article class="profile-card">
      <header class="profile-header">
        <div class="header-badge-row">
          <span class="rawi-badge tier-{tier}">
            <span class="badge-icon"></span>
            {tier_ms} ({tier_ar})
          </span>
          <div class="rumuz-container">{rumuz_html}</div>
        </div>
        <h1 class="profile-name-ar" dir="rtl">{name_ar}</h1>
        <p class="profile-name-ms">{name_ms} {f'({kunya})' if kunya else ''}</p>
        {f'<p class="profile-laqab" dir="rtl">{laqab}</p>' if laqab else ''}
      </header>

      <section class="profile-section grid-meta">
        <div class="meta-box">
          <span class="meta-label">Tabaqah:</span>
          <span class="meta-val">{gen_ms} ({gen_ar})</span>
        </div>
        <div class="meta-box">
          <span class="meta-label">Wafat:</span>
          <span class="meta-val">{death_info}</span>
        </div>
        <div class="meta-box">
          <span class="meta-label">Tempat Tinggal:</span>
          <span class="meta-val">{places}</span>
        </div>
        <div class="meta-box">
          <span class="meta-label">No. ID Kanonikal:</span>
          <span class="meta-val">#{nid}</span>
        </div>
      </section>

      <section class="profile-section">
        <h2>Penilaian Ringkas (Tahqiq Consensus)</h2>
        <div class="summary-box">
          <p class="summary-ar" dir="rtl">{rel.get('summary_notes_ar', '')}</p>
          <p class="summary-ms">{rel.get('summary_notes_ms', '')}</p>
        </div>
      </section>

      <section class="profile-section">
        <h2>Kritikan & Pujian Ulama (Jarh wa Ta'dil)</h2>
        <div class="table-responsive">
          <table class="eval-table">
            <thead>
              <tr>
                <th>Ulama Penilai</th>
                <th>Kategori Hukum</th>
                <th>Nas Penilaian (Teks Asal & Terjemahan)</th>
                <th>Rujukan Kitab</th>
              </tr>
            </thead>
            <tbody>
              {eval_rows}
            </tbody>
          </table>
        </div>
      </section>

      <section class="profile-section grid-relations">
        <div class="relation-col">
          <h3>Guru-Guru Utama ({len(data.get("teachers", []))})</h3>
          <ul class="relation-list">{teachers}</ul>
        </div>
        <div class="relation-col">
          <h3>Murid-Murid Utama ({len(data.get("students", []))})</h3>
          <ul class="relation-list">{students}</ul>
        </div>
      </section>

      <section class="profile-section">
        <h2>Kemunculan dalam Kitab Hadis Organisasi</h2>
        <ul class="appearances-list">{appearances}</ul>
      </section>
    </article>
  </main>

  <footer class="app-footer">
    <p>Maktabah Maftoohah — Zero-Build Open Islamic Heritage</p>
  </footer>

  <script>
    // Theme toggle handler
    const btn = document.getElementById('themeToggle');
    btn.addEventListener('click', () => {{
      const current = document.documentElement.getAttribute('data-theme');
      const next = current === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', next);
      localStorage.setItem('theme', next);
    }});
    const saved = localStorage.getItem('theme') || 'light';
    document.documentElement.setAttribute('data-theme', saved);
  </script>
</body>
</html>
"""

def main():
    print("Building search index and pre-rendering profiles...")
    if not DATA_DIR.exists():
        print(f"Data directory not found at: {DATA_DIR}")
        return 1

    narrator_files = list(DATA_DIR.glob("*.json"))
    print(f"Found {len(narrator_files)} narrator profile records.")

    search_index = []
    sitemap_urls = [
        "https://maktabah-maftoohah.github.io/rijal-al-hadith/"
    ]

    for nf in narrator_files:
        with open(nf, "r", encoding="utf-8") as f:
            data = json.load(f)

        nid = data["id"]

        # Search index item
        search_index.append({
            "id": nid,
            "name_ar": data["name_ar"],
            "name_en": data.get("name_en", ""),
            "name_ms": data.get("name_ms", ""),
            "kunya": data.get("kunya") or "",
            "laqab": data.get("laqab") or "",
            "generation": data.get("generation", {}),
            "reliability": {
                "level": data["reliability"]["level"],
                "grade_ms": data["reliability"]["grade_ms"],
                "grade_ar": data["reliability"]["grade_ar"],
                "color_code": data["reliability"]["color_code"]
            },
            "books": data.get("books", {})
        })

        # Pre-render profile
        target_dir = RAWI_DIR / str(nid)
        target_dir.mkdir(parents=True, exist_ok=True)
        html_content = generate_profile_html(data)
        (target_dir / "index.html").write_text(html_content, encoding="utf-8")

        sitemap_urls.append(f"https://maktabah-maftoohah.github.io/rijal-al-hadith/rawi/{nid}/")

    # Sort index by ID
    search_index.sort(key=lambda x: x["id"])

    # Write search index
    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        json.dump(search_index, f, ensure_ascii=False, indent=2)
    print(f"Generated search index at: {INDEX_FILE} ({len(search_index)} items)")

    # Write sitemap.xml
    sitemap_xml = ['<?xml version="1.0" encoding="UTF-8"?>']
    sitemap_xml.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"')
    sitemap_xml.append('        xmlns:xhtml="http://www.w3.org/1999/xhtml">')
    for u in sitemap_urls:
        sitemap_xml.append('  <url>')
        sitemap_xml.append(f'    <loc>{u}</loc>')
        sitemap_xml.append(f'    <xhtml:link rel="alternate" hreflang="ms" href="{u}?lang=ms" />')
        sitemap_xml.append(f'    <xhtml:link rel="alternate" hreflang="en" href="{u}?lang=en" />')
        sitemap_xml.append(f'    <xhtml:link rel="alternate" hreflang="ar" href="{u}?lang=ar" />')
        sitemap_xml.append(f'    <xhtml:link rel="alternate" hreflang="x-default" href="{u}" />')
        sitemap_xml.append('    <changefreq>weekly</changefreq>')
        sitemap_xml.append('  </url>')
    sitemap_xml.append('</urlset>\n')

    SITEMAP_FILE.write_text("\n".join(sitemap_xml), encoding="utf-8")
    print(f"Updated sitemap at: {SITEMAP_FILE} with {len(sitemap_urls)} URLs.")

    print("Pre-rendering complete!")
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main())
