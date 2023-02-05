student_data = {}

while True:
    register_number = input("Enter the register number (or type 'q' to quit): ")
    if register_number == 'q':
        break

    marks = int(input("Enter the marks: "))

    student_data[register_number] = marks

print(student_data)
