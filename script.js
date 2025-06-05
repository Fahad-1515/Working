const hamburger = document.getElementById("hamburger");
const navLinks = document.getElementById("nav-links");
const themeToggle = document.getElementById("theme-toggle");
const navbar = document.getElementById("navbar");
const body = document.body;

// Hamburger toggle
hamburger.addEventListener("click", () => {
  navLinks.classList.toggle("active");
  hamburger.classList.toggle("active");
});

navLinks.querySelectorAll("a").forEach((link) => {
  link.addEventListener("click", () => {
    if (navLinks.classList.contains("active")) {
      navLinks.classList.remove("active");
      hamburger.classList.remove("active");
    }
  });
});

// Theme toggle function
function setTheme(theme) {
  if (theme === "light") {
    body.classList.remove("dark");
    body.classList.add("light");
    navbar.classList.remove("dark");
    navbar.classList.add("light");
    themeToggle.textContent = "☀️";
  } else {
    body.classList.remove("light");
    body.classList.add("dark");
    navbar.classList.remove("light");
    navbar.classList.add("dark");
    themeToggle.textContent = "🌙";
  }
  localStorage.setItem("theme", theme);
}

// Load saved theme or default to dark
const savedTheme = localStorage.getItem("theme") || "dark";
setTheme(savedTheme);

// Toggle theme on click
themeToggle.addEventListener("click", () => {
  const currentTheme = body.classList.contains("dark") ? "dark" : "light";
  setTheme(currentTheme === "dark" ? "light" : "dark");
});

const cursor = document.getElementById("custom-cursor");
window.addEventListener("mousemove", (e) => {
  cursor.style.left = e.clientX + "px";
  cursor.style.top = e.clientY + "px";
});
