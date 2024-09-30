from uvicorn import run

"""
This script serves as the entry point for running the FastAPI application.

It initializes and runs the server using Uvicorn with specific configurations such as host, port, and auto-reload for development purposes.

Usage:
- Run this script to start the FastAPI server with the defined settings.
"""
if __name__ == "__main__":
    run("src.main:app", host="127.0.0.1", port=8001, reload=True)