import os
import luigi
import pandas as pd
from luigi import Task, LocalTarget, Parameter

from luigi_pipelines.task_dependencies import LoadData


class CreateDynamicTask(Task):
    location = Parameter()
    
    def output(self):
        path = os.path.join("sample_data", self.location + "_empdata.csv")
        return LocalTarget(path)
    
    def run(self):
        with open('sample_data\\sample_loaddata.csv', 'r') as f:
            with self.output().open('w') as out:
                for line in f:
                    if self.location in line:
                        out.write(line)
                        

class GetLocationWiseData(Task):
    status = False
    
    def requires(self):
        return LoadData()
    
    def complete(self):
        return self.status
    
    def run(self):
        df = pd.read_csv('sample_data\\sample_loaddata.csv')
        for i in df['location'].unique():
            target = yield CreateDynamicTask(i)
        self.status = True
        

if __name__ == '__main__':
    luigi.run(['GetLocationWiseData'])