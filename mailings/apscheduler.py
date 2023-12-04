
from mailings.management.commands.send_mails import Command

def job_function():
    Command.handle(Command())
