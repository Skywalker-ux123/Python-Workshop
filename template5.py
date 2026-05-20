from flask import Flask, jsonify

app = Flask(__name__)

# 1. A Simple Homepage Route
@app.route("/")
def home():
    # TODO: Return a simple HTML string welcoming users to the API
    return "YOUR_HTML_STRING_HERE"

# 2. A Dynamic API Route
# This route takes a <word> from the URL and judges its vibe
@app.route("/judge/<word>")
def judge_vibe(word):
    word = word.lower()
    
    # TODO: Write an if/elif/else statement to return a verdict based on the word!
    # Example: if word == "pizza", verdict = "NOT GUILTY"
    
    if word in ["coffee", "pizza", "sleep"]:
        verdict = "YOUR_CODE_HERE"
    elif word in ["homework", "traffic", "exam"]:
        verdict = "YOUR_CODE_HERE"
    else:
        verdict = "MID"

    # We return the data as JSON, the standard language of the web!
    return jsonify({
        "subject": word,
        "verdict": verdict
    })

if __name__ == "__main__":
    print("🚀 Server starting! Go to http://127.0.0.1:5000 in your browser.")
    app.run(debug=True)