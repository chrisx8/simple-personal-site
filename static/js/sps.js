var burger=document.querySelector(".burger");
var target=document.querySelector("#"+burger.dataset.target);
burger.addEventListener("click", function() {
    burger.classList.toggle("is-active"), target.classList.toggle("is-active")
});
