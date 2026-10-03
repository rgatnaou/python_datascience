import time
from datetime import datetime

t = time.time()

print(f"Seconds since January 1, 1970: {t:,.4f} or {t:.2e} in scientific notation")

print(datetime.now().strftime("%b %d %Y"))