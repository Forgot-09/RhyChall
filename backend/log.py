from datetime import datetime

now = datetime.now()
print(f"[{now.strftime('%H:%M:%S')}] 프로그램 시작! [{now.strftime('%Y/%m/%d')}]")

def log(content, level=0):
    now = datetime.now()
    if level == 0:
        level = "INFO"
    elif level == 1:
        level = "ERROR"
    elif level == 2:
        level = "WARN"
    print(f"[{now.strftime('%H:%M:%S')}] [{level}] {content}")