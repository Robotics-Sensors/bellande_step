from setuptools import setup, find_packages

with open("../../README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="bellande_step",
    version="0.3.3",
    description="Robots Step",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="RonaldsonBellande",
    author_email="ronaldsonbellande@gmail.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        "numpy",
    ],
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python",
    ],
    keywords=["package", "setuptools"],
    python_requires=">=3.0",
    extras_require={
        "dev": ["pytest", "pytest-cov[all]", "mypy", "black"],
    },
    package_data={
        'bellande_step': ['Bellande_Step'],
    },
    entry_points={
        'console_scripts': [
            'bellande_step_executable = bellande_step.bellande_step_executable:main',
            'bellande_step_api = bellande_step.bellande_step_api:main',
        ],
    },
    project_urls={
        "Home": "https://github.com/Robotics-Sensors/bellande_step",
        "Homepage": "https://github.com/Robotics-Sensors/bellande_step",
        "documentation": "https://github.com/Robotics-Sensors/bellande_step",
        "repository": "https://github.com/Robotics-Sensors/bellande_step",
    },
)
