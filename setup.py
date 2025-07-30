"""
PTAN stands for PyTorch AgentNet -- reimplementation of AgentNet library for pytorch
"""
import pathlib
import setuptools

requirements = pathlib.Path("requirements.txt").read_text().splitlines()


setuptools.setup(
    name="lqtech_ptan",
    author="lqtech",
    author_email="liuqiang@lqtech.cc",
    license='GPL-v3',
    description="PyTorch reinforcement learning framework:adapt to latest pytorch",
    version="0.0.1",
    packages=setuptools.find_packages(),
    install_requires=requirements,
)
