import schedule
import time
import subprocess
from datetime import datetime
import threading
import logging

# Configuración del logging
logging.basicConfig(
    filename='log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

class CommandHandler:
    def __init__(self):
        self.jobs = []

    def everyMinute(self, func, *args):
        job = schedule.every(1).minute.at(":00").do(self._run_in_thread, 'everyMinute', func, *args)
        self.jobs.append(job)

    def everyFiveMinutes(self, func, *args):
        job = schedule.every(5).minutes.at(":00").do(self._run_in_thread, 'everyFiveMinutes', func, *args)
        self.jobs.append(job)

    def everyHour(self, func, *args):
        job = schedule.every(1).hour.at(":00").do(self._run_in_thread, 'everyHour', func, *args)
        self.jobs.append(job)

    def at(self, time_str, func, *args):
        job = schedule.every().day.at(time_str).do(self._run_in_thread, f'at {time_str}', func, *args)
        self.jobs.append(job)

    def _run_in_thread(self, config, func, *args):
        job_thread = threading.Thread(target=self._run_and_log, args=(config, func) + args)
        job_thread.start()

    def _run_and_log(self, config, func, *args):
        start_time = datetime.now()
        func(*args)
        end_time = datetime.now()
        elapsed_time = (end_time - start_time).total_seconds()
        logging.info(
            f"Program: {args[0]}, Script: {args[1]}, Config: {config}, Arguments: {args[2:]}, Execution time: {elapsed_time} seconds")

    def run_pending(self):
        while True:
            schedule.run_pending()
            now = datetime.now()
            sleep_time = 60 - now.second
            time.sleep(sleep_time)


def call(program, script, args):
    subprocess.run([program, script] + list(args))


if __name__ == "__main__":
    handler = CommandHandler()
    logging.info(f"Handler started!")

    #Execution examples
    # Define tasks
    #handler.everyMinute(call, 'python', 'program.py', ['arg1', 'arg2'])
    #handler.everyFiveMinutes(call, 'python', 'another_program.py', ['arg1'])
    #handler.everyHour(call, 'python', 'hourly_program.py', [])
    #handler.at("12:00", call, 'python', 'noon_program.py', ['arg1', 'arg2'])
    # Execute a bash script every hour
    #handler.everyHour(call, 'bash', 'script.sh', ['arg1'])

    # Start the handler
    handler.run_pending()
