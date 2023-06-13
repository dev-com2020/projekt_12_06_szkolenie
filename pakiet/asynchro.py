import asyncio

async def greet(name):
    return f'Hello, {name}!'


async def main():
    for name in ['Mateusz', 'Kasia', 'Basia']:
        a = await greet(name)
        print(a)

asyncio.run(main())