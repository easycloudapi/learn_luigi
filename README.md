# learn_luigi

## Ref:
    1. Luigi ReadTheDocs: https://luigi.readthedocs.io/en/stable/

## Setup the Luigi Env (using WSL2 terminal instead of powershell)
1. Python env setup:
    ```shell
    python3 -m virtualenv .venv
    source .venv/bin/activate
    ```
2. Install Python packages:
    ```shell
    pip install -r requirements.txt
    ```
3. Run Luigi webserver
    ```shell
    # open "http://localhost:8082" or "http://localhost:8082/static/visualiser/index.html"
    luigid
    ```

## Learn Luigi (step by step)
1. Workflow Management Tool

### Step 1: Luigi Building Blocks -

| Id | Name | Description | Remarks |
| :--- | :---: | --- | --- |
| 1. | `Task` | 1. Is about Doing Something - means doing procession <br>2. Units of work in the pipeline <br>3. Can require other tasks <br>4. Task will complete only if its target exists  | |
| 2. | `Target` | 1. Once Task complete, its generate Target (Example: generation of file) <br>2. Processing Checkpoints (Example: Disk file, S3 File, Database Entry) | |
| | | | |

### Step 2: Key Methods of a Task -
1. Any luigi Task Class needs to inherit `luigi.Task`

| Id | Name | Description | Remarks |
| :--- | :---: | --- | --- |
| 1. | `output()` | 1. Specify Target | |
| 2. | `run()` | 1. Specify business logic | |
| 3. | `requires()` | 1. Specify Dependencies | |
| | | | |

### Sample Luigi Code Snippets
1. [hello_world.py](luigi_pipelines\hello_world.py): basic sample luigi task
2. [task_dependencies.py](luigi_pipelines\task_dependencies.py): Get Task Dependencies exaples