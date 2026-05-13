"""Setup configuration for Search Agents project."""

from setuptools import setup, find_packages

setup(
    name="search-agents",
    version="0.1.0",
    description="A Python project to create search agents",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/search-agents",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.8",
    install_requires=[],
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
            "black>=23.12.0",
            "flake8>=6.1.0",
            "mypy>=1.7.0",
        ]
    },
)
