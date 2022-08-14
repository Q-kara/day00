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
    first_name=input("Insert your first name \n")
    numbers=containsNumber(first_name)
    if numbers is True :
        print("Invalid first name")
        first_name=input("Please try again\n")
    
    last_name= input("Insert  your last name\n")
    numbers2=containsNumber(last_name)
    if numbers2 is True:
        print("Invalid last name")
        last_name=input("Please try again \n")


def create_user_name(first_name, last_name, cohort, final_campus):
    """
    Create and return a valid username
    """
    first_name=input("Insert your first name \n")
    numbers=containsNumber(first_name)
    if numbers is True :
        print("Invalid first name")
        first_name=input("Please try again\n")
    
    last_name= input("Insert  your last name\n")
    numbers2=containsNumber(last_name)
    if numbers2 is True:
        print("Invalid last name")
        last_name=input("Please try again \n")

    fnamelen=len(first_name)
    lnamelen=len(last_name)

    if fnamelen < 3:
        first_name=first_name+"o"
    if lnamelen < 3:
        last_name=last_name+"o"

    usefname = first_name[-3:]
    uselname =last_name[:3]

def user_campus(campus):
    """
    Return valid campus abbreviations
    """
    campuses=["Durban", "Johannesburg" ,"Cape Town", "Phokeng"]

if __name__ == '__main__':
    user_details()
    