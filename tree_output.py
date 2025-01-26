#!/usr/bin/env python3
import subprocess
import sys


def get_tree_output(output_file):
    try:
        # Run tree command with better formatting options
        result = subprocess.run(
            [
                "tree",
                "--charset",
                "ascii",  # Use ASCII characters
                "-I",
                "__pycache__",  # Ignore pycache directories
                "-I",
                "*.pyc",  # Ignore compiled Python files
                "-I",
                "venv",  # Ignore virtual environment directory
                "--dirsfirst",  # List directories first
            ],
            capture_output=True,
            text=True,
            check=True,
        )

        # Clean up the output by removing any special characters
        cleaned_output = (
            result.stdout.replace("\x1b", "")  # Remove escape sequences
            .replace("[0m", "")
            .replace("[01;34m", "")
            .replace("B", "")
        )  # Remove the 'B' artifact

        # Write the cleaned output to the specified file
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(cleaned_output)

    except subprocess.CalledProcessError as e:
        print(f"Error running tree command: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


def main():
    if len(sys.argv) != 2:
        print("Usage: python tree_output.py output_file")
        sys.exit(1)

    output_file = sys.argv[1]
    get_tree_output(output_file)
    print(f"Tree structure written to {output_file}")


if __name__ == "__main__":
    main()
