from datetime import datetime


now = datetime.today()
print(now.strftime("%a %b %d %H:%M:%S %Z %Y"))

print(now.strftime("%Z"))