import time

# Get the current time in seconds since the epoch
epoch_seconds = time.time()

# Convert it to a local time object (the time at epoch 0)
local_time = time.localtime()

time2 =  time.localtime(0)
formatted_time1 = time.strftime("%B %-d, %Y", time2)
# Get the formatted local time in human-readable format
formatted_time = time.strftime("%B %-d, %Y", local_time)

# Print the seconds since epoch and the formatted time
print(f"Seconds since {formatted_time1}: {epoch_seconds:.4f} or {epoch_seconds:.2e} in scientific notation")
print(f"{formatted_time}")
