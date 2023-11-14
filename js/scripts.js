document.addEventListener("DOMContentLoaded", function() {
    const menuToggle = document.querySelector('.menu-toggle');
    const menu = document.querySelector('.navbar');

    menuToggle.addEventListener('click', function() {
        if (menu.style.display === 'flex') {
            menu.style.display = 'none';
            menuToggle.classList.remove('menu-open'); // Cerrar el menú
        } else {
            menu.style.display = 'flex';
            menuToggle.classList.add('menu-open'); // Abrir el menú
        }
    });
});
