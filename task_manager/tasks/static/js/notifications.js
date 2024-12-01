document.addEventListener('DOMContentLoaded', function () {
    const notificationBtn = document.getElementById('notificationBtn');
    const notificationDropdown = document.getElementById('notificationDropdown');
    const deleteAllBtn = document.getElementById('deleteAllNotifications');
    const markAllReadBtn = document.getElementById('markAllRead');

    function updateUnreadCount() {
        const badge = notificationBtn.querySelector('span');
        if (badge) {
            const currentCount = parseInt(badge.textContent);
            if (currentCount > 1) {
                badge.textContent = currentCount - 1;
            } else {
                badge.remove();
            }
        }
    }

    function hideDropdown() {
        notificationDropdown.style.opacity = '0';
        notificationDropdown.style.transform = 'translateY(-10px)';
        setTimeout(() => {
            notificationDropdown.classList.add('hidden');
        }, 200);
    }

    // Toggle dropdown with animation
    notificationBtn.addEventListener('click', function (e) {
        e.stopPropagation();
        if (notificationDropdown.classList.contains('hidden')) {
            notificationDropdown.classList.remove('hidden');
            notificationDropdown.style.opacity = '0';
            notificationDropdown.style.transform = 'translateY(-10px)';

            requestAnimationFrame(() => {
                notificationDropdown.style.transition = 'opacity 200ms ease-out, transform 200ms ease-out';
                notificationDropdown.style.opacity = '1';
                notificationDropdown.style.transform = 'translateY(0)';
            });
        } else {
            hideDropdown();
        }
    });

    // Close dropdown when clicking outside
    document.addEventListener('click', function (e) {
        if (!notificationDropdown.contains(e.target) && !notificationBtn.contains(e.target)) {
            hideDropdown();
        }
    });

    // Mark notification as read
    document.querySelectorAll('.mark-read-btn').forEach(btn => {
        btn.addEventListener('click', async function () {
            const notificationId = this.dataset.id;
            const notificationItem = this.closest('.notification-item');

            try {
                const response = await fetch(`/api/notifications/${notificationId}/read/`, {
                    method: 'POST',
                    headers: {
                        'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
                    }
                });

                if (response.ok) {
                    notificationItem.classList.remove('bg-blue-50');
                    this.remove();
                    updateUnreadCount();
                }
            } catch (error) {
                console.error('Error marking notification as read:', error);
            }
        });
    });

    // Delete single notification
    document.querySelectorAll('.delete-notification-btn').forEach(btn => {
        btn.addEventListener('click', async function () {
            const notificationId = this.dataset.id;
            const notificationItem = this.closest('.notification-item');

            try {
                const response = await fetch(`/api/notifications/${notificationId}/delete/`, {
                    method: 'POST',
                    headers: {
                        'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
                    }
                });

                if (response.ok) {
                    notificationItem.remove();

                    if (!document.querySelector('.notification-item')) {
                        const noNotifications = document.createElement('div');
                        noNotifications.className = 'p-4 text-center text-gray-500 no-notifications';
                        noNotifications.textContent = 'No notifications';
                        notificationDropdown.querySelector('.max-h-96').appendChild(noNotifications);
                        deleteAllBtn?.remove();
                    }
                }
            } catch (error) {
                console.error('Error deleting notification:', error);
            }
        });
    });
    if (markAllReadBtn) {
        markAllReadBtn.addEventListener('click', async function () {
            try {
                const response = await fetch('/api/notifications/mark-all-read/', {
                    method: 'POST',
                    headers: {
                        'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
                    }
                });

                if (response.ok) {
                    document.querySelectorAll('.notification-item').forEach(item => {
                        item.classList.remove('bg-blue-50');
                        item.querySelector('.mark-read-btn')?.remove();
                    });
                    const badge = notificationBtn.querySelector('span');
                    if (badge) badge.remove();
                }
            } catch (error) {
                console.error('Error marking all notifications as read:', error);
            }
        });
    }
    // Delete all notifications
    if (deleteAllBtn) {
        deleteAllBtn.addEventListener('click', async function () {
            try {
                const response = await fetch('/api/notifications/delete-all/', {
                    method: 'POST',
                    headers: {
                        'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
                    }
                });

                if (response.ok) {
                    const notificationsContainer = notificationDropdown.querySelector('.max-h-96');
                    notificationsContainer.innerHTML = `
                        <div class="p-4 text-center text-gray-500 no-notifications">
                            No notifications
                        </div>
                    `;
                    const badge = notificationBtn.querySelector('span');
                    if (badge) badge.remove();
                    deleteAllBtn.remove();
                }
            } catch (error) {
                console.error('Error deleting all notifications:', error);
            }
        });
    }
});