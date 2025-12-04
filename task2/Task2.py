# -----------------------------
# Student Grade Calculator
# -----------------------------

# This function takes marks and returns (grade, comment)
def get_grade_and_comment(marks):
    # Optional debug print:
    # print("Debug: Inside get_grade_and_comment with marks =", marks)

    if marks >= 90:
        grade = "A+"
        comment = "Outstanding performance! 🎉"
    elif marks >= 80:
        grade = "A"
        comment = "Excellent work, keep it up!"
    elif marks >= 70:
        grade = "B"
        comment = "Good job! You can push a little more."
    elif marks >= 60:
        grade = "C"
        comment = "Fair, but there’s room to improve."
    elif marks >= 50:
        grade = "D"
        comment = "You passed, but try to study more next time."
    else:
        grade = "F"
        comment = "Needs improvement. Don’t give up!"

    return grade, comment


# -----------------------------
# Main Program
# -----------------------------

print("🎓 Student Grade Calculator")
print("Type 'q' anytime to finish.\n")

results = []  # This list will store all student results

while True:
    name = input("Enter student name (or 'q' to quit): ")

    if name.lower() == "q":
        break  # Exit the loop

    marks_input = input(f"Enter marks for {name} (0–100) or 'q' to quit: ")

    if marks_input.lower() == "q":
        break

    # Use print() to debug raw input if needed
    # print("Debug: Raw marks input =", marks_input)

    # Validate and convert marks to integer
    try:
        marks = int(marks_input)
    except ValueError:
        print("❌ Please enter a valid number for marks.\n")
        continue

    if marks < 0 or marks > 100:
        print("❌ Marks must be between 0 and 100.\n")
        continue

    # Get grade and comment using our function
    grade, comment = get_grade_and_comment(marks)

    # Store result in the list as a dictionary
    student_result = {
        "name": name,
        "marks": marks,
        "grade": grade,
        "comment": comment
    }
    results.append(student_result)

    # Show result immediately
    print(f"\n✅ Result for {name}:")
    print(f"   Marks  : {marks}")
    print(f"   Grade  : {grade}")
    print(f"   Comment: {comment}\n")

# -----------------------------
# Summary of all students
# -----------------------------

print("\n📋 Summary of all student results:")
if not results:
    print("No student data entered.")
else:
    for idx, r in enumerate(results, start=1):
        print(f"{idx}. {r['name']} - {r['marks']} marks - Grade: {r['grade']} - {r['comment']}")
