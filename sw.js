/**
 * Maktabah Maftoohah — Service Worker (Offline-First)
 * Repo: rijal-al-hadith
 */

const CACHE_NAME = "rijal-al-hadith-v1";
const STATIC_ASSETS = [
  "./",
  "./index.html",
  "./css/main.css",
  "./css/badges.css",
  "./js/app.js",
  "./js/search.js",
  "./js/modal.js",
  "./data/index.json",
  "./manifest.webmanifest"
];

self.addEventListener("install", (e) => {
  e.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      return cache.addAll(STATIC_ASSETS);
    })
  );
  self.skipWaiting();
});

self.addEventListener("activate", (e) => {
  e.waitUntil(
    caches.keys().then((keys) => {
      return Promise.all(
        keys.filter((key) => key !== CACHE_NAME).map((key) => caches.delete(key))
      );
    })
  );
  self.clients.claim();
});

self.addEventListener("fetch", (e) => {
  if (e.request.method !== "GET") return;

  e.respondWith(
    caches.match(e.request).then((cached) => {
      if (cached) return cached;
      return fetch(e.request).then((res) => {
        if (!res || res.status !== 200 || res.type !== "basic") {
          return res;
        }
        const cloned = res.clone();
        caches.open(CACHE_NAME).then((cache) => {
          cache.put(e.request, cloned);
        });
        return res;
      }).catch(() => {
        // Return index.html as fallback for navigations
        if (e.request.mode === "navigate") {
          return caches.match("./index.html");
        }
      });
    })
  );
});
