import pickle

f = open("employee.dat", "rb")
print("Details")

while True:
    try:
        employee = pickle.load(f)
        employee.display()
    except EOFError:
        print("All employee data displayed successfully")
        break


