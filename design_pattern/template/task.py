from abc import ABC, abstractmethod
from audit_trail import AuditTrail

class Task(ABC):
    def __init__(self, audit_trail: AuditTrail = AuditTrail()):
        self.audit_trail = audit_trail

    @abstractmethod
    def _do_execute(self):
        ...

    def execute(self):
        self.audit_trail.record()
        self._do_execute()

class TransferMoneyTask(Task):
    # Here, no init method is provided, so it will call the init method of the parent class, which is AuditTrail()
    # Thus, if we provide a audit_trail parameter in the constructor of TransferMoneyTask, it will override the audit_trail parameter of the parent class.
    def _do_execute(self):
        print("Transfer money from account A to account B")

class GenerateReportTask(Task):
    def _do_execute(self):
        print("Generate report for account A")
