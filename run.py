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


# open sheet linked to variable
sales = SHEET.worksheet('sales')

# pulls all values from worksheet, this is gspread 'get_all_values' built in function
data = sales.get_all_values()

print(data)
