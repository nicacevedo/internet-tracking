#%%
# !pip3 install speedtest-cli
from speedtest import Speedtest
from time import sleep
from datetime import datetime
import pandas as pd

s = Speedtest()
output = [['time', 'downspeed', 'upspeed']]
while True:
    try:
        time_now = datetime.now().strftime("%H:%M:%S")
        downspeed = round((round(s.download()) / 1048576), 2)
        upspeed = round((round(s.upload()) / 1048576), 2)
        output.append([time_now, downspeed, upspeed])
        print(f"time: {time_now}, downspeed: {downspeed} Mb/s, upspeed: {upspeed} Mb/s")
        pd.DataFrame(output[1:], columns=output[0]).to_csv('speedtest.csv', index=False)
        # 60 seconds sleep
        sleep(60)
    except Exception as e:
        print(e)
    





# %%
