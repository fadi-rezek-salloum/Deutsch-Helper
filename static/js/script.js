const navbar = document.getElementById("navbar");

const hero = document.querySelector(".hero__container");
const login = document.querySelector(".login__container");

if (hero) {
    hero.style.height = `calc(100dvh - ${navbar.offsetHeight}px)`;
}

if (login) {
    login.style.height = `calc(100dvh - ${navbar.offsetHeight}px)`;
}
