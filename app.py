from flask import Flask, render_template
from datetime import datetime

import random

app = Flask(__name__)

# DevOps journey started in February 2025
START_DATE = datetime(2025, 2, 1)

def get_devops_metrics():
    return {
        "days_learning": (datetime.now() - START_DATE).days,
        "containers_launched": random.randint(50, 200),
        "servers_configured": random.randint(10, 50),
        "terraform_wins": random.randint(5, 20),
        "last_cicd_fail": f"{random.randint(0, 7)} days ago",
        "current_quest": "Kubernetes Mastery",
        "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

@app.route('/')
def dashboard():
    metrics = get_devops_metrics()
    return render_template('dashboard.html', metrics=metrics)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)