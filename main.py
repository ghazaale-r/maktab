import logging

name = "project"
logger = logging.getLogger("log in")
logging.basicConfig(level=logging.DEBUG,
                    filename='app.log',
                    format="'%(asctime)s - %(name)s - %(levelname)s - %(message)s' \n",
                    datefmt='%d-%b-%y %H:%M:%S')
logging.debug('This is a debug message')
print("hello world")


def fact(n):
    return 1 if (n == 1 or n == 0) else n * fact(n - 1);


num = 5
print(f"Factorial of {num} is {fact(num)}")

print("factorial of n ")