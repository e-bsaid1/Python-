class User:
    """Greet the user"""
    
    def __init__(self,first_name,last_name, age, mail):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.mail = mail
        self.login_attempts = 0
        
    def describe_user(self):
        print(" Summary :")
        print(f"\nFirst name : {self.first_name.title()}")
        print(f"\nLast name : {self.last_name.title()}")
        print(f"\nAge: {self.age} years old")
        print(f"\nMail: {self.mail}")
        
    def greet_user(self):
        print(
        f"Hello {self.first_name.title()} {self.last_name.title()} !")
        
    def increment_login_attempts(self, i):
        self.login_attempts += i
        print(f"Login attempts : {self.login_attempts}")
    
    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f"Login attempts : {self.login_attempts}")

            

class Admin(User):
    
    def __init__(self,first_name,last_name, age, mail):
        super().__init__(first_name,last_name, age, mail)
        self.privileges = Privilege()
        
class Privilege():
    
    def __init__(self, privilege = []):
        self.privilege = privilege
        
        
    def show_privileges(self):
        print(f"List of privilege:")
        if self.privilege:
            for privilege in self.privilege:
                print(f"- {privilege}")    
        else:
            print("- This user has no privileges")        