import csv

def read_csv(filename):
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)
# read_csv(input("Enter a filename: "))


def write_csv(filename, data):
    with open(filename, 'a+', newline='\n') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(data)

        csvfile.seek(0)
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)

# data =['vinay', 26, 'Satara', 40000, 'Teacher']
# write_csv('data.csv', data)


def delimeted_csv(filename, semicolon):
    with open(filename, mode='w+') as csv_file:
        writer = csv.writer(csv_file, delimiter=semicolon)
        writer.writerows(data)

        csv_file.seek(0)
        reader = csv.reader(csv_file, delimiter=semicolon)
        for row in reader:
            print(row)

data = [
    ['Name', 'Age', 'City'],
    ['Dimitri Valtteri', '30', 'New York'],
    ['Wilfrith Heilyn', '25', 'Los Angeles'],
    ['Margaid Toma', '35', 'Chicago']
]

delimeted_csv('delimeted.csv', ';')


