__author__ = 'durgadas_kamath'

import taskflow.engines
from taskflow.patterns import linear_flow as lf
from taskflow import task

'''
This example demonstrates Linear workflow using taskflow .
In addition , it also demonstrates the REVERT functionality.
'''

class WorkflowClass1(task.Task):
    def execute(self, wkf1, *args, **kwargs):
        print("Executed : ", wkf1)

    def revert(self, wkf1, *args, **kwargs):
        print("Reverting : ", wkf1)


class WorkflowClass2(task.Task):
    def execute(self, wkf2, *args, **kwargs):
        print("Executed : ", wkf2)

    def revert(self, wkf2, *args, **kwargs):
        print("Reverting : ", wkf2)


class WorkflowClass3(task.Task):
    def execute(self,wkf3, *args, **kwargs):
        raise Exception

    def revert(self, wkf3, *args, **kwargs):
        print("Reverting : ", wkf3)


def flow_watch(state, details):
    print('Flow State: {}'.format(state))
    print('Flow Details: {}'.format(details))


def task_watch(state, details):
    print('Task State: {}'.format(state))
    print('Task Details: {}'.format(details))


flow = lf.Flow('WorkflowEx')
flow.add(WorkflowClass1())
flow.add(WorkflowClass2())
flow.add(WorkflowClass3())

engine = taskflow.engines.load(flow, store=dict(wkf1='workflow_task_1', wkf2='workflow_task_2', wkf3='workflow_task_3'))
engine.notifier.register('*', flow_watch)
engine.task_notifier.register('*', task_watch)

try:
    engine.run()
except Exception as ex:
    print(ex.message)
