import socket

class Assignment2:
    def __init__(self, year):
        self.year = year

    def tellAge(self, currentYear):
        age = currentYear - self.year
        print(f'Your age is {age}')

    def listAnniversaries(self):
        #Current Year Assumption
        current_year = 2022
        anniversaries = [i for i in range(10, current_year - self.year + 1, 10)]
        return anniversaries

    def modifyYear(self, n):
        year_str = str(self.year)
        repeated_str = year_str[:2] * n
        odd_chars = ''.join(str(self.year * n)[::2])
        modified_str = repeated_str + odd_chars
        return modified_str

    @staticmethod
    def checkGoodString(string):
        if len(string) >= 9 and string[0].islower() and sum(c.isdigit() for c in string) == 1:
            return True
        return False

    @staticmethod
    def connectTcp(host, port):
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((host, port))
            client_socket.close()
            return True
        except Exception as e:
            return False


# Easy Change Testing Varaiables:
# Task 2 (Age)
a = Assignment2(2000)
a.tellAge(2022)

# Task 3 (List)
a = Assignment2(2000)
ret = a.listAnniversaries()
print(ret)

# Task 4 (String Manipulation)
a = Assignment2(2000)
ret = a.modifyYear(5)
print(ret)

# Task 5 (Loop and Conditional statements)
ret = Assignment2.checkGoodString("f1obar0more")
print(ret)

ret = Assignment2.checkGoodString("foobar0more")
print(ret)

# Task 6 (Socket)
retval = Assignment2.connectTcp("www.google.com", 80)
if retval:
    print("Connection established correctly")
else:
    print("Some error")
