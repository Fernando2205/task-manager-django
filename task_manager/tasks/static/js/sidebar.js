// Update sidebar.js
document.addEventListener('DOMContentLoaded', function () {
    const sidebar = document.getElementById('sidebar');
    const main = document.getElementById('main');
    const openBtn = document.getElementById('sidebarToggle');
    const closeBtn = document.getElementById('sidebarCloseBtn');

    // Add CSS to prevent initial animation
    const style = document.createElement('style');
    style.textContent = `
        .no-animation { transition: none !important; }
        @keyframes enableTransition {
            from { transition: none; }
            to { transition: transform 300ms ease-in-out; }
        }
    `;
    document.head.appendChild(style);

    function setSidebarState(isOpen, animate = true) {
        if (!animate) {
            sidebar.classList.add('no-animation');
            main.classList.add('no-animation');
        }

        if (isOpen) {
            sidebar.classList.remove('-translate-x-full');
            main.classList.add('sm:ml-64');
            main.classList.remove('ml-0');
        } else {
            sidebar.classList.add('-translate-x-full');
            main.classList.remove('sm:ml-64');
            main.classList.add('ml-0');
        }

        if (!animate) {
            // Force reflow
            sidebar.offsetHeight;
            main.offsetHeight;

            // Remove no-animation class after initial state is set
            requestAnimationFrame(() => {
                sidebar.classList.remove('no-animation');
                main.classList.remove('no-animation');
            });
        }

        localStorage.setItem('sidebarOpen', isOpen);
    }

    // Initialize sidebar state without animation
    const isSidebarOpen = localStorage.getItem('sidebarOpen') === 'true';
    setSidebarState(isSidebarOpen, false);

    function toggleSidebar() {
        const isCurrentlyOpen = !sidebar.classList.contains('-translate-x-full');
        setSidebarState(!isCurrentlyOpen, true);
    }

    openBtn.addEventListener('click', toggleSidebar);
    closeBtn.addEventListener('click', toggleSidebar);

    // Close sidebar on mobile when clicking outside
    document.addEventListener('click', function (e) {
        const isSidebarOpen = !sidebar.classList.contains('-translate-x-full');
        if (isSidebarOpen &&
            !sidebar.contains(e.target) &&
            !openBtn.contains(e.target)) {
            setSidebarState(false, true);
        }
    });
});