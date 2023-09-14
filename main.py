import luigi
from luigi import WrapperTask

from luigi_pipelines.hello_world import SayHelloWorld
from luigi_pipelines.task_dependencies import LoadData
from luigi_pipelines.dynamic_task import GetLocationWiseData


class Final(WrapperTask):
    def requires(self):
        required_tasks = [(SayHelloWorld(), 1), 
                         (LoadData(), 1),
                         (GetLocationWiseData(), 1)]
        return [i[0] for i in required_tasks if i[1] == 1]


if __name__ == '__main__':
    # Run luigi using luigid central scheduler instead of local scheduler
    # luigi.run(['LoadData'])
    luigi.run(['Final'])