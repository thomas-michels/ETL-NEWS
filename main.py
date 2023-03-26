"""
Inicialize application
"""

import asyncio
from app.api import run_api
from app.worker import Worker


if __name__ == "__main__":
    worker = asyncio.new_event_loop()
    worker.run_in_executor(None, Worker)
    
    api = asyncio.new_event_loop()
    api.run_in_executor(None, run_api)
