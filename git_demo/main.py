import os
from time import sleep
from dotenv import load_dotenv

load_dotenv()

##functions

def add(a:int, b:int) -> int:
    return a+b


def write_db(data:int) -> None:
    print(f"Attempting to make a connect to {os.environ.get('DATABASE_URL')} with \n \t user {os.environ.get('DATABASE_USE')} \n \t password {os.environ.get('DATABASE_PASSWORD')}")
    sleep(1)
    return

def main():
    num1 = input("Enter first number:")
    num2 = input("Enter second number:")
    result = add(num1,num2)
    write_db(result)

if __name__ == "__main__":
    main()