"""Example module that greets a person by name."""


def greet(name: str) -> None:
    """Print a greeting for the given name.

    Args:
        name: The name of the person to greet.
    """
    message = f"Hello, {name}"
    print(message)


if __name__ == "__main__":
    greet("Claude")
