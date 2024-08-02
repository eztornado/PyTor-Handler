# PyTor - Handler

## Descripción en Español

PyTor Handler  es un script escrito en Python que actúa como un demonio para automatizar la ejecución de otros scripts o comandos en servidores Windows o Linux. Utiliza la biblioteca `schedule` para manejar la programación de tareas y `threading` para asegurar que las tareas se ejecuten en paralelo, evitando bloqueos del sistema. Este script es útil para programar tareas recurrentes como ejecutar scripts cada minuto, cada cinco minutos, cada hora, o a una hora específica del día.

### Características

- **Programación Flexible**: Permite programar tareas para que se ejecuten cada minuto, cada cinco minutos, cada hora o a una hora específica del día.
- **Ejecución Paralela**: Utiliza `threading` para ejecutar las tareas en paralelo, evitando bloqueos del sistema.
- **Compatibilidad**: Funciona tanto en servidores Windows como Linux.
- **Fácil Configuración**: Define las tareas a ejecutar de manera sencilla en el script principal.

### Instalación

1. Clona el repositorio:
    ```bash
    git clone https://github.com/eztornado/PyTor-Handler.git
    cd PyTor-Handler
    ```

2. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

### Uso

1. Define tus tareas en el archivo `handler.py`:
    ```python
    handler.everyMinute(call, 'python', 'program.py', ['arg1', 'arg2'])
    handler.everyFiveMinutes(call, 'python', 'another_program.py', ['arg1'])
    handler.everyHour(call, 'python', 'hourly_program.py', [])
    handler.at("12:00", call, 'python', 'noon_program.py', ['arg1', 'arg2'])
    handler.everyHour(call, 'bash', 'script.sh', ['arg1'])
    ```

2. Ejecuta el script:
    ```bash
    python handler.py
    ```

## English Description

PyTor Handler is a Python script that acts as a daemon to automate the execution of other scripts or commands on Windows or Linux servers. It uses the `schedule` library to handle task scheduling and `threading` to ensure tasks run in parallel, preventing system blockages. This script is useful for scheduling recurring tasks such as running scripts every minute, every five minutes, every hour, or at a specific time of day.

### Features

- **Flexible Scheduling**: Allows scheduling tasks to run every minute, every five minutes, every hour, or at a specific time of day.
- **Parallel Execution**: Uses `threading` to run tasks in parallel, avoiding system blockages.
- **Compatibility**: Works on both Windows and Linux servers.
- **Easy Configuration**: Easily define the tasks to be executed in the main script.

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/eztornado/PyTor-Handler.git
    cd PyTor-Handler
    ```

2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Usage

1. Define your tasks in the `handler.py` file:
    ```python
    handler.everyMinute(call, 'python', 'program.py', ['arg1', 'arg2'])
    handler.everyFiveMinutes(call, 'python', 'another_program.py', ['arg1'])
    handler.everyHour(call, 'python', 'hourly_program.py', [])
    handler.at("12:00", call, 'python', 'noon_program.py', ['arg1', 'arg2'])
    handler.everyHour(call, 'bash', 'script.sh', ['arg1'])
    ```

2. Run the script:
    ```bash
    python handler.py
    ```

## Contribución

Las contribuciones son bienvenidas. Siéntete libre de abrir un issue o enviar un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT. Para más detalles, consulta el archivo LICENSE.
