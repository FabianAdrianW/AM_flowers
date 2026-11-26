/* AM Flowers · otwarcie kurtyny po przejściu ze strony Kwiaciarni Małgorzata (?z=malgorzata).
   Ładowany w <head> bez defer, żeby kurtyna była od pierwszej klatki. Odtwarza się raz: parametr znika z adresu. */
(() => {
  try {
    const q = new URLSearchParams(location.search);
    if (q.get('z') !== 'malgorzata') return;
    q.delete('z');
    history.replaceState(history.state, '', location.pathname + (q.toString() ? '?' + q : '') + location.hash);
    if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    const root = document.documentElement;
    root.classList.add('arrive');
    const open = () => {
      setTimeout(() => root.classList.add('arrive-go'), 650);
      setTimeout(() => root.classList.remove('arrive', 'arrive-go'), 1800);
    };
    document.readyState === 'loading' ? document.addEventListener('DOMContentLoaded', open, { once: true }) : open();
  } catch (_) {}
})();
