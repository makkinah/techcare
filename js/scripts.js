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

    // Añade un listener para cerrar el menú al hacer clic en un enlace en el modo móvil
    document.querySelectorAll('.navbar a').forEach(function(link) {
        link.addEventListener('click', function() {
            if (window.innerWidth <= 768) {
                menu.style.display = 'none';
                menuToggle.classList.remove('menu-open');
            }
        });
    });

    // Añade un listener para cerrar el menú al hacer clic fuera del menú en el modo móvil
    document.addEventListener('click', function(event) {
        if (window.innerWidth <= 768 && !menu.contains(event.target) && !menuToggle.contains(event.target)) {
            menu.style.display = 'none';
            menuToggle.classList.remove('menu-open');
        }
    });
});