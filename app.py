from flask import Flask, jsonify, request

app = Flask(__name__)

# Load the data
data = []
try:
    with open('data.json') as f:
        data = json.load(f)
except Exception as e:
    print(e)

# Define the recommendation function
def recommend_content(user_id):
    # Get the user's preferences
    user_preferences = data[user_id]['preferences']

    # Find other users with similar preferences
    similar_users = []
    for user in data:
        if user['preferences'] == user_preferences:
            similar_users.append(user)

    # Recommend content to the user
    recommended_content = []
    for user in similar_users:
        for item in user['recommended_content']:
            if item not in user_recommended_content:
                recommended_content.append(item)

    return recommended_content

# Create the route for getting recommendations
@app.route('/recommendations/<int:user_id>')
def get_recommendations(user_id):
    # Get the recommendations
    recommendations = recommend_content(user_id)

    # Return the recommendations as JSON
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True)