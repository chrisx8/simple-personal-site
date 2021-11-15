// hamburger nav menu on mobile
var burger = document.querySelector(".burger");
var target = document.querySelector("#"+burger.dataset.target);
burger.addEventListener("click", function() {
    burger.classList.toggle("is-active"), target.classList.toggle("is-active");
});

// toggle dark mode based on browser color scheme
const darkMode = window.matchMedia("(prefers-color-scheme: dark)").matches;
var hCaptcha = document.getElementById("h-captcha");
if (hCaptcha != null && darkMode) {
    hCaptcha.setAttribute("data-theme","dark");
}

// toggle color of current page button based on browser color scheme
var currentPagerBtn = document.getElementById("current-pager-btn");
if (currentPagerBtn != null && darkMode) {
    currentPagerBtn.classList.remove('is-dark');
    currentPagerBtn.classList.add('is-light');
}
