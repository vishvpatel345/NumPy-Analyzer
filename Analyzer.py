import numpy as np


class DataAnalytics:

    def __init__(self, arr=None):
        self.arr = np.array([]) if arr is None else np.array(arr)

    def input_data(self):
        print("1. 1D Array")
        print("2. 2D Array")

        choice = input("Enter choice: ")

        if choice == "1":
            a = list(map(int, input("Enter numbers: ").split()))
            self.arr = np.array(a)

        elif choice == "2":
            rows = int(input("Enter number of rows: "))
            data = []

            for i in range(rows):
                row = list(map(int, input("Enter row values: ").split()))
                data.append(row)

            if data and all(len(row) == len(data[0]) for row in data):
                self.arr = np.array(data)
            else:
                print("Please enter equal values in every row.")

        else:
            print("Invalid choice")
            return

        print("Array created successfully!")

    def display(self):
        print(self.arr)

    def statistics(self):
        print("Sum:", np.sum(self.arr))
        print("Mean:", np.mean(self.arr))
        print("Median:", np.median(self.arr))
        print("Minimum:", np.min(self.arr))
        print("Maximum:", np.max(self.arr))
        print("Variance:", np.var(self.arr))
        print("Standard Deviation:", np.std(self.arr))
        print("25th Percentile:", np.percentile(self.arr, 25))

    def sort_array(self):
        print("1. Ascending")
        print("2. Descending")

        choice = input("Enter choice: ")

        if choice == "1":
            print(np.sort(self.arr, axis=None))
        elif choice == "2":
            print(np.sort(self.arr, axis=None)[::-1])
        else:
            print("Invalid choice")

    def search(self):
        n = int(input("Enter value to search: "))
        print("Found:", np.any(self.arr == n))

    def filter_array(self):
        n = int(input("Enter threshold: "))
        print(self.arr[self.arr > n])

    def array_operations(self):
        b = np.array(list(map(int, input("Enter second array: ").split())))

        if self.arr.ndim == 1 and len(self.arr) == len(b):
            print("Addition:", self.arr + b)
            print("Subtraction:", self.arr - b)
            print("Multiplication:", self.arr * b)

            if np.all(b != 0):
                print("Division:", self.arr / b)
            else:
                print("Division not possible because the array contains zero.")

        elif self.arr.ndim == 2:
            if b.size == self.arr.shape[1]:
                print("Dot Product:", np.dot(self.arr, b))
            else:
                print("Array dimensions do not match.")

        else:
            print("Array sizes must be equal.")

    def extra_operations(self):
        print("1. Display first elements")
        print("2. Combine arrays")
        print("3. Split array")

        choice = input("Enter choice: ")

        if choice == "1":
            print(self.arr[..., :2])

        elif choice == "2":
            b = np.array(list(map(int, input("Enter numbers: ").split())))
            print(np.concatenate((self.arr.ravel(), b)))

        elif choice == "3":
            print(np.array_split(self.arr, 2))

        else:
            print("Invalid choice")

    @staticmethod
    def correlation(a, b):
        if len(a) == len(b) and len(a) > 1:
            return np.corrcoef(a, b)[0, 1]
        return "Arrays must have equal lengths greater than one."

    @classmethod
    def information(cls):
        print("NumPy Analyzer - Array Analysis Tool")


def main():
    obj = DataAnalytics()

    while True:
        print("\n--- NumPy Analyzer ---")
        print("1. Input Array")
        print("2. Display Array")
        print("3. Statistics")
        print("4. Sort Array")
        print("5. Search")
        print("6. Filter")
        print("7. Array Operations")
        print("8. Extra Operations")
        print("9. Project Information")
        print("10. Correlation")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            obj.input_data()

        elif choice == "2":
            obj.display()

        elif choice == "3":
            if obj.arr.size > 0:
                obj.statistics()
            else:
                print("Enter data first")

        elif choice == "4":
            if obj.arr.size > 0:
                obj.sort_array()
            else:
                print("Enter data first")

        elif choice == "5":
            if obj.arr.size > 0:
                obj.search()
            else:
                print("Enter data first")

        elif choice == "6":
            if obj.arr.size > 0:
                obj.filter_array()
            else:
                print("Enter data first")

        elif choice == "7":
            if obj.arr.size > 0:
                obj.array_operations()
            else:
                print("Enter data first")

        elif choice == "8":
            if obj.arr.size > 0:
                obj.extra_operations()
            else:
                print("Enter data first")

        elif choice == "9":
            DataAnalytics.information()

        elif choice == "10":
            a = list(map(float, input("Enter first array: ").split()))
            b = list(map(float, input("Enter second array: ").split()))
            print("Correlation:", DataAnalytics.correlation(a, b))

        elif choice == "11":
            print("Thank you for using NumPy Analyzer!")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()