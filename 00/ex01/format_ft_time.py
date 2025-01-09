import time
import datetime

print(f"Seconds since January 1, 1970: {time.time():,.4f} or "
      f"{time.time():.2e} in scientific notation")
print(datetime.datetime.now().strftime("%b %d %Y"))
