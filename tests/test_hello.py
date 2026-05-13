"""Tests for the hello module."""

import sys
from pathlib import Path

# Add src directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from search_agents.hello import HelloWorld


def test_hello_world_default():
    """Test HelloWorld with default name."""
    greeter = HelloWorld()
    assert greeter.name == "Search Agents"
    assert greeter.greet() == "Hello, Search Agents!"


def test_hello_world_custom_name():
    """Test HelloWorld with custom name."""
    greeter = HelloWorld("Python")
    assert greeter.name == "Python"
    assert greeter.greet() == "Hello, Python!"


if __name__ == "__main__":
    test_hello_world_default()
    test_hello_world_custom_name()
    print("All tests passed!")
