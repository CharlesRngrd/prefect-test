import pandas as pd
from prefect import flow, task


@task(log_prints=True)
def die():
    print("Good bye world !")

@flow(log_prints=True)
def hello_world():
    print("Hello world !")
    pd.DataFrame()
    die()


if __name__ == "__main__":
    hello_world.serve(name="test-1")
