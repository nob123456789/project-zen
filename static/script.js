const ham = document.getElementById("hamburger");
const menu = document.getElementById("h-menu");

ham.addEventListener("click", function (e) {
  if (menu.style.display == "none"){
      menu.style.display = "block";
      menu.classList.add('menu_active');
  }
  else{
    menu.style.display = "none";
    menu.classList.remove('menu_active');
  }
})