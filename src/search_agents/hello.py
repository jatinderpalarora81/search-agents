"""Hello World module for testing the search agents project."""


class HelloWorld:
    """A simple Hello World class for testing."""

    def __init__(self, name: str = "Search Agents"):
        """Initialize the HelloWorld class.

        Args:
            name: The name to greet. Defaults to "Search Agents".
        """
        self.name = name

    def greet(self) -> str:
        """Return a greeting message.

        Returns:
            A greeting message string.
        """
        return f"Hello, {self.name}!"

    def display_info(self) -> None:
        """Display project information."""
        print(f"Project: {self.name}")
        print(f"Message: {self.greet()}")
        print("Welcome to the Search Agents project!")


if __name__ == "__main__":
    # Simple test when run directly
    greeter = HelloWorld()
    greeter.display_info()
