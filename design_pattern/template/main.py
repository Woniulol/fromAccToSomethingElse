# all the operations should be registered with an audit trail system
from task import GenerateReportTask, TransferMoneyTask
from audit_trail import AuditTrail

if __name__ == '__main__':
    # this audit trail is likely to be a duplicate operation, so that you may instantiate within the Task class

    audit_trail_2 = AuditTrail()

    task1 = GenerateReportTask()
    task1.execute()

    task2 = TransferMoneyTask(audit_trail=audit_trail_2)
    task2.execute()

