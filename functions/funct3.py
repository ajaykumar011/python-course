def age_count(x):
    if int(x) > 1980 and int(x) < 2020:
        age = 2020 - int(x)
        return str(age)
    return 'Invalid'

birth_year=input("Enter your birth year: ")
print("Your age is " + age_count(birth_year))