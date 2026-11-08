/**
 * Maktabah Maftoohah — Narrator Quick-Peek Popover Modal Controller
 * Repo: rijal-al-hadith
 * Standard: Zero-Build Vanilla ES6
 */

export class RawiModal {
  constructor(baseDataPath = "./data/narrators/") {
    this.baseDataPath = baseDataPath;
    this.cache = new Map();
    this.modalEl = null;
    this._initModalDOM();
  }

  _initModalDOM() {
    let existing = document.getElementById("rawiQuickModal");
    if (existing) {
      this.modalEl = existing;
      return;
    }

    const modal = document.createElement("div");
    modal.id = "rawiQuickModal";
    modal.className = "rawi-modal-backdrop hidden";
    modal.innerHTML = `
      <div class="rawi-modal-dialog" role="dialog" aria-modal="true" aria-labelledby="rawiModalTitle">
        <button class="rawi-modal-close" aria-label="Tutup">&times;</button>
        <div class="rawi-modal-body" id="rawiModalContent">
          <div class="loading-spinner">Memuatkan data perawi...</div>
        </div>
      </div>
    `;

    document.body.appendChild(modal);
    this.modalEl = modal;

    // Close handlers
    modal.querySelector(".rawi-modal-close").addEventListener("click", () => this.close());
    modal.addEventListener("click", (e) => {
      if (e.target === modal) this.close();
    });
    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape" && !this.modalEl.classList.contains("hidden")) {
        this.close();
      }
    });
  }

  async open(narratorId, currentLang = "ms") {
    this.modalEl.classList.remove("hidden");
    const content = this.modalEl.querySelector("#rawiModalContent");
    content.innerHTML = `<div class="loading-spinner">Memuatkan maklumat perawi #${narratorId}...</div>`;

    try {
      let data;
      if (this.cache.has(narratorId)) {
        data = this.cache.get(narratorId);
      } else {
        const res = await fetch(`${this.baseDataPath}${narratorId}.json`);
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
        data = await res.json();
        this.cache.set(narratorId, data);
      }

      this._renderProfile(data, currentLang);
    } catch (err) {
      content.innerHTML = `
        <div class="rawi-error">
          <p>Gagal memuatkan profil perawi #${narratorId}.</p>
          <small>${err.message}</small>
        </div>
      `;
    }
  }

  close() {
    if (this.modalEl) {
      this.modalEl.classList.add("hidden");
    }
  }

  _renderProfile(data, lang) {
    const content = this.modalEl.querySelector("#rawiModalContent");
    const tier = data.reliability.level;
    const tierName = lang === "ms" ? data.reliability.grade_ms : (lang === "en" ? data.reliability.grade_en : data.reliability.grade_ar);
    const rumuzHtml = (data.books && data.books.rumuz)
      ? data.books.rumuz.map(r => `<span class="rumuz-tag">${r}</span>`).join(" ")
      : "";

    const deathText = data.death && data.death.ah
      ? `${data.death.ah} H / ${data.death.ce || "-"} M`
      : "Tidak direkod";

    const teachersCount = data.teachers ? data.teachers.length : 0;
    const studentsCount = data.students ? data.students.length : 0;

    content.innerHTML = `
      <div class="rawi-card-header">
        <div class="rawi-title-group">
          <span class="rawi-badge tier-${tier}">
            <span class="badge-icon"></span>
            ${tierName}
          </span>
          <h2 id="rawiModalTitle" class="rawi-modal-arabic" dir="rtl">${data.name_ar}</h2>
          <p class="rawi-modal-latin">${data.name_ms || data.name_en} ${data.kunya ? `(${data.kunya})` : ""}</p>
        </div>
        <div class="rawi-rumuz-row">${rumuzHtml}</div>
      </div>

      <div class="rawi-meta-grid">
        <div class="meta-item">
          <span class="meta-label">Tabaqah (Generasi):</span>
          <span class="meta-val">${data.generation.name_ms}</span>
        </div>
        <div class="meta-item">
          <span class="meta-label">Tahun Wafat:</span>
          <span class="meta-val">${deathText}</span>
        </div>
        <div class="meta-item">
          <span class="meta-label">Tempat Tinggal:</span>
          <span class="meta-val">${(data.places_of_stay || []).join(", ") || "-"}</span>
        </div>
        <div class="meta-item">
          <span class="meta-label">Rangkaian:</span>
          <span class="meta-val">${teachersCount} Guru / ${studentsCount} Murid</span>
        </div>
      </div>

      ${data.reliability.summary_notes_ms ? `
        <div class="rawi-summary-quote">
          <p>${data.reliability.summary_notes_ms}</p>
        </div>
      ` : ""}

      <div class="rawi-modal-actions">
        <a href="./rawi/${data.id}/?lang=${lang}" class="btn-primary" style="display:inline-block; text-decoration:none;">
          Lihat Profil Lengkap & Jarh wa Ta'dil ↗
        </a>
      </div>
    `;
  }
}
