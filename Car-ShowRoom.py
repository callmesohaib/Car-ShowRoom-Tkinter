import tkinter as tk
from tkinter import messagebox


class Car:
    def __init__(self, car_data):
        self.car_data = car_data

    def displayNames(self):
        """Return a list of car names."""
        return [name for name, _, _, _ in self.car_data]

    def displaySalePrices(self):
        """Return a list of sale prices."""
        return [price for _, price, _, _ in self.car_data]

    def displayRentPrices(self):
        """Return a list of rent prices."""
        return [rent for _, _, rent, _ in self.car_data]

    def displayAvailability(self):
        """Return a list of availability statuses."""
        return [available for _, _, _, available in self.car_data]

    def updateAvailability(self, index, new_status):
        """Update the availability status of a car."""
        self.car_data[index] = (
            self.car_data[index][0],  # name
            self.car_data[index][1],  # price
            self.car_data[index][2],  # rent
            new_status,  # new availability status
        )


class CarGUI:
    def __init__(self):
        self.filename = "./carName.txt"
        self.car = Car(read_car_data_from_file(self.filename))

        self.root = tk.Tk()
        self.root.title("Car ShowRoom")
        self.root.geometry("650x500")

        # Heading
        self.heading = tk.Label(
            self.root, text="HAQ Motors", font=("Bold", 20), bg="black", fg="white"
        )
        self.heading.grid(row=0, column=0, columnspan=4, pady=20, sticky="nsew")

        # Display the table
        self.display_table(self.root)

        # Buttons
        self.btnFrame = tk.Frame(self.root)
        self.btnFrame.grid(
            row=len(self.car.displayNames()) + 2,
            column=0,
            columnspan=4,
            pady=10,
            sticky="ew",
        )

        self.buyBtn = tk.Button(
            self.btnFrame,
            text="Buy Car",
            font=("Arial", 16),
            bg="green",
            fg="white",
            command=self.buy_car,
        )
        self.buyBtn.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        self.rentBtn = tk.Button(
            self.btnFrame,
            text="Rent Car",
            font=("Arial", 16),
            fg="black",
            bg="yellow",
            command=self.rent_car,
        )
        self.rentBtn.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        self.exitBtn = tk.Button(
            self.btnFrame,
            text="Exit",
            font=("Arial", 16),
            fg="white",
            bg="red",
            width=10,
            command=self.main_close,
        )
        self.exitBtn.grid(row=0, column=2, padx=10, pady=10, sticky="ew")

        self.root.mainloop()

    def main_close(self):
        """Close the main window."""
        self.root.destroy()

    def display_table(self, window):
        """Create and display the car data table in the given window."""

        # Clear existing widgets
        for widget in window.grid_slaves():
            if int(widget.grid_info()["row"]) > 1:
                widget.destroy()

        # Header Labels
        self.header = ["Cars", "Sale Price", "Rent Price", "Availability"]
        for col, head in enumerate(self.header):
            self.header_label = tk.Label(
                window,
                text=head,
                font=("Arial", 16, "bold"),
                bg="lightgray",
                padx=30,
                pady=5,
            )
            self.header_label.grid(row=1, column=col, sticky="nsew")

        # Data Labels
        car_names = self.car.displayNames()
        sale_prices = self.car.displaySalePrices()
        rent_prices = self.car.displayRentPrices()
        availability = self.car.displayAvailability()

        for i, (name, price, rent, available) in enumerate(
            zip(car_names, sale_prices, rent_prices, availability)
        ):
            tk.Label(window, text=name, font=("Arial", 14)).grid(
                row=i + 2, column=0, pady=5, padx=30, sticky="nsew"
            )
            tk.Label(window, text=f"${price}", font=("Arial", 14)).grid(
                row=i + 2, column=1, pady=5, padx=30, sticky="nsew"
            )
            tk.Label(window, text=f"${rent}", font=("Arial", 14)).grid(
                row=i + 2, column=2, pady=5, padx=30, sticky="nsew"
            )
            tk.Label(window, text=available, font=("Arial", 14)).grid(
                row=i + 2, column=3, pady=5, padx=30, sticky="nsew"
            )

    def buy_car(self):
        self.root.withdraw()
        self.newWindow = tk.Toplevel(self.root)
        self.newWindow.geometry("650x500")
        self.newWindow.title("Buy Car Page")
        self.newWindow.config(bg="lightblue")

        # Heading Label
        self.newLabel = tk.Label(
            self.newWindow, text="Buy Page", font=("Arial", 14), bg="black", fg="white"
        )
        self.newLabel.grid(row=0, column=0, columnspan=4, pady=20, sticky="nsew")

        # Display the table
        self.display_table(self.newWindow)

        # Input Label
        self.input = tk.Label(
            self.newWindow,
            text="Enter Car name",
            font=("Arial", 12),
            bg="black",
            fg="white",
        )
        self.input.grid(row=8, column=0, padx=10, pady=5, sticky="w")

        # Text Box
        self.textBox = tk.Text(
            self.newWindow,
            height=1,
            font=("Arial", 18),
            bg="white",
            width=20,
        )
        self.textBox.grid(
            row=8,
            column=1,
            columnspan=4,
            padx=10,
            pady=10,
            sticky="ew",
        )

        # Buttons
        self.Btn1 = tk.Button(
            self.newWindow,
            text="Buy",
            font=("Arial", 16),
            bg="green",
            fg="white",
            command=self.buy_car_confirm,
        )
        self.Btn1.grid(row=9, column=0, padx=10, pady=10, sticky="ew")

        self.Btn2 = tk.Button(
            self.newWindow,
            text="Back",
            font=("Arial", 16),
            fg="black",
            bg="red",
            command=self.mainWindow,
        )
        self.Btn2.grid(row=9, column=1, padx=10, pady=10, sticky="ew")

        self.newWindow.protocol("WM_DELETE_WINDOW", self.onclosing)

    def rent_car(self):
        self.root.withdraw()
        self.newWindow = tk.Toplevel(self.root)
        self.newWindow.geometry("650x500")
        self.newWindow.title("Rent Car Page")
        self.newWindow.config(bg="orange")

        # Heading Label
        self.newLabel = tk.Label(
            self.newWindow, text="Rent Page", font=("Arial", 14), bg="black", fg="white"
        )
        self.newLabel.grid(row=0, column=0, columnspan=4, pady=20, sticky="nsew")

        # Display the table
        self.display_table(self.newWindow)

        # Input Label
        self.input = tk.Label(
            self.newWindow,
            text="Enter Car name",
            font=("Arial", 12),
            bg="black",
            fg="white",
        )
        self.input.grid(row=8, column=0, padx=10, pady=5, sticky="w")

        # Text Box
        self.textBox = tk.Text(
            self.newWindow,
            height=1,
            font=("Arial", 18),
            bg="white",
            width=20,
        )
        self.textBox.grid(
            row=8,
            column=1,
            columnspan=4,
            padx=10,
            pady=10,
            sticky="ew",
        )
        # Input Label
        self.input = tk.Label(
            self.newWindow,
            text="Enter Hours",
            font=("Arial", 12),
            bg="black",
            fg="white",
        )
        self.input.grid(row=9, column=0, padx=10, pady=5, sticky="w")

        # Text Box
        self.textBox = tk.Text(
            self.newWindow,
            height=1,
            font=("Arial", 18),
            bg="white",
            width=20,
        )
        self.textBox.grid(
            row=9,
            column=1,
            columnspan=4,
            padx=10,
            pady=10,
            sticky="ew",
        )

        # Buttons
        self.Btn1 = tk.Button(
            self.newWindow,
            text="Rent",
            font=("Arial", 16),
            bg="green",
            fg="white",
            command=self.rent_car_confirm,
        )
        self.Btn1.grid(row=10, column=0, padx=10, pady=10, sticky="ew")

        self.Btn2 = tk.Button(
            self.newWindow,
            text="Back",
            font=("Arial", 16),
            fg="black",
            bg="red",
            command=self.mainWindow,
        )
        self.Btn2.grid(row=10, column=1, padx=10, pady=10, sticky="ew")

        self.newWindow.protocol("WM_DELETE_WINDOW", self.onclosing)

    def onclosing(self):
        self.root.destroy()
        self.newWindow.destroy()

    def mainWindow(self):
        self.newWindow.destroy()
        self.root.deiconify()
        self.update_main_window()

    def buy_car_confirm(self):
        car_names = self.car.displayNames()
        availability = self.car.displayAvailability()
        car_name = self.textBox.get("1.0", tk.END).strip()

        try:
            index = car_names.index(car_name)
            if availability[index] == "Yes":
                messagebox.showinfo(
                    "Success", f"Car '{car_name}' purchased successfully.\n"
                )
                availability[index] = "No"
                self.car.updateAvailability(index, "No")
                self.save_car_data()
                self.newWindow.destroy()
                self.root.deiconify()
                self.update_main_window()
            else:
                messagebox.showerror(
                    "Error", f"Car '{car_name}' is not available for purchase."
                )
        except ValueError:
            messagebox.showerror(
                "Error", "Car name not found. Please enter a valid car name."
            )
            self.textBox.delete("1.0", tk.END)

    def rent_car_confirm(self):
        car_names = self.car.displayNames()
        availability = self.car.displayAvailability()
        car_name = self.textBox.get("1.0", tk.END).strip()

        try:
            index = car_names.index(car_name)
            if availability[index] == "Yes":
                messagebox.showinfo(
                    "Success", f"Car '{car_name}' rented successfully.\n"
                )
                availability[index] = "No"
                self.car.updateAvailability(index, "No")
                self.save_car_data()
                self.newWindow.destroy()
                self.root.deiconify()
                self.update_main_window()
            else:
                messagebox.showerror(
                    "Error", f"Car '{car_name}' is not available for rent."
                )
        except ValueError:
            messagebox.showerror(
                "Error", "Car name not found. Please enter a valid car name."
            )
            self.textBox.delete("1.0", tk.END)

    def save_car_data(self):
        """Save the updated car data to the file."""
        car_data = list(
            zip(
                self.car.displayNames(),
                self.car.displaySalePrices(),
                self.car.displayRentPrices(),
                self.car.displayAvailability(),
            )
        )
        write_car_data_to_file(self.filename, car_data)

    def update_main_window(self):
        """Update the main window with the latest car data."""
        self.car = Car(read_car_data_from_file(self.filename))
        self.display_table(self.root)
        self.btnFrame = tk.Frame(self.root)
        self.btnFrame.grid(
            row=len(self.car.displayNames()) + 2,
            column=0,
            columnspan=4,
            pady=10,
            sticky="ew",
        )

        self.buyBtn = tk.Button(
            self.btnFrame,
            text="Buy Car",
            font=("Arial", 16),
            bg="green",
            fg="white",
            command=self.buy_car,
        )
        self.buyBtn.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        self.rentBtn = tk.Button(
            self.btnFrame,
            text="Rent Car",
            font=("Arial", 16),
            fg="black",
            bg="yellow",
            command=self.rent_car,
        )
        self.rentBtn.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        self.exitBtn = tk.Button(
            self.btnFrame,
            text="Exit",
            font=("Arial", 16),
            fg="white",
            bg="red",
            width=10,
            command=self.main_close,
        )
        self.exitBtn.grid(row=0, column=2, padx=10, pady=10, sticky="ew")


def write_car_data_to_file(filename, car_data):
    with open(filename, "w") as file:
        for name, price, rent, available in car_data:
            file.write(f"{name},{price},{rent},{available}\n")


def read_car_data_from_file(filename):
    car_data = []
    try:
        with open(filename, "r") as file:
            for line in file:
                name, price, rent, available = line.strip().split(",")
                car_data.append((name, price, rent, available))
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
    return car_data


def main():
    CarGUI()


if __name__ == "__main__":
    main()
