"""
The purspose of this file is to make n calls using a http libray of choice.
We will include any possible way to make http calls.
Additionally we also want to do this generically and allow to pass the page we want to process.
Currently we just support get requests.
"""

import requests
import asyncio
import httpx
import aiohttp

async def httpx_call(count: int, url: str):
    """ This is a httpx call. It support both sync and async http calls. """
    
    httpx_client = httpx.AsyncClient()

    async with httpx_client:

        tasks = [httpx_client.get(url) for _ in range(count)]

        await asyncio.gather(*tasks)
        

async def aiohttp_call(count: int, url: str):
    """ This is aiohttp and only support async http calls. """

    aiohttp_client = aiohttp.ClientSession()

    async with aiohttp_client:

        tasks = [aiohttp_client.get(url) for _ in range(count)]

        await asyncio.gather(*tasks)


def requests_call(count: int, url: str):
    """ This is requests and only support sync http calls. """
    
    tasks = [requests.get(url) for _ in range(count)]
   
