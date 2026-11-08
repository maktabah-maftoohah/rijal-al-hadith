/**
 * Maktabah Maftoohah — Smart Arabic Search & Normalizer
 * Repo: rijal-al-hadith
 * Standard: Zero-Build Vanilla ES6
 */

/**
 * Strips diacritics, standardizes Alef, Taa Marbutah, and common patronymics.
 * @param {string} text
 * @returns {string} Normalized searchable string
 */
export function normalizeArabic(text) {
  if (!text) return "";
  return text
    // Strip Tashkeel & Harakat (fathah, dammah, kasrah, sukun, shaddah, tanween)
    .replace(/[\u064B-\u065F\u0670]/g, "")
    // Standardize Alef variations (أ, إ, آ -> ا)
    .replace(/[إأآ]/g, "ا")
    // Standardize Taa Marbutah to Haa (ة -> ه)
    .replace(/ة/g, "ه")
    // Standardize Alef Maqsurah to Yaa (ى -> ي)
    .replace(/ى/g, "ي")
    // Normalize patronymic Ibn / Bin (ابن / بن -> بن)
    .replace(/\bبن\b|\bابن\b/g, "بن")
    // Normalize Abu (أبو / ابو -> ابو)
    .replace(/\bأبو\b|\bابو\b/g, "ابو")
    .trim()
    .toLowerCase();
}

/**
 * Filter an array of narrators based on query and faceted criteria.
 * @param {Array} narrators Full or index list
 * @param {Object} criteria { query, tier, tabaqah, ramz }
 * @returns {Array} Filtered narrators
 */
export function filterNarrators(narrators, { query = "", tier = null, tabaqah = null, ramz = null } = {}) {
  const normQuery = normalizeArabic(query);
  const romanQuery = query.trim().toLowerCase();

  return narrators.filter(item => {
    // 1. Reliability Tier Filter
    if (tier !== null && tier !== "" && item.reliability.level !== parseInt(tier, 10)) {
      return false;
    }

    // 2. Tabaqah Filter
    if (tabaqah && item.generation && item.generation.code !== tabaqah) {
      return false;
    }

    // 3. Rumuz al-Kutub Filter
    if (ramz && item.books && item.books.rumuz) {
      if (!item.books.rumuz.includes(ramz)) {
        return false;
      }
    }

    // 4. Text Query Filter
    if (!normQuery && !romanQuery) {
      return true;
    }

    const normNameAr = normalizeArabic(item.name_ar || "");
    const normKunya = normalizeArabic(item.kunya || "");
    const normLaqab = normalizeArabic(item.laqab || "");
    const nameEn = (item.name_en || "").toLowerCase();
    const nameMs = (item.name_ms || "").toLowerCase();
    const idStr = String(item.id);

    return (
      normNameAr.includes(normQuery) ||
      normKunya.includes(normQuery) ||
      normLaqab.includes(normQuery) ||
      nameEn.includes(romanQuery) ||
      nameMs.includes(romanQuery) ||
      idStr === romanQuery
    );
  });
}
