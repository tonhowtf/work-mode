import psutil
from pprint import pprint as pp


for proc in psutil.process_iter(['pid', 'name']):
    if(proc.info['name'] == "Telegram"):
        p = psutil.Process(proc.info['pid'])
        pp(f"{proc.info['name']} terminated at PID: {proc.info['pid']}")
        p.terminate()
        p.wait()

