from flask import Flask, request, jsonify

app = Flask(__name__)

# Define the POST endpoint
@app.route('/bfhl', methods=['POST'])
def handle_post():
    try:
        # Extract data from request
        data = request.json.get('data', [])
        
        # Initialize response components
        numbers = []
        alphabets = []
        highest_lowercase_alphabet = []
        user_id = "john_doe_17091999"  # hardcoded example values
        email = "john@xyz.com"
        roll_number = "ABCD123"

        # Separate numbers and alphabets
        for item in data:
            if item.isdigit():
                numbers.append(item)
            elif item.isalpha():
                alphabets.append(item)
                if item.islower():
                    highest_lowercase_alphabet.append(item)

        # Determine the highest lowercase alphabet
        if highest_lowercase_alphabet:
            highest_lowercase_alphabet = [max(highest_lowercase_alphabet)]
        else:
            highest_lowercase_alphabet = []

        # Construct response
        response = {
            "is_success": True,
            "user_id": user_id,
            "email": email,
            "roll_number": roll_number,
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": highest_lowercase_alphabet
        }
        return jsonify(response), 200

    except Exception as e:
        # Error handling
        return jsonify({"is_success": False, "message": str(e)}), 400

# Define the GET endpoint
@app.route('/bfhl', methods=['GET'])
def handle_get():
    response = {
        "operation_code": 1
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
