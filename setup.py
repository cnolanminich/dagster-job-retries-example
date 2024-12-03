from setuptools import find_packages, setup

setup(
    name="job_retries",
    packages=find_packages(exclude=["job_retries_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
