from prefect import flow


if __name__ == "__main__":
   flow.from_source(
       source="https://github.com/CharlesRngrd/prefect-test.git",
       entrypoint="example_simple/flow.py:hello_world"
   ).deploy(
       name="my-deployment",
       work_pool_name="worker-1",
   )
