from setuptools import setup
import mlops_cost_optimizer

with open("README.md", 'r', encoding="utf-8") as fh:
    readme = fh.read()

setup(
    name="mlops_cost_optimizer",
    version=mlops_cost_optimizer.__version__,
    author="Jon T. Anderson",
    author_email="jontanderson@gmail.com",
    description="A MLOps Cost Optimizer Library for exploring cost scenarios based on architecture and usage decisions.",
    long_description=readme,
    long_description_content_type="text/markdown",
    license="BSD-3 License",
    url="https://github.com/jontanderson/mlops_cost_optimizer",
    python_requires=">=3.10",
    packages=["mlops_cost_optimizer"],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    install_requires=["pandas>=1.5.2", "numpy>=1.24.0"]
)