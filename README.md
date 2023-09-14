# learn_luigi

## Ref:
    1. Luigi ReadTheDocs: https://luigi.readthedocs.io/en/stable/

## Setup the Luigi Env (using WSL2 terminal instead of powershell)
1. Python env setup(WSL2):
    ```shell
    python3 -m virtualenv .venv
    source .venv/bin/activate
    ```
2. Python env setup(Poweshell):
    ```shell
    py -m virtualenv .venv
    Set-ExecutionPolicy Unrestricted -Scope Process
    .venv\\Scripts\\activate
    ```
3. Install Python packages:
    ```shell
    pip install -r requirements.txt
    ```
4. Execute the Luigi sample pipelines (*using local scheduler*)
    ```shell
    python luigi_pipelines/hello_world.py
    python luigi_pipelines/task_dependencies.py
    ```
5. Run Luigi webserver in different powershell terminal (*luigid central scheduler*)
    ```shell
    # open "http://localhost:8082" or "http://localhost:8082/static/visualiser/index.html"
    luigid
    ```
6. After hosting luigid central scheduler, execute main.py
    ```shell
    python main.py
    # or, execute individual luigi pipeline withouth local scheduler
    ```

## Learn Luigi (step by step)
1. Workflow Management Tool

### Step 1: Luigi Building Blocks -

| Id | Name | Description | Remarks |
| :--- | :---: | --- | --- |
| 1. | `Task` | 1. Is about Doing Something - means doing procession <br>2. Units of work in the pipeline <br>3. Can require other tasks <br>4. Task will complete only if its target exists <br>5. <u>**Characteristics of Luigi Tasks**</u> are "Identifiable - (unique taskid)", "Atomic - Basic Unit of target exists or not", "Idempotent - Runs again, same result"  | |
| 2. | `Target` | 1. Once Task complete, its generate Target (Example: generation of file) <br>2. Processing Checkpoints (Example: Disk file, S3 File, Database Entry) | |
| 3. | `Wrapper Task` | 1. Special type of luigi task <br>2. Its only has "requires()" method <br>3. Has no targets, no business logic | |
| 4. | `Parameter` | 1. Pass parameter to a task | |
| | | | |

### Step 2: Key Methods of a Task -
1. Any luigi Task Class needs to inherit `luigi.Task`

| Id | Name | Description | Remarks |
| :--- | :---: | --- | --- |
| 1. | `output()` | 1. Specify Target | |
| 2. | `run()` | 1. Specify business logic | |
| 3. | `requires()` | 1. Specify Dependencies | | 
| 4. | `complete()` | Instead of using `output()` for target, you can use `complete()` | |
| | | | |

### Step 3: Using luigi Configuration -

| Id | Name | Description | Remarks |
| :--- | :---: | --- | --- |
| | | | |
### Sample Luigi Code Snippets
1. [hello_world.py](luigi_pipelines\hello_world.py): basic sample luigi task
2. [task_dependencies.py](luigi_pipelines\task_dependencies.py): Get Task Dependencies exaples