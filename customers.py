"""Customers at Hackbright."""


class Customer:
    """Ubermelon customer."""

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def __repr__(self):
        return f"<customer: {self.first_name}, {self.email}, {self.password}"

def read_customers_from_file(filepath):
    customers_dict = {}
    
    with open(filepath) as file:
        for line in file:
            (
                first_name,
                last_name,
                email,
                password
            ) = line.strip().split("|")
            customers_dict[email] = Customer(first_name, last_name, email, password)
    
    return customers_dict

def get_by_email(email):
    return customers.get(email, 0)

customers = read_customers_from_file("customers.txt")