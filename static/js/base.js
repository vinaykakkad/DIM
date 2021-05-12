document.addEventListener('DOMContentLoaded', () => {

    navbar = document.querySelector('.nav-class');

    document.addEventListener('scroll', () => {
        if (window.scrollY > 10) {
            navbar.classList.add('shadow');
        }
        else {
            navbar.classList.remove('shadow');
        }
    });
});