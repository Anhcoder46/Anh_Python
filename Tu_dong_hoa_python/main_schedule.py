import schedule
import time

def job(name):
    print("Thực hiện công việc", name)
    print("___________________")
    
#schedule.every(2).minutes.do(job)
#schedule.every().hour.do(job)
schedule.every().day.at("14:30").do(job, name = "22ct4")

while True:
    schedule.run_pending()
    time.sleep(1)