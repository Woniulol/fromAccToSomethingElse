"""
The `for` keyword works with iterables.
The `await` keyword works with awaitables.

Types of awaitables:
A native coroutine object: created by calling a native coroutine object
An `asyncio.Task`: usually created by passing a coroutine object to `asyncio.create_task()`

`asyncio.Task` is a subclass of `asyncio.Future`

As the end user, we usually don't need to maintain the reference to `asyncio.Task`.
Creating the `asyncio.Task` is already enough to schedule the coroutine to run

In contrast, we use `await other_coro()` to run `other_coro` right now and wait for its completion
because we need tis result before we can proceed.
"""

import time
from pathlib import Path
from typing import Callable

import httpx

POP20_CC = ('CN IN US ID BR PK NG BD RU JP '
            'MX PH VN ET EG DE IR TR CD FR').split()

BASE_URL = 'https://www.fluentpython.com/data/flags'
DEST_DIR = Path('downloaded')

def save_flag(img: bytes, filename: str) -> None:
    (DEST_DIR / filename).write_bytes(img)

def get_flag(cc: str) -> bytes:
    url = f'{BASE_URL}/{cc}/{cc}.gif'.lower()
    resp = httpx.get(url, timeout=6.1,
                     follow_redirects=True)
    resp.raise_for_status()
    return resp.content

def download_many(cc_list: list[str]) -> int:
    for cc in sorted(cc_list):
        image = get_flag(cc)
        save_flag(image, f'{cc}.gif')
        print(cc, end=' ', flush=True)
    return len(cc_list)

def main(downloader: Callable[[list[str]], int]) -> None:
    DEST_DIR.mkdir(exist_ok=True)
    t0 = time.perf_counter()
    count = downloader(POP20_CC)
    elapsed = time.perf_counter() - t0
    print(f'\n{count} downloads in {elapsed:.2f}s')

if __name__ == '__main__':
    main(download_many)
