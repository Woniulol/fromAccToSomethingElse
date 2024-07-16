from fx.command import Command
from customer_service import CustomerService

class AddCustomerCommand(Command):
    def __init__(self, service: CustomerService) -> None:
        self._service = service

    def execute(self):
        self._service.add_customer()