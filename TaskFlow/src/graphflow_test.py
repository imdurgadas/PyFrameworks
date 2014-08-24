import taskflow.engines
from taskflow.patterns import graph_flow as gf
from taskflow.patterns import linear_flow as lf
from taskflow import task

class Executor(task.Task):
    def execute(self, greet, name):
        return greet + name

flow = gf.Flow('main').add(
#Linear flow
lf.Flow('linear').add(
Executor("getX1", provides='x1', rebind=['x', 'y']),
),
#Graph flow
Executor("getX3", provides='x3', rebind=['x1', 'x2']),
Executor("getX2", provides='x2', rebind=['x1', 'x4'])
)

# initial variable inputs
store = {"x": 'X',"y": 'Y',"x4": 'X4'}

#engine_conf = 'serial' will be singlethreaded
result = taskflow.engines.run(flow, engine_conf='parallel', store=store)
print("result %s" % result)