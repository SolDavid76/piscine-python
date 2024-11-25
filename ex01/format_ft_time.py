import time
from datetime import datetime

timestamp = time.time()
scientific = f"{timestamp:.2e}"
date = datetime.fromtimestamp(timestamp).strftime("%b %d %Y")

print(f"Seconds since January 1, 1970: {timestamp:,.4f} or {scientific} in scientific notation")
print(date)
