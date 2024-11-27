from flask import Blueprint, jsonify
from agents import analyze_fitness, analyze_sleep, analyze_journaling
from insights import aggregate_insights

api = Blueprint('api', __name__)

# Endpoint for fitness data
@api.route('/api/fitness', methods=['GET'])
def get_fitness_insights():
    return jsonify(analyze_fitness())

# Endpoint for sleep data
@api.route('/api/sleep', methods=['GET'])
def get_sleep_insights():
    return jsonify(analyze_sleep())

# Endpoint for journaling data
@api.route('/api/journaling', methods=['GET'])
def get_journaling_insights():
    return jsonify(analyze_journaling())

# Endpoint for aggregated insights
@api.route('/api/insights', methods=['GET'])
def get_aggregated_insights():
    return jsonify(aggregate_insights())

def register_routes(app):
    app.register_blueprint(api)
