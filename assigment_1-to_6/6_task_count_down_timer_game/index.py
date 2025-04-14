import time
import sys

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f"\033[1;32m⏳ {mins:02d}:{secs:02d} \033[0m"
        sys.stdout.write("\r" + timer)
        sys.stdout.flush()
        time.sleep(1)
        seconds -= 1

    print("\n\033[1;31m🎉 Time's up! ⏰🎉\033[0m")

# Example: Countdown from 10 seconds
countdown_timer(10)