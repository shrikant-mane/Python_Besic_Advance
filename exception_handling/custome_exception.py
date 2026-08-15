class CustomeException(Exception):
    pass

def get_customer_id(customer_id):
    if customer_id <= 0:
        raise CustomeException("Invalid customer id")
    return f"Customer id: {customer_id} found"

try:
    customer =  get_customer_id(0)
    print(customer)
except CustomeException as ex:
    print("Error:", ex)

get_customer_id(0)

