from datetime import datetime

now = datetime.now()
epoch = now.timestamp()
print(
    f"Seconds since January 1, 1970: {epoch:,.4f} or {epoch:.2e}",
    "in scientific notation",
)
print(now.strftime("%b %d %Y"))
