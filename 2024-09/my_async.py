import asyncio
import socket
from keyword import kwlist


MAX_KEYWORD_LEN = 4

async def probe(domain: str) -> tuple[str, bool]:
    loop = asyncio.get_running_loop()
    try:
        # Suspends the current coroutine object.
        # Give the control back to event loop, waiting to be called.
        await loop.getaddrinfo(domain, None)
    except socket.gaierror:
        return (domain, False)
    return (domain, True)

async def main():
    names = (kw for kw in kwlist if len(kw) <= MAX_KEYWORD_LEN)
    domains = (f"{name}.dev".lower() for name in names)

    # probe(...) will return a coroutine object
    coros = [probe(domain=domain) for domain in domains]

    # asyncio.as_completed returns a generator of coroutine object, and return the results of the
    # original Futures (or coroutines) in the order in which and as soon as they complete.

    for coro in asyncio.as_completed(coros):

        # Within this for loop, we know for sure each coroutine is finished already, and
        # we only need to retrieve the result from each coroutine use `await`

        domain, found = await coro # Get return value
        mark = "+" if found else "-"
        print(f"{mark} {domain}")

if __name__ == "__main__":
    asyncio.run(main())