from graphics import GraphWin, Rectangle, Point, Text

progression_data = []
#count_calculation = 0 before run the programme
student_progress_count_calculation = 0  
student_module_trailer_count_calculation = 0
student_exclude_count_calculation = 0
student_d_module_count_calculation = 0
student_total_count_calculation = 0

# Function to draw a bar in the histogram
def draw_bar(win, category, count, total, x, y, width, height):
    percent = count / total
    bar_height = percent * height
    bar = Rectangle(Point(x, y), Point(x + width, y - bar_height))
    bar.setFill(category_colors[category])
    bar.draw(win)

    label = Text(Point(x + width / 2, y - bar_height / 2), f"{count}\n")
    label.setSize(10)
    label.draw(win)
    # Add text label below the x-axis line
    label_below = Text(Point(x + width / 2, y + 15), f"{category}")
    label_below.setSize(12)
    label_below.draw(win)
# Function to create and display the histogram
def display_histogram(progress, trailer, retriever, exclude):
    total_students = progress + trailer + retriever + exclude

    win_width = 600
    win_height = 400
    win = GraphWin("Progress Histogram", win_width, win_height)
    win.setBackground("white")

    # Draw bars for each category
    x_position = 100
    bar_width = 100
    bar_height = 200
    y_position = win_height - 80

    draw_bar(win, "Progress", progress, total_students, x_position, y_position, bar_width, bar_height)
    x_position += bar_width

    draw_bar(win, "Trailer", trailer, total_students, x_position, y_position, bar_width, bar_height)
    x_position += bar_width

    draw_bar(win, "Retriever", retriever, total_students, x_position, y_position, bar_width, bar_height)
    x_position += bar_width

    draw_bar(win, "Exclude", exclude, total_students, x_position, y_position, bar_width, bar_height)

    # Display total number of students
    total_label = Text(Point(win_width / 2, win_height - 20), f"Total Students: {total_students}")
    total_label.setSize(15)
    total_label.draw(win)

    win.getMouse()  # Wait for a mouse click to close the window
    win.close()

# Initialize counts for each category
progress_count = 0
trailer_count = 0
retriever_count = 0
exclude_count = 0
#function for check the range
def range_check_for_staff_version(your_input_1):  
    if your_input_1 <= 120 and your_input_1 >= 0 and your_input_1 % 20 == 0:
        boolean_save_1 = True

    else:
        print("Out of range.")
        boolean_save_1 = False
        return boolean_save_1

# Function to save progression data to a text file
def save_progression_data():
    with open('progression_data.txt', 'w') as file:
        for data in progression_data:
            outcome, pass_mark, defer_mark, fail_mark = data
            file.write(f"{outcome} - {pass_mark}, {defer_mark}, {fail_mark}\n")
# Function to access and print stored progression data
def print_stored_data():
    with open('progression_data.txt', 'r') as file:
        stored_data = file.readlines()
        for line in stored_data:
            print(line.strip())

while True:
    boolean_save_2 = False
    while boolean_save_2 == False:

        boolean_range = False
        while boolean_range == False:
            try:
                student_pass_mark_for_staff_version = int(input("Please enter PASS credit\t: "))
                boolean_range = range_check_for_staff_version(student_pass_mark_for_staff_version)

            except ValueError:
                print("Integers required")
                boolean_range = False

        boolean_range = False
        while boolean_range == False:
            try:
                student_defer_mark_for_staff_version = int(input("Please enter DEFER credit\t: "))
                boolean_range = range_check_for_staff_version(student_defer_mark_for_staff_version)

            except ValueError:
                print("Integers required")
                boolean_range = False

        boolean_range = False
        while boolean_range == False:
            try:
                student_fail_mark_for_staff_version = int(input("Please enter FAIL credit\t: "))
                boolean_range = range_check_for_staff_version(student_fail_mark_for_staff_version)

            except ValueError:
                print("Integers required")
                boolean_range = False
                
        total_mark_for_staff_version = student_pass_mark_for_staff_version + student_fail_mark_for_staff_version + student_defer_mark_for_staff_version
        if total_mark_for_staff_version == 120:  # Total calculated by the sum of 3 credit types
            boolean_save_2 = True
        else:
            print("Total incorrect")
            boolean_save_2 = False

    if student_pass_mark_for_staff_version == 120:
        print("Progress")
        progression_data.append(("Progress", student_pass_mark_for_staff_version,student_defer_mark_for_staff_version,student_fail_mark_for_staff_version))
        progress_count += 1

    elif student_pass_mark_for_staff_version == 100:
        print("Progress–module trailer")
        progression_data.append(("Progress (module trailer)", student_pass_mark_for_staff_version,student_defer_mark_for_staff_version,student_fail_mark_for_staff_version))
        trailer_count += 1
    elif student_fail_mark_for_staff_version >= 80:
        print("Exclude")
        progression_data.append(("Exclude",  student_pass_mark_for_staff_version,student_defer_mark_for_staff_version,student_fail_mark_for_staff_version))
        exclude_count += 1
    else:
        print("Do not progress–module retriever")
        progression_data.append(("Module retriever",  student_pass_mark_for_staff_version,student_defer_mark_for_staff_version,student_fail_mark_for_staff_version))
        retriever_count += 1

    student_total_count_calculation = student_d_module_count_calculation + student_exclude_count_calculation + student_module_trailer_count_calculation + student_progress_count_calculation
    input_command_for_exit = input("\nWould you like to enter another set of data? \nEnter 'y' for yes or 'q' to quit and view results:  ")
    if input_command_for_exit == "q":
        save_progression_data()  
        print("\n")
        
        break  # break used for stop the programme
    else:
        print("\n")
        continue
# Print the stored data in the required format
for data in progression_data:
    outcome, pass_mark, defer_mark, fail_mark = data
    print(f"{outcome} - {pass_mark}, {defer_mark}, {fail_mark}")

#Display histogram
category_colors = {"Progress": "blue", "Trailer": "blue", "Retriever": "blue", "Exclude": "blue"}
display_histogram(progress_count, trailer_count, retriever_count, exclude_count)
# -------------------------------------------------------------------------------------------------------------------------------------#
# end of the programme
