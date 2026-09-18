from flask import Flask, jsonify

app = Flask(__name__)


employees = [
    {
        "id": 1,
        "name": "John",
        "role": "QA Engineer"
    },
    {
        "id": 2,
        "name": "Sarah",
        "role": "DevOps Engineer"
    },
    {
        "id": 3,
        "name": "David",
        "role": "Developer"
    }
]


@app.route("/")
def home():
    return """
    <h1>DevOps Employee Management System</h1>
    <p>Application is running successfully.</p>
    """


@app.route("/health")
def health():
    return jsonify({
        "status": "UP"
    })


@app.route("/employees")
def get_employees():
    return jsonify(employees)


@app.route("/employees/<int:employee_id>")
def get_employee(employee_id):

    for employee in employees:
        if employee["id"] == employee_id:
            return jsonify(employee)

    return jsonify({
        "error": "Employee not found"
    }), 404


if __name__ == "__main__":
    import os

    port = int(os.environ.get("PORT", 5000))

    app.run(
        host="0.0.0.0",
        port=port
    )