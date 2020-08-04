import time

start_time = time.time()
while True:
    try:
        while True:
            print(round(time.time() - start_time, 2))
            time.sleep(0.1)
    except KeyboardInterrupt:
        end_time = time.time()
        print(f'time recorded : {round(end_time-start_time,2)} seconds')
        break
