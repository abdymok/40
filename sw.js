const CACHE = 'abdymok-40-v20261025-1';

self.addEventListener('install', event => {
  self.skipWaiting();
});

self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(keys =>
      Promise.all(
        keys
          .filter(key => key.startsWith('abdymok-40-') && key !== CACHE)
          .map(key => caches.delete(key))
      )
    ).then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', event => {
  const request = event.request;
  if (request.method !== 'GET') return;

  const url = new URL(request.url);
  if (url.origin !== self.location.origin) return;

  // Never intercept media or byte-range requests. Safari needs the server's native
  // 206 Partial Content response for reliable MP4 playback and seeking.
  if (request.headers.has('range') || /\.(mp4|mov|m4a|webm|m4v)$/i.test(url.pathname)) return;

  event.respondWith(
    fetch(request, { cache: 'no-store' })
      .then(response => {
        if (response && response.status === 200) {
          const copy = response.clone();
          caches.open(CACHE).then(cache => cache.put(request, copy));
        }
        return response;
      })
      .catch(() => caches.match(request))
  );
});
