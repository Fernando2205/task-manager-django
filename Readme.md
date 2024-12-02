# Task Manager

## Descripción

Task Manager es una aplicación diseñada para ayudarte a organizar y gestionar tus tareas diarias de manera eficiente. Con esta herramienta, puedes crear, editar y dar seguimiento a tus tareas, mejorando tu productividad y asegurándote de que nada importante se quede sin hacer. La aplicación es completamente responsive, adaptándose a cualquier dispositivo, y cuenta con un sistema de notificaciones y modo oscuro para una mejor experiencia de usuario.

## Características

- **Crear Tareas**: Añade nuevas tareas con título, descripción y fecha de vencimiento.
- **Editar Tareas**: Modifica los detalles de tus tareas existentes.
- **Marcar como Completadas**: Señala las tareas que has finalizado.
- **Eliminar Tareas**: Remueve tareas que ya no necesitas.
- **Lista de Tareas**: Visualiza tus tareas pendientes y completadas.
- **Filtrar Tareas**: Organiza tus tareas por estado.
- **Vista de Calendario**: Observa tus tareas en un calendario interactivo.
- **Sistema de Notificaciones**: Recibe alertas sobre tus tareas.
- **Modo Oscuro**: Alterna entre modo claro y oscuro según tu preferencia.
- **Diseño Responsive**: Adaptable a dispositivos móviles, tabletas y escritorios.
- **Interfaz Intuitiva y Moderna**: Fácil de usar con un diseño atractivo.
- **Ordenamiento por Fecha**: Organiza tus tareas por fecha de vencimiento.

## Tecnologías

- **Backend**: Django
- **Frontend**: Tailwind CSS, JavaScript
- **Base de Datos**: SQLite
- **Iconos**: Box Icons

## Instalación

### Prerrequisitos

- Python 3.x
- pip
- Git

### Pasos

1. **Clonar el Repositorio**

    ```bash
    git clone https://github.com/Fernando2205/task-manager-django.git
    ```

2. **Entrar al Directorio del Proyecto**

    ```bash
    cd task-manager
    ```

3. **Crear un Entorno Virtual y Activarlo**

    ```bash
    python -m venv venv
    venv\Scripts\activate  # En Windows
    source venv/bin/activate  # En macOS/Linux
    ```

4. **Instalar las Dependencias**

    ```bash
    pip install -r requirements.txt
    ```

5. **Aplicar Migraciones de la Base de Datos**

    ```bash
    python manage.py migrate
    ```

6. **Ejecutar el Servidor de Desarrollo**

    ```bash
    python manage.py runserver
    ```

7. **Acceder a la Aplicación**

    Abre tu navegador y visita `http://127.0.0.1:8000/`

## Uso

- **Crear una Nueva Tarea**: Haz clic en el botón "New Task" y completa los campos requeridos.
- **Editar una Tarea**: Selecciona una tarea y haz clic en el icono de edición.
- **Marcar como Completada**: Haz clic en el icono de la palomita para marcar una tarea como completada.
- **Eliminar una Tarea**: Haz clic en el icono de la basura para eliminar una tarea.
- **Filtrar Tareas**: Utiliza los filtros de navegación para ver tareas según su estado o fecha.
- **Vista de Calendario**: Navega por tu calendario para ver las tareas programadas.
- **Notificaciones**: Observa las notificaciones en la esquina superior derecha para estar al tanto de tus tareas.

## Desarrollador

**Delio Palacios** - Estudiante de Ingeniería de Sistemas  
Universidad de San Buenaventura Cali

## Contacto

**Delio Palacios** - [deliopalaciosviafara@gmail.com](mailto:deliopalaciosviafara@gmail.com)
