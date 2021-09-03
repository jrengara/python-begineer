monthConversion = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May"
}

print(monthConversion["Jan"])
print(monthConversion.get("Jan"))

print(monthConversion.get("Luv", "not a valid key"))
