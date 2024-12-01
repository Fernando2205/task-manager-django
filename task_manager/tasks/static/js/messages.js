document.addEventListener('DOMContentLoaded', function () {
    var message = document.getElementById('message');
    if (message) {
        // Start with opacity 0
        message.style.opacity = '0';

        // Force reflow
        message.offsetHeight;

        // Fade in
        message.style.opacity = '1';

        // Fade out after delay
        setTimeout(function () {
            message.style.opacity = '0';
            setTimeout(function () {
                message.remove();
            }, 500);
        }, 3000);
    }
});