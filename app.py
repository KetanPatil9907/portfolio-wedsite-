from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/contact", methods=["POST"])
def contact():
    data = request.get_json()

    name = data.get("name", "")
    email = data.get("email", "")
    message = data.get("message", "")

    if not name or not email or not message:
        return jsonify({
            "success": False,
            "message": "Please fill all fields."
        }), 400

    # For now, we only display the submitted data in the server console.
    # Later you can connect this to a database or email service.
    print("New Contact Message")
    print("Name:", name)
    print("Email:", email)
    print("Message:", message)

    return jsonify({
        "success": True,
        "message": "Thank you! Your message has been received."
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)