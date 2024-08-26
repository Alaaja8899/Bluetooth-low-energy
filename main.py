import random
import json
import subprocess
from datetime import datetime, timedelta

FILE_PATH = './data.json'

def get_random_int(min_val, max_val):
    return random.randint(min_val, max_val)

def make_commit(n):
    if n == 0:
        subprocess.run(["git", "push"])
        return

    x = get_random_int(0, 54)
    y = get_random_int(0, 6)
    date = (datetime.now() - timedelta(weeks=52 - x, days=y)).strftime('%Y-%m-%dT%H:%M:%S')

    data = {
        "date": date
    }

    print(date)

    with open(FILE_PATH, 'w') as f:
        json.dump(data, f)

    subprocess.run(["git", "add", FILE_PATH])
    subprocess.run(["git", "commit", "-m", date, "--date", date])

    make_commit(n - 1)

make_commit(500)
