import psutil
from rich import print

def kill_process():
    for proc in psutil.process_iter(['pid', 'name']):
        if(proc.info['name'] == "Telegram"):
            p = psutil.Process(proc.info['pid'])
            print(f"{proc.info['name']} terminated at PID: {proc.info['pid']}[bold magenta]")
            p.terminate()
            p.wait() 



