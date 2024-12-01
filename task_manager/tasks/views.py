from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import views as auth_views, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse

from .forms import CustomAuthenticationForm, CustomUserCreationForm

from .models import Task, Notification

# Create your views here.


def landing(request):
    return render(request, 'landing.html')


@login_required
def home(request):
    tasks = Task.objects.filter(user=request.user)
    filter_status = request.GET.get('status', 'all')
    sort_by = request.GET.get('sort')

    if filter_status == 'completed':
        tasks = tasks.filter(completed=True)
    elif filter_status == 'pending':
        tasks = tasks.filter(completed=False)

    if sort_by == 'desc':
        tasks = tasks.order_by('-due_date', '-due_time')
    else:
        tasks = tasks.order_by('due_date', 'due_time')  # Default ordering

    context = {
        'tasks': tasks,
        'total_tasks': Task.objects.filter(user=request.user).count(),
        'completed_tasks': Task.objects.filter(user=request.user, completed=True).count(),
        'pending_tasks': Task.objects.filter(user=request.user, completed=False).count(),
        'active_filter': filter_status,
        'sort_by': sort_by,
        'notifications': Notification.objects.filter(user=request.user).order_by('-created_at')[:5],
        'unread_notifications_count': Notification.objects.filter(user=request.user, is_read=False).count()
    }
    return render(request, 'index.html', context)


@login_required
def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        due_time = request.POST.get('due_time')
        origin_url = request.POST.get('origin_url')
        completed = False

        if title and due_date and due_time:
            task = Task(
                title=title,
                description=description,
                due_date=due_date,
                due_time=due_time,
                completed=completed,
                user=request.user
            )
            task.save()

            # Create notification
            create_notification(
                request.user,
                'task_created',
                'New Task Created',
                f'You created a new task: {title}'
            )

            if origin_url and origin_url.startswith(request.build_absolute_uri('/')[:-1]):
                return redirect(origin_url)
            return redirect('home')

    context = {
        'origin_url': request.META.get('HTTP_REFERER')
    }
    return render(request, 'add_task.html', context)


@login_required
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id, user=request.user)
    return render(request, 'delete.html', {'task': task})


@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        due_time = request.POST.get('due_time')

        if title and due_date and due_time:
            task.title = title
            task.description = description
            task.due_date = due_date
            task.due_time = due_time
            task.save()

            # Create notification for edit
            create_notification(
                request.user,
                'task_edited',
                'Task Updated',
                f'Task "{title}" was updated'
            )

            return redirect('home')

    context = {
        'task': task,
        'notifications': Notification.objects.filter(user=request.user).order_by('-created_at')[:5],
        'unread_notifications_count': Notification.objects.filter(user=request.user, is_read=False).count()
    }
    return render(request, 'edit_task.html', context)


@login_required
def view_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    context = {
        'task': task,
        'notifications': Notification.objects.filter(user=request.user).order_by('-created_at')[:5],
        'unread_notifications_count': Notification.objects.filter(user=request.user, is_read=False).count()
    }
    return render(request, 'view_task.html', context)


@login_required
def toggle_complete(request, task_id):
    task = Task.objects.get(id=task_id, user=request.user)
    if task:
        task.completed = not task.completed
        task.save()
        return redirect(request.META.get('HTTP_REFERER'))


@login_required
def remove_task(request, task_id):
    task = Task.objects.get(id=task_id, user=request.user)
    if task:
        title = task.title
        task.delete()

        # Create notification
        create_notification(
            request.user,
            'task_deleted',
            'Task Deleted',
            f'Task "{title}" was deleted'
        )

        return redirect('home')


@login_required
def mark_notification_read(request, notification_id):
    notification = get_object_or_404(
        Notification, id=notification_id, user=request.user)
    notification.is_read = True
    notification.save()
    return JsonResponse({'status': 'success'})


@login_required
def mark_all_notifications_read(request):
    request.user.notification_set.filter(is_read=False).update(is_read=True)
    return JsonResponse({'status': 'success'})


@login_required
def calendar_view(request):
    tasks = Task.objects.filter(
        user=request.user).order_by('due_date', 'due_time')
    return render(request, 'calendar_view.html', {'tasks': tasks})


@login_required
def delete_notification(request, notification_id):
    notification = get_object_or_404(
        Notification, id=notification_id, user=request.user)
    notification.delete()
    return JsonResponse({'status': 'success'})


@login_required
def delete_all_notifications(request):
    Notification.objects.filter(user=request.user).delete()
    return JsonResponse({'status': 'success'})


def create_notification(user, type, title, message):
    Notification.objects.create(
        user=user,
        notification_type=type,
        title=title,
        message=message
    )


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(
                request, 'Your account has been created successfully!')
            return redirect('login')

    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


class LoginView(auth_views.LoginView):
    template_name = 'registration/login.html'
    form_class = CustomAuthenticationForm

    def form_valid(self, form):
        messages.success(self.request, 'You have logged in successfully!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.warning(
            self.request, 'Invalid username or password. Please try again.')
        return super().form_invalid(form)

    def dispatch(self, request, *args, **kwargs):
        if 'next' in request.GET:
            messages.info(
                request, 'You need to be logged in to access this page.')
        return super().dispatch(request, *args, **kwargs)


def custom_logout(request):
    logout(request)
    messages.info(request, 'You have been logged out successfully!')
    return redirect('login')
