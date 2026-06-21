/* WoAIS1 theme toggle (Bootstrap 5.3 data-bs-theme).
 * Initial resolution order: localStorage -> prefers-color-scheme -> "light".
 * Sets the theme as early as possible (script runs in <head>) to avoid a flash.
 */
(function () {
  var STORAGE_KEY = "woais1-theme";

  function resolveInitial() {
    try {
      var stored = localStorage.getItem(STORAGE_KEY);
      if (stored === "light" || stored === "dark") return stored;
    } catch (e) { /* localStorage may be blocked */ }
    if (window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches) {
      return "dark";
    }
    return "light";
  }

  function applyTheme(theme) {
    document.documentElement.setAttribute("data-bs-theme", theme);
  }

  applyTheme(resolveInitial());

  function syncButton(btn) {
    if (!btn) return;
    var current = document.documentElement.getAttribute("data-bs-theme") || "light";
    btn.setAttribute("aria-label",
      current === "dark" ? "Switch to light mode" : "Switch to dark mode");
    btn.innerHTML = current === "dark"
      ? '<i class="fas fa-sun"></i>'
      : '<i class="fas fa-moon"></i>';
  }

  function onReady() {
    var btn = document.getElementById("theme-toggle");
    syncButton(btn);
    if (!btn) return;
    btn.addEventListener("click", function () {
      var current = document.documentElement.getAttribute("data-bs-theme") || "light";
      var next = current === "dark" ? "light" : "dark";
      applyTheme(next);
      try { localStorage.setItem(STORAGE_KEY, next); } catch (e) { /* ignore */ }
      syncButton(btn);
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", onReady);
  } else {
    onReady();
  }
})();
