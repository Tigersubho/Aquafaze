
 const preloader = document.querySelector('.preloader');

const fadeEffect = setInterval(() => {
  if (!preloader.style.opacity) {
    preloader.style.opacity = 1.25;
  }
  if (preloader.style.opacity > 0) {
    preloader.style.opacity -= 0.2;
  } else {
    clearInterval(fadeEffect);
    preloader.style.display="none";
  }
}, 300);
window.addEventListener('load', fadeEffect);

