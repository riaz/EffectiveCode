import time
import pytest
from cookbook.http import perf

# markign at module level
pytestmark = pytest.mark.asyncio

async def test_httpx_call():
    start_time = time.perf_counter()
    await perf.httpx_call(500, "http://google.com")
    end_time = time.perf_counter()
    print(f"HTTPX: {end_time - start_time:.2f} seconds")


async def test_aiohttp_call():
    start_time = time.perf_counter()
    await perf.aiohttp_call(500, "http://google.com")
    end_time = time.perf_counter()
    print(f"AIOHTTP: {end_time - start_time:.2f} seconds")
