import time
import pytest
from cookbook.http import perf

# These are exclusively for saving the plots generated in the test
import matplotlib.pyplot as plt
import numpy as np

# markign at module level - or use this decorator -  @pytest.mark.asyncio
# note: we need the module - pytest-asyncio
pytestmark = pytest.mark.asyncio

async def __test_httpx_call(count: int = 10, resource: str = "http://google.com"):
    start_time = time.perf_counter()
    await perf.httpx_call(count, resource)
    end_time = time.perf_counter()
    return end_time - start_time
    print(f"HTTPX: {end_time - start_time:.2f} seconds")


async def __test_aiohttp_call(count: int = 10, resource: str = "http://google.com"):
    start_time = time.perf_counter()
    await perf.aiohttp_call(count, resource)
    end_time = time.perf_counter()
    return end_time - start_time
    #print(f"AIOHTTP: {end_time - start_time:.2f} seconds")


def __test_requests_call(count: int = 10, resource: str = "http://google.com"):
    start_time = time.perf_counter()
    perf.requests_call(count, resource)
    end_time = time.perf_counter()
    return end_time - start_time
    #print(f"Requests: {end_time - start_time:.2f} seconds")


async def test_generate_report():
    file_loc = "/Users/riaz/EffectiveCode/Python/Courses/PythonCookbook/files"
    resource = "http://google.com"
    # We will try to save a matplotlib plot with x axis with number of calls and y-axis with time taken 
    # we use the following granularity -> 10 calls, 50 calls, 100 calls
    # we will also want to print out time taken to run this test itself
    
    start_time = time.perf_counter()

    x_axis = [10, 50, 100, 200]

    # we will save the times seperaty to provide labels
    # this may seem a bit messy and could be done using pandas
    t_httpx = []
    t_aiohttp = []
    t_requests = []

    for count in x_axis:
        httpx_time = await __test_httpx_call(count, resource)
        aiohttp_time = await __test_aiohttp_call(count, resource)
        requests_time = __test_requests_call(count, resource)

        t_httpx.append(httpx_time)
        t_aiohttp.append(aiohttp_time)
        t_requests.append(requests_time)

    print("httpx ", t_httpx)
    print("aiohttp ", t_aiohttp)
    print("requests ", t_requests)

    plt.plot(x_axis, t_httpx, label="httpx")
    plt.plot(x_axis, t_aiohttp, label="aiohttp")
    plt.plot(x_axis, t_requests, label="requests")

    plt.xlabel('Iterations')
    plt.ylabel('Time in seconds')
    plt.legend()
    plt.savefig("/".join([file_loc, "http_perf_report.png"]))

    end_time = time.perf_counter()
    print(f"Time taken for perf test: {end_time - start_time:.2f} seconds")
