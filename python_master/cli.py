"""CLI entry point for Python Master app."""

import subprocess
import sys
import os


def main():
    """Run the Python Master Streamlit app."""
    app_path = os.path.join(os.path.dirname(__file__), "app.py")
    subprocess.run([sys.executable, "-m", "streamlit", "run", app_path] + sys.argv[1:])


if __name__ == "__main__":
    main()
