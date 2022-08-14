from xml.dom import UserDataHandler
 
def containsNumber(value):
    for character in value:
        if character.isdigit():
            return True
    return False

def user_details():
    """
    Prompt user input
    """
    while True:
        numbers = False
        first_name = input("Insert your first name\n")
        numbers = containsNumber(first_name)
        if(numbers or first_name == ""):
            print("Invalid first name")
            continue
        break

    while True:
        numbers = False
        last_name = input("Insert your last name\n")
        numbers = containsNumber(last_name)
        if (numbers or last_name == ""):
            print("Invalid last name")
            continue
        break

    while True:
        numbers = False
        cohort = input("Insert your cohort\n")
        numbers = containsNumber(last_name)
        if (numbers or cohort == "" or len(cohort) != 4):
            print("Invalid cohort")
            continue
        break

    valid_campuses = ["johannesburg", "cape town", "durban", "phokeng"]
    while True:
        campus = input("Insert the campus you will be attending in\n")
        if (campus.lower() not in valid_campuses or campus == ""):
            print("Invalid campus")
            continue
        break

    print(create_user_name(first_name, last_name, cohort, campus))


def create_user_name(first_name, last_name, cohort, final_campus):
    """
    Create and return a valid username
    """
    fnamelen=len(first_name)
    lnamelen=len(last_name)

    if fnamelen < 3:
        if fnamelen == 1:
            first_name = first_name + "o"
        first_name=first_name+"o"
    if lnamelen < 3:
        if lnamelen == 1:
            last_name = last_name + "o"
        last_name=last_name+"o"

    usefname = first_name[-3:].lower()
    uselname =last_name[:3].lower()

    campus = user_campus(final_campus)

    return usefname+uselname+cohort+campus

def user_campus(campus):
    """
    Return valid campus abbreviations
    """
    campus = campus.lower()
    campuses = {"durban":"DBN", "johannesburg":"JHB", "cape town":"CPT", "phokeng":"PHO"}
    return campuses[campus]

if __name__ == '__main__':
    user_details()
    