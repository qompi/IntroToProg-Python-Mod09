# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# ACompeau, 12.4.19, Modified code to complete assignment 9
# ------------------------------------------------------------------------ #

if __name__ == "__main__":
    from DataClasses import Employee as Emp
    from ProcessingClasses import FileProcessor as Fp
    from IOClasses import EmployeeIO as Eio
else:
    raise Exception("This file was not created to be imported")


# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body
# Load data from file into a list of employee objects when script starts
lstFileData = []
lstEmployeeTable = []
fileName = "EmployeeData.txt"
lstFileData = Fp.read_data_from_file(fileName)
for row in lstFileData:
    lstEmployeeTable.append(Emp(row[0], row[1], row[2].strip()))


while True:

    # Show user a menu of options
    Eio.print_menu_items()

    # '''
    #         Menu of Options
    #         1) Show current employee data
    #         2) Add new employee data.
    #         3) Save employee data to File
    #         4) Exit program
    #         '''
    # Get user's menu option choice
    choice = Eio.input_menu_options()

    # Show user current data in the list of employee objects
    if choice == '1':
        Eio.print_current_list_items(lstEmployeeTable)
        continue

    # Let user add data to the list of employee objects
    elif choice == '2':
        employee_input = Eio.input_employee_data()
        lstEmployeeTable.append(employee_input)
        print(employee_input, "\nThis entry has been added to the list!\n\n")

        continue

    # let user save current data to file
    elif choice == '3':
        Fp.save_data_to_file(fileName, lstEmployeeTable)
        print("Your data was saved to: " + fileName)
        continue

    # Let user exit program
    elif choice == '4':
        break

    # If not 1-4
    else:
        print("<Please enter a number between [1,4]>")
        continue

# Main Body of Script  ---------------------------------------------------- #
