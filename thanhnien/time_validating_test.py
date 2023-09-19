from dateutil import parser

# Example time string
time_string = '
                18/09/2023 14:50 GMT+7
            '

try:
    # Parse the time string using dateutil.parser
    parsed_time = parser.parse(time_string)
    print("Parsed Time:", parsed_time)
except ValueError:
    print("Invalid time format.")