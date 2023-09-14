import luigi
from luigi import Task, LocalTarget
import pandas as pd
import json


class GetEmpNames(Task):
    def output(self):
        return LocalTarget('sample_data/sample_names.json')
    
    def run(self):
        with self.output().open('w') as f:
            print('{"empdata": [{"id": 1, "name": "Indra"},  \
                   {"id": 2, "name": "Vikram"},  \
                   {"id": 3, "name": "Pravin"}]}', file=f)
    
        
class GetEmpLocations(Task):    
    def output(self):
        return LocalTarget('sample_data/sample_locations.json')
    
    def run(self):        
        with self.output().open('w') as f:
            print('{"locdata": [{"id": 1, "location": "Kolkata"},  \
                   {"id": 2, "location": "Pune"},  \
                   {"id": 3, "location": "Pune"}]}', file=f)
            

class LoadData(Task):
    def requires(self):
        return [GetEmpNames(), 
                GetEmpLocations()]
    
    def output(self):
        return LocalTarget('sample_data/sample_loaddata.csv')
    
    def run(self):
        with self.input()[0].open('r') as f:
            output_emp_data = json.load(f)
        df_emp = pd.DataFrame(output_emp_data.get('empdata'))
        
        with self.input()[1].open('r') as f:
            output_loc_data = json.load(f)
        df_loc = pd.DataFrame(output_loc_data.get('locdata'))
        
        df = pd.merge(df_emp, df_loc, on="id", how="inner")
        df.to_csv(self.output().path, header=True, index=False)

 
if __name__ == '__main__':
    # python luigi_pipelines/task_dependencies.py
    luigi.run(['LoadData', '--local-scheduler']) 