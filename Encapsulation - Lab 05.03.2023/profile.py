class Profile:
    def __init__(self, username: str, password: str, ):
        self.username = username
        self.password = password

    @property
    def username(self):             # after we validate and SET, value goes to GETTER in order to return be returned
        return self.__username

    @username.setter
    def username(self, value):          # first we VALIDATE the username, through a SETTER
        if not 5 <= len(value) <= 15:
            raise ValueError("The username must be between 5 and 15 characters.")
        self.__username = value

    @property
    def password(self):                 # same process for the password
        return self.__password

    @password.setter            # REMEMBER: first VALIDATE than the returned value will be passed to the GETTER !
    def password(self, value):
        if len(value) < 8 or not any(c.isdigit() for c in value) or not any(c.isalpha() and c.isupper() for c in value):
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        self.__password = value

    def __str__(self):
        return f'You have a profile with username: "{self.__username}" and password: {"*" * len(self.__password)}'


correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)