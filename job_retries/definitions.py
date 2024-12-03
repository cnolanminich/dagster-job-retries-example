import dagster as dg

@dg.op()
def always_fail():
    raise Exception("Always fail")

@dg.job(tags={"dagster/max_retries": 3})
def sample_job():
    always_fail()


@dg.job(tags={"dagster/max_retries": 3, "dagster/retry_strategy": "ALL_STEPS"})
def other_sample_sample_job():
    pass



defs = dg.Definitions(
    jobs=[sample_job, other_sample_sample_job]
)
