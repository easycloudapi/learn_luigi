import luigi
import logging

logger = logging.getLogger('SayHelloWorld')


class SayHelloWorld(luigi.Task):
    def output(self):
        return luigi.LocalTarget('sample_report.csv')
    
    def run(self):
        out = 'Hello World'
        print(out)
        logger.info(out)  # logger is not working currently
        print('Indranil Pal')
        
        with self.output().open('w') as file:
            file.write(out)
            

if __name__ == '__main__':
    # python3 luigi_pipelines/hello_world.py
    luigi.run(['SayHelloWorld', '--local-scheduler'])
