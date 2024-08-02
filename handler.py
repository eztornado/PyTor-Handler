import schedule
import time
import subprocess
from datetime import datetime
import threading


class CommandHandler:
    def __init__(self):
        self.jobs = []

    def everyMinute(self, func, *args):
        job = schedule.every(1).minute.do(self._run_in_thread, func, *args)
        self.jobs.append(job)

    def everyFiveMinutes(self, func, *args):
        job = schedule.every(5).minutes.do(self._run_in_thread, func, *args)
        self.jobs.append(job)

    def everyHour(self, func, *args):
        job = schedule.every(1).hour.do(self._run_in_thread, func, *args)
        self.jobs.append(job)

    def at(self, time_str, func, *args):
        job = schedule.every().day.at(time_str).do(self._run_in_thread, func, *args)
        self.jobs.append(job)

    def _run_in_thread(self, func, *args):
        job_thread = threading.Thread(target=func, args=args)
        job_thread.start()

    def run_pending(self):
        while True:
            schedule.run_pending()
            time.sleep(60)


def call(program, script, args):
    subprocess.run([program, script] + list(args))


if __name__ == "__main__":
    handler = CommandHandler()

    #Execution Examples
    # Define tasks
    #handler.everyMinute(call, 'python', 'program.py', ['arg1', 'arg2'])
    #handler.everyFiveMinutes(call, 'python', 'another_program.py', ['arg1'])
    #handler.everyHour(call, 'python', 'hourly_program.py', [])
    #handler.at("12:00", call, 'python', 'noon_program.py', ['arg1', 'arg2'])
    # Execute a bash script every hour
    #handler.everyHour(call, 'bash', 'script.sh', ['arg1'])

    # Start the handler
    handler.run_pending()
