import json  # For saving and loading data


# ==========================break_point_add_function======================================================================

class StudentSystem:
    def __init__(self):  # self is a reference to the current instance of the class
        # Dictionary to hold all students
        # Key = student_id, Value = {name, age, grades, info_tuple}
        self.students_dictionary = {}

    def add_student(self):
        student_name = str(input("Please input student name: "))
        age = int(input("Please input your age: "))
        student_id = int(input("Please enter your ID: "))

        grades_list = []  # COLLECTION OF MULTIPLE GRADES
        num_of_grades = int(input("How many grades do you want to enter? "))
        for i in range(num_of_grades):
            grade = float(input("Enter grade {0}: ".format(i + 1)))
            grades_list.append(grade)  # append is used to add an item to the end of the list

        student_tuple = (student_id, student_name)  # use tuple to store permanent or fixed information

        self.students_dictionary[student_id] = {
            # stores student information in a dictionary, where it needs key-value pairs
            "name": student_name,
            "age": age,
            "grades": grades_list,
            "info_tuple": student_tuple
        }

        print("Student {0} added successfully with ID {1}".format(student_name, student_id))  # CONFIRMATION MESSAGE


# ==========================break_point_display_function======================================================================

class DisplayStudents(StudentSystem):  # MERGED CLASS FROM MAIN
    def display_students(self):  # DISPLAY STUDENT FUNCTION
        if not self.students_dictionary:  # IF STUDENT IS NOT FOUND IN THE DICTIONARY
            print("No students found!")
        else:
            print("List of students:")  # LIST THE STUDENT IF NEW
            for student_id, student_info in self.students_dictionary.items():
                print("ID: {0}, Name: {1}, Age: {2}, Grades: {3}".format(
                    student_id, student_info['name'], student_info['age'], student_info['grades']
                ))


# ==========================break_point_update_function======================================================================

class UpdateStudent(StudentSystem):  # MERGED CLASS FROM MAIN
    def update_student(self):  # UPDATE STUDENT FUNCTION
        student_id = int(input("Enter the ID of the student to update: "))
        if student_id in self.students_dictionary:
            print("1. Update Name")
            print("2. Update Age")
            print("3. Update Grades")
            print("4. Update Info Tuple")
            choice2 = int(input("Enter your choice: "))

            if choice2 == 1:
                new_name = input("Enter new name: ")  # NEW NAME CHANGE UPDATE
                self.students_dictionary[student_id]["name"] = new_name
                print("Name updated successfully for the student with ID {0}!".format(student_id))

            elif choice2 == 2:
                new_age = int(input("Enter new age: "))  # NEW AGE CHANGE UPDATE
                self.students_dictionary[student_id]["age"] = new_age
                print("Age updated successfully for the student with ID {0}!".format(student_id))

            elif choice2 == 3:  # NEW GRADES CHANGE UPDATE
                new_grades = input("Enter new grades (comma separated): ").split(",")
                self.students_dictionary[student_id]["grades"] = [float(grade) for grade in new_grades]
                print("Grades updated successfully for the student with ID {0}!".format(student_id))

            elif choice2 == 4:  # NEW INFO TUPLE CHANGE UPDATE
                new_info_tuple = input("Enter new info tuple (comma separated): ").split(",")
                self.students_dictionary[student_id]["info_tuple"] = tuple(new_info_tuple)
                print("Info tuple updated successfully for the student with ID {0}!".format(student_id))

            else:  # INVALID INPUTS
                print("Invalid choice! Please try again.")
        else:
            print("Student with ID {0} not found!".format(student_id))


# ==========================break_point_delete_function======================================================================

class DeleteStudent(StudentSystem):  # MERGED CLASS FROM MAIN
    def delete_student(self):  # DELETE STUDENT FEATURE
        student_id = int(input("Enter the ID of the student to delete: "))
        if student_id in self.students_dictionary:
            del self.students_dictionary[student_id]
            print("Student with ID {0} deleted successfully!".format(student_id))
        else:
            print("Student with ID {0} not found!".format(student_id))


# ==========================break_point_save_to_file_function======================================================================

class SaveToFile(StudentSystem):  # MERGED CLASS FROM MAIN
    def save_to_file(self):  # SAVE TO FILE FEATURE
        with open("students_data.json", "w") as file:
            json.dump(self.students_dictionary, file, indent=4)
        print("Data saved to students_data.json successfully!")


# ==========================break_point_load_from_file_function======================================================================

class LoadFromFile(StudentSystem):  # MERGED CLASS FROM MAIN
    def load_from_file(self):  # LOAD DATA FROM JSON FILE
        try:
            with open("students_data.json", "r") as file:
                self.students_dictionary = json.load(file)
            print("Data loaded from students_data.json successfully!")
        except FileNotFoundError:
            print("No data file found! Please save data first.")


# =======================================Main_Menu======================================================================

class StudentManagementSystem( DisplayStudents, UpdateStudent, DeleteStudent, SaveToFile, LoadFromFile):
    pass


system = StudentManagementSystem()

while True:
    print("\n===== Student Information System =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Save to File")
    print("6. Load from File")
    print("7. Exit")
    option = int(input("Enter your choice: "))

    if option == 1:  # ADD STUDENT
        system.add_student()

    elif option == 2:  # DISPLAY STUDENT
        system.display_students()

    elif option == 3:  # UPDATE STUDENT
        system.update_student()

    elif option == 4:  # DELETE STUDENT
        system.delete_student()

    elif option == 5:  # SAVE TO FILE
        system.save_to_file()

    elif option == 6:  # LOAD FROM FILE
        system.load_from_file()

    elif option == 7:  # EXIT
        print("Exiting the system. Goodbye!")
        break

    else:
        print("Invalid option! Please try again.")

    # =======================================Main_Menu_Breakpoint======================================================================

    # DOCUMENTATION:

    """
    problems
    1. looping the menu option - fixed

    2. if nested - fixed

    3. indentation issues - fixed

    4. variable names inconsistent - 

    5. 




    #key note: Define a function
    #Similar situation in Java: public void methodName() is equivalent to  = def method_name(self:)

    #Constructor:
    #public ClassName() in Java is equivalent to def _init_(self): in python

    #If your while True: menu loop is at the top, it will try to run before your class is even defined.
    When Python sees system = StudentSystem(), it needs to already know what StudentSystem is.
    That means all class definitions must be above the code that uses them.

"""

# variables used in the code:

"""

Menu & Option Handling

option → stores user choice from the menu.

Student Info (Inside add_student)

student - stores the student's name (but sometimes called student_name).
age - stores student's age.
ID - student'S ID
grades_list - list of grades for the student 
num_of_grades - number of grades to enter.
grade - each grade entered.
Student_tuple - tuple containing (student_id, student_name).

Dictionary to Store Students

self.students_dictionary - dictionary holding all students:

Display Students

student_id - key in the dictionary.
student_info - dictionary containing details of a single student.

Update Students

choice2 - user's choice for what to update.
new_name - new name for the student.
new_age - new age for the student.
new_grades - new grades list.
new_info_tuple - new tuple with updated info.



Delete Students

student_id - ID entered by the user for deletion.


Miscellaneous

self - reference to the current object instance of a class.

    """