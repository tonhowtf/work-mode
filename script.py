import psutil
import time
from rich import print
from alive_progress import alive_bar


def kill_process():
    for proc in psutil.process_iter(['pid', 'name']):
        if(proc.info['name'] == "Telegram"):
            p = psutil.Process(proc.info['pid'])
            print(f"{proc.info['name']} terminated at PID: {proc.info['pid']}[bold magenta]")
            p.terminate()
            p.wait() 

def work_mode(hours: float):
        total_timer = int(hours * 3600)
        print(f"Iniciando timer de [bold green]{time} hora(s)")
        with alive_bar(total_timer) as bar:
            for i in range(total_timer):
                time.sleep(1)
                kill_process()
                bar()

work_mode(0.01)




