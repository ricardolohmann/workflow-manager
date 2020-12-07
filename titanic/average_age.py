import prefect
from prefect import task, Flow

import pandas as pd


@task
def read_data(file_location: str) -> pd.DataFrame:
    df = pd.read_csv(file_location)
    return df


@task
def compute_average_age(df: pd.DataFrame) -> None:
    average = df["Age"].mean()
    logger = prefect.context.get("logger")
    logger.info(f"Average age is: {average}")


@task
def display_dataframe(df: pd.DataFrame) -> None:
    logger = prefect.context.get("logger")
    logger.info(df)


with Flow("Titanic") as flow:
    url = "https://raw.githubusercontent.com/A3Data/hermione/master/hermione/file_text/train.csv"
    df = read_data(url)
    compute_average_age(df)
    display_dataframe(df)

flow.register(project_name="Titanic", idempotency_key=flow.serialized_hash())
