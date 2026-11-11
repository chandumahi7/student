from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

# Initial Student Database with ID, Name, Course, Attendance, and Marks
students = [
    {
        "id": "S101",
        "name": "LIKITHA",
        "course": "Data Science",
        "attendance": 85,
        "marks": 92,
    },
    {
        "id": "S102",
        "name": "Vikram Kumar",
        "course": "Electronics",
        "attendance": 62,
        "marks": 38,
    },
    {
        "id": "S103",
        "name": "Sonia Verma",
        "course": "Information Technology",
        "attendance": 90,
        "marks": 78,
    },
    {
        "id": "S104",
        "name": "Kiran Patel",
        "course": "Mechanical",
        "attendance": 70,
        "marks": 45,
    },
]


# Route to serve the Frontend UI
@app.route("/")
def index():
  return render_template("index.html")


# API: Get all students
@app.route("/api/students", methods=["GET"])
def get_students():
  return jsonify(students)


# API: Add a new student
@app.route("/api/students", methods=["POST"])
def add_student():
  data = request.get_json()
  student_id = data.get("id")

  # Check if ID already exists
  if any(s["id"].lower() == student_id.lower() for s in students):
    return jsonify({"error": "Student ID already exists!"}), 400

  new_student = {
      "id": student_id,
      "name": data.get("name"),
      "course": data.get("course"),
      "attendance": int(data.get("attendance", 0)),
      "marks": int(data.get("marks", 0)),
  }
  students.append(new_student)
  return (
      jsonify({"message": "Student added successfully", "student": new_student}),
      201,
  )


# API: Delete a student by ID
@app.route("/api/students/<string:student_id>", methods=["DELETE"])
def delete_student(student_id):
  global students
  students = [s for s in students if s["id"].lower() != student_id.lower()]
  return jsonify({"message": "Student deleted successfully"})


if __name__ == "__main__":
  app.run(debug=True)