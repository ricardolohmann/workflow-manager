# my-workflow-manager

## Install

```shell
pip install requirements.txt
```

## Running

Configure Prefect for local orchestration, and save the configuration in local `~/.prefect` directory.

```shell
prefect backend server
```

Start the server, UI, and all required infrastructure.

```shell
prefect server start
```

Once all components are running, you can view the UI by opening a browser and visiting http://localhost:8080.

Please note that executing flows from the server requires at least one Prefect Agent to be running.
So, we'll start one in other terminal with the following command:

```shell
prefect agent local start
```

Create the project:

```shell
prefect create project "Titanic"
```

Run the workflow:

```shell
python titanic/average_age.py
```
