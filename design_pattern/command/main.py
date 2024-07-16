from customer_service import CustomerService
from add_customer_command import AddCustomerCommand
from black_white_command import BlackWhiteCommand
from composite_command import CompositeCommand
from resize_command import ResizeCommand
from fx.button import Button

if __name__ == '__main__':
    customer_service = CustomerService()
    command = AddCustomerCommand(customer_service)
    button = Button('Add Customer', command)
    button.click()

    composite_command = CompositeCommand()
    composite_command.add(ResizeCommand())
    composite_command.add(BlackWhiteCommand())
    button = Button('Composite Command', composite_command)
    button.click()

