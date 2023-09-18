from tkinter import *
from tkinter import messagebox


# Create a dictionary to simulate teacher and student data
teacher_data = {
    "teacher1"       
    : "password1",
    "teacher2": "password2"
}

student_data = {
    "student1": {
        "password": "password1",
        "courses": ["Math", "Science", "History"],
        "grades":{"Math": {"Quiz1": 90, "Quiz2": 85,"Quize3":90},
                  "Science": {"Quiz1": 78, "Quiz2": 92},
                  "History": {"Quiz1": 88, "Quiz2": 76}
                  }
    },
    "student2": {
        "password": "password2",
        "courses": ["English", "Art", "Music"],
        "grades": {
            "English": {"Quiz1": 92, "Quiz2": 88},
            "Art": {"Quiz1": 75, "Quiz2": 80},
  
        }
    }
}

root = Tk()
root.title("Welcome")
root.geometry("500x500")

# Global variables
entry_username = None
entry_password = None

def register(username, password, role):
    # Perform registration logic here based on the role (teacher or student)
    if role == "teacher":
        # You can implement teacher registration logic here
        teacher_data[username] = {"password": password, "courses": [], "grades": {}}
    messagebox.showinfo("Register", "Registration successful!")
        pass
    elif role == "student":
        student_data[username] = {"password": password, "courses": [], "grades": {}}
    messagebox.showinfo("Register", "Registration successful!")

def login(username, password, role):
    # Check if username and password are correct based on the role (teacher or student)
    if role == "teacher":
        if username in teacher_data and teacher_data[username]["password"] == password:
            messagebox.showinfo("Login", "Teacher login successful!")
            open_teacher_page(username)
        else:
            messagebox.showerror("Login", "Invalid username or password")
    elif role == "student":
        if username in student_data and student_data[username]["password"] == password:
            messagebox.showinfo("Login", "Student login successful!")
            open_student_page(username)
        else:
            messagebox.showerror("Login", "Invalid username or password")

def open_student_page(username):
    root.withdraw()  # Hide the login/register window

    student_page = Tk()
    student_page.title("Student Page")
    student_page.geometry("500x500")

    label_student = Label(student_page, text=f"Welcome, {username}!")
    label_student.pack()

    # Add buttons for viewing profile, courses, grades, and quizzes
    def view_profile():
        profile_window = Toplevel(student_page)
        profile_window.title("View Profile")
        profile_window.geometry("400x400")

        # Display student profile information
        profile_label = Label(profile_window, text=f"Student: {username}")
        profile_label.pack()

        
    def view_courses():
        courses_window = Toplevel(student_page)
        courses_window.title("Courses")
        courses_window.geometry("400x400")

        # Display student's enrolled courses
        courses_label = Label(courses_window, text=f"Courses: {', '.join(student_data[username]['courses'])}")
        courses_label.pack()

    def view_grades():
        grades_window = Toplevel(student_page)
        grades_window.title("Grades")
        grades_window.geometry("400x400")
        
    

        for course, grade_dict in student_data[username]['grades'].items():
            course_label = Label(grades_window, text=f"Course: {course}")
            course_label.pack()

            for quiz, score in grade_dict.items():
                quiz_label = Label(grades_window, text=f"{quiz}: {score}")
                quiz_label.pack()


    def add_course():
        add_course_window = Toplevel(student_page)
        add_course_window.title("Add Course")
        add_course_window.geometry("400x400")

        course_name_label = Label(add_course_window, text="Course Name:")
        course_name_label.pack()
        course_name_entry = Entry(add_course_window)
        course_name_entry.pack()

        def save_course():
            course_name = course_name_entry.get()
            for student in student_data.values():
                student["courses"].append(course_name)
                student["grades"][course_name] = {}
            messagebox.showinfo("Add Course", "Course added successfully!")
            add_course_window.destroy()
        save_course_button = Button(add_course_window, text="Save Course", command=save_course)
        save_course_button.pack()
    
   



          



    view_profile_button = Button(student_page, text="View Profile", command=view_profile)
    view_profile_button.pack()

    view_courses_button = Button(student_page, text="View Courses", command=view_courses)
    view_courses_button.pack()

    view_grades_button = Button(student_page, text="View Grades", command=view_grades)
    view_grades_button.pack()

    add_subject_button = Button(student_page, text="Add Subject", command=add_course)
    add_subject_button.pack() 

    
    student_page.mainloop()

