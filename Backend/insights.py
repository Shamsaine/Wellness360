from agents import analyze_fitness, analyze_sleep, analyze_journaling

def aggregate_insights():
    fitness = analyze_fitness()
    sleep = analyze_sleep()
    journaling = analyze_journaling()
    return {
        "fitness": fitness,
        "sleep": sleep,
        "journaling": journaling,
        "overall_recommendation": "Focus on improving sleep consistency and increasing physical activity."
    }
