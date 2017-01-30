#!/usr/bin/python
import time

# this script assumes it's run every minute during specific times of the day.
# example user crontab entry runs sct from from 0 to 10 minutes at 6PM daily
# and from 50 to 59 minutes at 5AM daily.
# 0-10 18 * * * env DISPLAY=:0 XAUTHORITY=$HOME/.Xauthority /usr/bin/sct $(/path/to/this.py)
# 50-59 5 * * * env DISPLAY=:0 XAUTHORITY=$HOME/.Xauthority /usr/bin/sct $(/path/to/this.py)

# configurable options

daytemp = 6500      # daytime color temp
nighttemp = 2000    # color temp to reach after evening
ttj = 10            # how many minutes will it take to reach target temp
evening = 1080      # number in minutes since midnight, time to start adjusting temp.
morning = 359       # number in minutes since midnight, temp will reach daytemp by that moment


t = time.localtime()
minutes_since_midnight = t.tm_hour * 60 + t.tm_min                # an integer from 0 to 1440
minutes_after_evening = max(0, minutes_since_midnight - evening)  # same as above
minutes_till_morning = max(0, morning - minutes_since_midnight)   # an integer from 0 to ttj
step = int((daytemp - nighttemp) / ttj)                           # temp delta

print(max(nighttemp, daytemp - max(minutes_after_evening, min(minutes_till_morning, ttj)) * step))