def open_teacher_page(username):
    root.withdraw()  # Hide the login/register window

    teacher_page = Tk()
    teacher_page.title("Teacher Page")
    teacher_page.geometry("500x500")

    label_teacher = Label(teacher_page, text=f"Welcome Dr, {username}!")
    label_teacher.pack()

    def add_student():
        add_student_window = Toplevel(teacher_page)
        add_student_window.title("Add Student")
        add_student_window.geometry("400x400")

        student_username_label = Label(add_student_window, text="Student Username:")
        student_username_label.pack()
        student_username_entry = Entry(add_student_window)
        student_username_entry.pack()

        student_password_label = Label(add_student_window, text="Student Password:")
        student_password_label.pack()
        student_password_entry = Entry(add_student_window, show="*")
        student_password_entry.pack()

        def save_student():
            student_username = student_username_entry.get()
            student_password = student_password_entry.get()
            student_data[student_username] = {"password": student_password, "courses": [], "grades": {}}
            messagebox.showinfo("Add Student", "Student added successfully!")
            add_student_window.destroy()

        save_student_button = Button(add_student_window, text="Save Student", command=save_student)
        save_student_button.pack()

    def add_course():
        add_course_window = Toplevel(teacher_page)
        add_course_window.title("Add Course")
        add_course_window.geometry("400x400")

        course_name_label = Label(add_course_window, text="Course Name:")
        course_name_label.pack()
        course_name_entry = Entry(add_course_window)
        course_name_entry.pack()

        def save_course():
            course_name = course_name_entry.get()
            for student in student_data.values():
                student["courses"].append(course_name)
                student["grades"][course_name] = {}
            messagebox.showinfo("Add Course", "Course added successfully!")
            add_course_window.destroy()

        save_course_button = Button(add_course_window, text="Save Course", command=save_course)
        save_course_button.pack()

    def add_grade():
        add_grade_window = Toplevel(teacher_page)
        add_grade_window.title("Add Grade")
        add_grade_window.geometry("400x400")

        student_label = Label(add_grade_window, text="Student:")
        student_label.pack()
        student_var = StringVar()
        student_dropdown = OptionMenu(add_grade_window, student_var, *student_data.keys())
        student_dropdown.pack()

        course_label = Label(add_grade_window, text="Course:")
        course_label.pack()
        course_var = StringVar()
        course_dropdown = OptionMenu(add_grade_window, course_var, "")
        course_dropdown.pack()

        def update_course_dropdown(*args):
            selected_student = student_var.get()
            courses = student_data[selected_student]["courses"]
            course_dropdown["menu"].delete(0, "end")
            for course in courses:
                course_dropdown["menu"].add_command(label=course, command=lambda c=course: course_var.set(c))

        student_var.trace("w", update_course_dropdown)

        quiz_label = Label(add_grade_window, text="Quiz Name:")
        quiz_label.pack()
        quiz_entry = Entry(add_grade_window)
        quiz_entry.pack()

        score_label = Label(add_grade_window, text="Score:")
        score_label.pack()
        score_entry = Entry(add_grade_window)
        score_entry.pack()

        def save_grade():
            selected_student = student_var.get()
            selected_course = course_var.get()
            quiz_name = quiz_entry.get()
            score = score_entry.get()

            if selected_student in student_data and selected_course in student_data[selected_student]["courses"]:
                student_data[selected_student]["grades"][selected_course][quiz_name] = int(score)
                messagebox.showinfo("Add Grade", "Grade added successfully!")
                add_grade_window.destroy()
            else:
                messagebox.showerror("Add Grade", "Invalid student or course selection!")

        save_grade_button = Button(add_grade_window, text="Save Grade", command=save_grade)
        save_grade_button.pack()

    add_student_button = Button(teacher_page, text="Add Student", command=add_student)
    add_student_button.pack()

    add_course_button = Button(teacher_page, text="Add Course", command=add_course)
    add_course_button.pack()

    add_grade_button = Button(teacher_page, text="Add Grade", command=add_grade)
    add_grade_button.pack()

    teacher_page.mainloop()

# Global variables
entry_username = None
entry_password = None

def tab2():
    Label1.destroy()
    Button1.destroy()
    Button2.destroy()
    Label2 = Label(root, text="Teacher Login or Register", font=('times_new_roman', 25))
    Label2.pack()

    global entry_username, entry_password
    label_username = Label(root, text="Username:")
    label_username.pack()
    entry_username = Entry(root)
    entry_username.pack()

    label_password = Label(root, text="Password:")
    label_password.pack()
    entry_password = Entry(root, show="*")
    entry_password.pack()

    button_register = Button(root, text="Register", command=lambda: register(entry_username.get(), entry_password.get(), "teacher"))
    button_register.pack()

    button_login = Button(root, text="Login", command=lambda: login(entry_username.get(), entry_password.get(), "teacher"))
    button_login.pack()

def tab3():
    Label1.destroy()
    Button1.destroy()
    Button2.destroy()
    Label2 = Label(root, text="Student Login or Register", font=('times_new_roman', 25))
    Label2.pack()

    global entry_username, entry_password
    label_username = Label(root, text="Username:")
    label_username.pack()
    entry_username = Entry(root)
    entry_username.pack()

    label_password = Label(root, text="Password:")
    label_password.pack()
    entry_password = Entry(root, show="*")
    entry_password.pack()

    button_register = Button(root, text="Register", command=lambda: register(entry_username.get(), entry_password.get(), "student"))
    button_register.pack()

    button_login = Button(root, text="Login", command=lambda: login(entry_username.get(), entry_password.get(), "student"))
    button_login.pack()

Label1 = Label(root, text="Are you a teacher or student?", font=('times_new_roman', 25))
Label1.pack()

Button1 = Button(root, text='Teacher', font=('times_new_roman', 25), command=tab2)
Button1.pack()

Button2 = Button(root, text='Student', font=('times_new_roman', 25), command=tab3)
Button2.pack()

root.mainloop()




