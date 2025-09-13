document.addEventListener("DOMContentLoaded", () => {
  const toggle = document.getElementById("theme-toggle");
  if (!toggle) return;

  toggle.addEventListener("click", () => {
    const html = document.documentElement;
    const current = html.getAttribute("data-bs-theme");
    const next = current === "dark" ? "light" : "dark";
    html.setAttribute("data-bs-theme", next);
    localStorage.setItem("theme", next);
    toggle.textContent = next === "dark" ? "🌙" : "☀️";
  });

  // persist user choice
  const saved = localStorage.getItem("theme");
  if (saved) {
    document.documentElement.setAttribute("data-bs-theme", saved);
    toggle.textContent = saved === "dark" ? "🌙" : "☀️";
  }
});
