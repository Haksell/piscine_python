from datetime import datetime

# Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09 in scientific notation
# Oct 21 2022

now = datetime.now()
epoch = now.timestamp()
print(f"Seconds since January 1, 1970: {epoch:,.4f} or {epoch:.3g} in scientific notation")
print(now.strftime("%b %d %Y"))
