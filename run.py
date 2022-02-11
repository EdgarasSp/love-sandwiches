import gspread
from google.oauth2.service_account import Credentials

# Constant variable like scope below must be written in capitals as this tells dev that this is a constant variable(will not change)

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

# where to find credentials
CREDS = Credentials.from_service_account_file('creds.json')

# these creds have scope listed in variable
SCOPED_CREDS = CREDS.with_scopes(SCOPE)

# what is authorised
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

# open spreedsheet
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

"""Below is used for testing api

# open sheet linked to variable
sales = SHEET.worksheet('sales')

# pulls all values from worksheet, this is gspread 'get_all_values' built in function
data = sales.get_all_values()

print(data)    """

def get_sales_data():
    """
    Get sales figures input from the user.
    """
    print("Please enter sales data from the last market.")
    print("Data should be six numbers, separated by commas.")
    print("Example: 10,20,30,40,50,60\n")

    data_str = input("Enter your data here: ")

    # to test entered data = print(f"The data provided is {data_str}")"

    # split string by comma delimiter, commas are removed
    sales_data = data_str.split(",")

    # this calls new function to check/validate numbers and we pass sales_data variable
    validate_data(sales_data)

    # to check print of entered values in this function = 
    print(f"Print from get_sales_data function: {sales_data}")


def validate_data(values):
    
    # this now prints entered values from not from first but second function 
    print(f"Print from validate_data function: {values}")

    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly 6 values.
    """
    try:
        # if len("instancies") in variable "Values" !=(does not equil) to 6
        if len(values) != 6:
            #raise(create error message "valueerror" used for number check if TRUE)
            raise ValueError(
                #print text and output how many instancies you actualy have in variable "values"
                f"Exactly 6 values required, you provided {len(values)}"
            )
            # if other non numeric error also TRUE
            # show(valueerror code) bit assign it to E variable
    except ValueError as e:
        #print text and show what was the error as E, \n show in a new line
        print(f"Invalid data: {e}, please try again.\n")
        
get_sales_data()

