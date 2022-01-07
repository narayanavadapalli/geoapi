import aiohttp
import asyncio

async def main():
    geojson='https://datahub.io/core/geo-countries/r/countries.geojson'
    async with aiohttp.ClientSession() as session:
        async with session.get(geojson) as response:

            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])

            html = await response.text()
            print("Body:", html, "...")

loop = asyncio.get_event_loop()
loop.run_until_complete(main())