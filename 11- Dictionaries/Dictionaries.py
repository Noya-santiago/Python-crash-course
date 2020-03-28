""" Isn't that hard. Its just a conversion of strings """

month_conversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March"
}
print(month_conversions.get("Luv", "Not a valid key")) 
print(month_conversions.get("Mar", "Not a valid key"))