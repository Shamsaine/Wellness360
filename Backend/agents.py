import json

# Load mock data once at app start
with open("data/mock_data.json") as file:
    mock_data = json.load(file)

# Fitness agent logic
def analyze_fitness():
    metrics = mock_data["wearable_data"]["metrics"]
    avg_steps = sum(m["steps"] for m in metrics) / len(metrics)
    return {
        "average_steps": avg_steps,
        "recommendation": "Increase daily steps to reach a goal of 10,000 steps."
    }

# Sleep agent logic
def analyze_sleep():
    metrics = mock_data["wearable_data"]["metrics"]
    avg_sleep = sum(m["sleep_hours"] for m in metrics) / len(metrics)
    poor_sleep_days = [m for m in metrics if m["sleep_hours"] < 6]
    return {
        "average_sleep_hours": avg_sleep,
        "poor_sleep_days": poor_sleep_days,
        "recommendation": "Try a consistent bedtime to improve sleep quality."
    }

# Journaling sentiment agent logic
def analyze_journaling():
    entries = mock_data["journaling_data"]["journal_entries"]
    sentiments = {"positive": 0, "negative": 0, "neutral": 0}
    for entry in entries:
        sentiment_score = len(entry["entry"]) % 3  # Mock sentiment logic
        if sentiment_score == 0:
            sentiments["positive"] += 1
        elif sentiment_score == 1:
            sentiments["negative"] += 1
        else:
            sentiments["neutral"] += 1
    return {
        "sentiments": sentiments,
        "recommendation": "Maintain positive journaling habits to improve mental health."
    }
