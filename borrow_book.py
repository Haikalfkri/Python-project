import csv
import datetime
import matplotlib.pyplot as plt


def book_list():
    return {
        1: {'title': 'Cinderella', 'genre': 'Romance', 'amount': 8},
        2: {'title': 'Transformers', 'genre': 'Action, Robot', 'amount': 10},
        3: {'title': 'Bumblebee', 'genre': 'Action, Robot', 'amount': 8},
        4: {'title': 'You are the apple of my eye', 'genre': 'Romance', 'amount': 12},
        5: {'title': 'Superman','genre': 'Action','amount': 10},
    }


def generate_csv(name, bookNumber, amount, date):
    filename = "book_history.csv"
    data = [name, bookNumber, amount, date]
    with open(filename, 'a', newline='') as file:
        csvwriter = csv.writer(file)
        csvwriter.writerow(data)


def generate_graph():
    x = []
    y = []
    
    with open('book_history.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            x.append(f"book {row[1]}")
            y.append(int(row[2]))

    plt.bar(x, y, color = 'g', width = 0.5)
    plt.xlabel("Book Number")
    plt.ylabel("Amount")
    plt.title("Book Amount")
    plt.legend()
    plt.show()

def main():
    book_dict = book_list()
    
    for key, value in book_dict.items():
        print(f"{key}, title: {value['title']}, genre: {value['genre']}, amount: {value['amount']}")

    print("If you want to borrow book, please choose the number of the book and the amount!!")
    name = input("Enter your name: ")
    bookNumber = int(input("Enter book number: "))
    bookAmount = int(input("Enter book amount: "))
    date_entry = input("Enter borrowing date in format YYYY-MM-DD format: ")
    year, month, day = map(int, date_entry.split("-"))
    date = datetime.date(year, month, day)
    
    if bookNumber in book_dict and bookAmount > 0 and bookAmount <= book_dict[bookNumber]['amount']:
        generate_csv(name, bookNumber, bookAmount, date)
        book_dict[bookNumber]['amount'] -= bookAmount
        print("Success")
    else:
        print("Please enter valid book amount and book number")


if __name__ == "__main__":
    # main()
    generate_graph()