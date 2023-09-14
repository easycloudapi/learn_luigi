import luigi
from luigi import Task, LocalTarget
import pandas as pd
import json


class GetData(Task):
    def output(self):
        return LocalTarget('sample_1.json')
    
    def run(self):
        with self.output().open('w') as f:
            print('{"data": [{"id": 1, "name": "Indra"}, {"id": 2, "name": "Vikram"}]}', file=f)
            

class StoreData(Task):
    def requires(self):
        return GetData()
    
    def output(self):
        return LocalTarget('sample_1.csv')
    
    def run(self):
        with self.input().open('r') as f:
            output_data = json.load(f)
        df = pd.DataFrame(output_data.get('data'))
        df.to_csv(self.output().path, header=True, index=False)

 
if __name__ == '__main__':
    # python3 luigi_pipelines/task_dependencies.py
    luigi.run(['StoreData', '--local-scheduler']) 