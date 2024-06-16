const hamburgerBtn = document.querySelector(".hamburger_btn");
const navbarMenu = document.querySelector(".navbar");
const hamburgerCloseBtn = document.querySelector(".hamburger_close_btn");

hamburgerBtn.addEventListener("click", () => {
  navbarMenu.classList.add("open");
});

hamburgerCloseBtn.addEventListener("click", () => {
  navbarMenu.classList.remove("open");
});
