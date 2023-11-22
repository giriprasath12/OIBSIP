import random
import string
def generate_password(length=12):

    characters = string.ascii_letters + string.digits + string.punctuation

    password = [random.choice(string.ascii_uppercase),
                random.choice(string.ascii_lowercase),
                random.choice(string.digits),
                random.choice(string.punctuation)]

    for _ in range(length - 4):
        password.append(random.choice(characters))

    random.shuffle(password)

    password_str = ''.join(password)

    return password_str

def main():

    password_length = int(input("Enter the desired length of the password: "))

    password = generate_password(password_length)
    print(f"Random Password: {password}")

if __name__ == "__main__":
    main()
