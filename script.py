import argparse
import psutil
import time
from rich import print
from alive_progress import alive_it

victim = ['Telegram', 'Discord']


def kill_process():
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] in victim:
            try:
                proc.terminate()
                proc.wait()
                print(f"{proc.info['name']} terminated at PID: {proc.info['pid']} [bold magenta]")
            except psutil.NoSuchProcess:
                continue
            except psutil.AcessDenied:
                print(f"[bold red]Access Denied para {proc.info['name']} Run as sudo")


def work_mode(hours: float):
        total_timer = int(hours * 3600)
        print(f"Iniciando timer de [bold green]{hours} hora(s)")
        for i in alive_it(range(1, total_timer+1)):
            time.sleep(1)
            kill_process()

parser = argparse.ArgumentParser(
                    prog='workmode',
                    description='block aplications during work',
                    epilog='')




