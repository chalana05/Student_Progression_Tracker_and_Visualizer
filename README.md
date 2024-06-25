## Student Progression System

This Python program allows staff to record and categorize student progress based on their credit marks in three categories: PASS, DEFER, and FAIL. The program ensures input validation, stores progression data, and visualizes the results using a histogram.

Features

1. Input Validation: Ensures the credit marks are within the valid range (0 to 120, increments of 20) and their total equals 120.

2. Progression Categories:

      • Progress: PASS credits = 120

      • Progress (module trailer): PASS credits = 100

      • Module retriever: PASS credits < 100 and FAIL credits < 80

      • Exclude: FAIL credits ≥ 80


3. Data Storage: Saves the progression data to a text file.

4. Data Retrieval: Prints stored progression data from the text file.

5. Visualization: Displays a histogram showing the count of students in each progression category.


Usage

1. Running the Program:

    • The program will prompt for PASS, DEFER, and FAIL credit inputs.

    • Input validation checks will ensure the entered values are correct.

    • Based on the input, the student will be categorized into one of the progression categories.

    • The program will ask if you want to enter another set of data or quit to view results.

2. Storing Data:

    • Upon exiting, the program saves the entered progression data to progression_data.txt.

3. Displaying Histogram:

    • The program visualizes the data using a histogram, displaying the count of students in each category.


Example

    Please enter PASS credit    : 100
    Please enter DEFER credit   : 20
    Please enter FAIL credit    : 0
    Progress (module trailer)

    Would you like to enter another set of data?
    Enter 'y' for yes or 'q' to quit and view results: q


Code Structure

⦿ Functions:

   • draw_bar(): Draws a bar in the histogram for a given category.

   • display_histogram(): Creates and displays the histogram.

   • range_check_for_staff_version(): Validates input range.

   • save_progression_data(): Saves progression data to a file.

   • print_stored_data(): Prints stored progression data from the file.
 
⦿ Main Logic:

  • Validates user input.

  • Categorizes the student based on input credits.

  • Updates counts for each category.

  • Saves and displays data as required.

⦿ Visualization
<br>
The histogram displays the counts of each category with the following color coding:

  • Progress: Blue

  • Trailer: Blue

  • Retriever: Blue

  • Exclude: Blue

This program helps staff efficiently manage and visualize student progression data.











































   
