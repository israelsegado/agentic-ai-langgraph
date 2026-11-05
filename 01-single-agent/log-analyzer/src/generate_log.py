import random
from datetime import datetime, timedelta

random.seed(12)
lines = []
dt = datetime.now()
for i in range(12000):
    dt += timedelta(seconds=random.randint(1, 5))
    ts = dt.strftime("%Y-%m-%dT%H:%M:%S+0100")
    r = random.random()
    if r < 0.90:
        msg = "systemd[1]: Started Daily apt activities."
    elif r < 0.95:
        msg = "sshd[812]: Failed password for root from 203.0.113.7 port 51000"
    elif r < 0.98:
        msg = "nginx[455]: [error] connect() failed (111: Connection refused) upstream"
    else:
        msg = "kernel: Out of memory: Killed process 3021 (java)"

    lines.append(f"{ts} myhost {msg}")

open("../test-logs/data.log", 'w').write("\n".join(lines))