/**
 * Maktabah Maftoohah — Rijal al-Hadith Main Application
 * Modern Zero-Build Vanilla ES6 Module Architecture
 * Repo: rijal-al-hadith
 */

import { filterNarrators, normalizeArabic } from "./search.js";
import { RawiModal } from "./modal.js";

class RijalApp {
  constructor() {
    this.narratorsIndex = [];
    this.modal = new RawiModal("./data/narrators/");
    this.currentCriteria = {
      query: "",
      tier: "",
      tabaqah: "",
      ramz: null
    };
    this.currentLang = localStorage.getItem("lang") || "ms";
  }

  async init() {
    this._initTheme();
    this._bindEvents();
    await this._loadIndex();
    this._render();
    this._checkURLParams();
  }

  _initTheme() {
    const savedTheme = localStorage.getItem("theme") || "light";
    document.documentElement.setAttribute("data-theme", savedTheme);

    const btn = document.getElementById("themeToggle");
    if (btn) {
      btn.addEventListener("click", () => {
        const cur = document.documentElement.getAttribute("data-theme");
        const next = cur === "dark" ? "light" : "dark";
        document.documentElement.setAttribute("data-theme", next);
        localStorage.setItem("theme", next);
        btn.textContent = next === "dark" ? "☀️" : "🌙";
      });
      btn.textContent = savedTheme === "dark" ? "☀️" : "🌙";
    }
  }

  _bindEvents() {
    const searchInput = document.getElementById("searchInput");
    const tierFilter = document.getElementById("tierFilter");
    const tabaqahFilter = document.getElementById("tabaqahFilter");
    const rumuzButtons = document.querySelectorAll(".rumuz-btn");

    if (searchInput) {
      searchInput.addEventListener("input", (e) => {
        this.currentCriteria.query = e.target.value;
        this._render();
      });
    }

    if (tierFilter) {
      tierFilter.addEventListener("change", (e) => {
        this.currentCriteria.tier = e.target.value;
        this._render();
      });
    }

    if (tabaqahFilter) {
      tabaqahFilter.addEventListener("change", (e) => {
        this.currentCriteria.tabaqah = e.target.value;
        this._render();
      });
    }

    rumuzButtons.forEach(btn => {
      btn.addEventListener("click", () => {
        const val = btn.getAttribute("data-ramz");
        if (this.currentCriteria.ramz === val) {
          this.currentCriteria.ramz = null;
          btn.classList.remove("active");
        } else {
          rumuzButtons.forEach(b => b.classList.remove("active"));
          this.currentCriteria.ramz = val;
          btn.classList.add("active");
        }
        this._render();
      });
    });

    const langBtn = document.getElementById("langToggle");
    if (langBtn) {
      langBtn.addEventListener("click", () => {
        this.currentLang = this.currentLang === "ms" ? "en" : "ms";
        localStorage.setItem("lang", this.currentLang);
        langBtn.textContent = this.currentLang.toUpperCase();
        this._render();
      });
      langBtn.textContent = this.currentLang.toUpperCase();
    }
  }

  async _loadIndex() {
    const container = document.getElementById("contentView");
    try {
      const res = await fetch("./data/index.json");
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      this.narratorsIndex = await res.json();
    } catch (err) {
      if (container) {
        container.innerHTML = `
          <div class="rawi-error">
            <p>Gagal memuatkan pangkalan data perawi.</p>
            <small>${err.message}</small>
          </div>
        `;
      }
    }
  }

  _render() {
    const container = document.getElementById("contentView");
    const statsEl = document.getElementById("resultsStats");
    if (!container) return;

    const filtered = filterNarrators(this.narratorsIndex, this.currentCriteria);

    if (statsEl) {
      const label = this.currentLang === "en" ? "narrators found" : "perawi ditemui";
      statsEl.textContent = `${filtered.length} ${label} (daripada ${this.narratorsIndex.length} rekod)`;
    }

    if (filtered.length === 0) {
      container.innerHTML = `
        <div style="text-align:center; padding: 3rem 1rem; color: var(--text-muted);">
          <p style="font-size: 1.15rem; margin-bottom: 0.5rem;">Tiada perawi sepadan dengan carian.</p>
          <small>Cuba gunakan kata kunci yang berbeza atau kosongkan tapisan.</small>
        </div>
      `;
      return;
    }

    const cardsHtml = filtered.map(item => this._renderCard(item)).join("");
    container.innerHTML = `<div class="narrator-grid">${cardsHtml}</div>`;

    // Attach quick-peek clicks
    container.querySelectorAll(".btn-card-peek").forEach(btn => {
      btn.addEventListener("click", () => {
        const id = parseInt(btn.getAttribute("data-id"), 10);
        this.modal.open(id, this.currentLang);
      });
    });
  }

  _renderCard(item) {
    const tier = item.reliability.level;
    const tierName = this.currentLang === "en" ? (item.reliability.grade_en || item.reliability.grade_ms) : item.reliability.grade_ms;
    const genName = this.currentLang === "en" ? (item.generation.name_en || item.generation.name_ms) : item.generation.name_ms;
    const latinName = this.currentLang === "en" ? (item.name_en || item.name_ms) : (item.name_ms || item.name_en);

    const rumuzTags = (item.books && item.books.rumuz)
      ? item.books.rumuz.map(r => `<span class="rumuz-tag">${r}</span>`).join(" ")
      : "";

    return `
      <div class="narrator-card" data-id="${item.id}">
        <div>
          <div class="card-top">
            <span class="rawi-badge tier-${tier}">
              <span class="badge-icon"></span>
              ${tierName}
            </span>
            <div class="card-rumuz">${rumuzTags}</div>
          </div>
          <h3 class="card-arabic-name" dir="rtl">${item.name_ar}</h3>
          <p class="card-latin-name">${latinName} ${item.kunya ? `(${item.kunya})` : ""}</p>
          <div class="card-meta-list">
            <div><strong>Tabaqah:</strong> ${genName}</div>
            <div><strong>ID Kanonikal:</strong> #${item.id}</div>
          </div>
        </div>
        <div class="card-actions">
          <button class="btn-card-peek" data-id="${item.id}">Imbasan Pantas 👁️</button>
          <a href="./rawi/${item.id}/?lang=${this.currentLang}" class="btn-card-full">Profil Penuh ↗</a>
        </div>
      </div>
    `;
  }

  _checkURLParams() {
    const params = new URLSearchParams(window.location.search);
    const peekId = params.get("peek") || params.get("id");
    if (peekId) {
      const id = parseInt(peekId, 10);
      if (!isNaN(id)) {
        this.modal.open(id, this.currentLang);
      }
    }
  }
}

// Bootstrap
document.addEventListener("DOMContentLoaded", () => {
  const app = new RijalApp();
  app.init();
});
