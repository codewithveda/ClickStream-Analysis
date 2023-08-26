const header = document.querySelector ("header");
window. addEventListener ("scroll", function(){

     Header.classList.toggle("sticky", window.scrollY > 0);
});