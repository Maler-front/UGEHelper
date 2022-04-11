import sys

sys.path.append('/1st task')
import FirstTaskFactory

factory = FirstTaskFactory()
task = factory.newTask()
task.displayTask()
input("smth")
task.displayAnswer()
