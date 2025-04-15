# from flask import Flask, request, jsonify
# import requests

# app = Flask(__name__)

# @app.route('/generate', methods=['POST'])
# def handle_generation():
#     try:
#         data = request.json
#         prompt = data.get("prompt", "").strip()
#         language = data.get("language", "python").strip().lower()

#         if not prompt:
#             return jsonify({"error": "No prompt provided"}), 400

#         # Format the prompt for better model understanding
#         full_prompt = f"Generate {language} code for the following problem:\n{prompt}"

#         # Send request to the model server (server.py)
#         response = requests.post("http://localhost:5000/generate", json={"prompt": full_prompt})
#         return jsonify(response.json())

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# if __name__ == "__main__":
#     app.run(port=5001)



















import requests

def main():
    prompt = input("Enter your prompt: ")
    language = input("Enter language (e.g. python, cpp, java): ")

    try:
        response = requests.post("http://localhost:5001/generate", json={
            "prompt": prompt,
            "language": language
        })

        print("\nFull Response JSON:")
        print(response.json())  # Debug line

        if response.status_code == 200:
            data = response.json()
            print("\nGenerated Code:\n")
            print(data.get("response", "[No 'response' field in response]"))
        else:
            print("Error:", response.status_code, response.text)
    except Exception as e:
        print("Error:", str(e))

if __name__ == "__main__":
    main()
