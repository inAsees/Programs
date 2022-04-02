import random
import string
import os
import csv


class PasswordGenerator:
    def __init__(self):
        self._create_directory()
        self._load_from_file()
        self._dic = {}
        self._minimum_length = 4

    def generate_password(self, password_usage: str, password_length: int) -> str:
        password = ""
        if password_length == 0:
            password_length = 12
        for i in range(password_length):
            password += random.choice(string.ascii_letters + string.punctuation + string.digits)
        self._dic[password_usage] = password
        return password

    def save(self) -> None:
        with open(r"C:\Users\DELL\Desktop\my_passwords_repository\passwords_list.csv",
                  "w", newline="") as f:
            writer = csv.writer(f)
            for domain in self._dic:
                writer.writerow([domain, self._dic[domain]])

    def get_minimum_length(self) -> int:
        return self._minimum_length

    def _load_from_file(self) -> None:
        with open(r"C:\Users\DELL\Desktop\my_passwords_repository\passwords_list.csv",
                  "r") as f:
            reader = csv.reader(f)
            for rows in reader:
                self._dic[rows[0]] = rows[1]

    def _create_directory(self) -> None:
        if "my_passwords_repository" not in os.listdir(r'C:\Users\DELL\Desktop'):
            os.mkdir(r"C:\Users\DELL\Desktop\my_passwords_repository")
            with open(r"C:\Users\DELL\Desktop\my_passwords_repository\passwords_list.csv",
                      "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["Domain Name", "Password"])


class CliHandler:
    def start(self):
        password_gen = PasswordGenerator()
        password_usage = input("Password Generator Application.\n"
                               "Where are you going to use this password? "
                               "Example:Facebook,Instagram etc.\n")
        while True:
            user_input = input(
                f"Do you want to provide maximum length for the password?\n"
                f"Make sure to provide minimum length of {password_gen.get_minimum_length()} characters.\n"
                "If YES press '1'.\n"
                "If NO press '2'.\n")
            if user_input == "1":
                while True:
                    try:
                        password_length = int(input("Please provide the maximum length of the password:"))
                    except ValueError as e:
                        print("Invalid input")
                        continue

                    if password_length < password_gen.get_minimum_length():
                        print(f"This is less than {password_gen.get_minimum_length()},try again.")
                        continue
                    print(f"Password is: {password_gen.generate_password(password_usage, password_length)}")
                    break
                break

            elif user_input == "2":
                print(f"Password is: {password_gen.generate_password(password_usage, password_length=0)}")
                break
            else:
                print("Invalid input")
                continue
        print("Do you want to save the password?\n"
              "If YES press 1\n"
              "If NO press 2\n")
        user_input = input()
        if user_input == "1":
            password_gen.save()
            print("Password saved successfully")
        elif user_input == "2":
            print("Password not saved.")


if __name__ == "__main__":
    CliHandler().start()
