class Person:
    age = 0
    addr = ""
    SSN = ""

John = Person()
John.age = int(input("Age Input: "))
John.addr = input("Addr Input: ")
John.SSN = input("SSN Input: ")
print("John Age:", John.age)
print("John Addr:", John.addr)
print("John Name:", John.SSN)
print()

James = Person()
James.age = int(input("Age Input: "))
James.addr = input("Addr Input: ")
James.SSN = input("SSN Input: ")
print("James Age:", James.age)
print("James Addr:", James.addr)

#수정
#print("James Name:", James.SSN)
