import asyncio

"""
difference between time.sleep() and asyncio.sleep()
"""

async def get_user():
    await asyncio.sleep(2)
    # return {"user":'Shrikant'}
    return {"user": "Shrikant"}
async def get_book():
    await asyncio.sleep(2)
    return {"book": "Python"}

async def get_notification():
    await asyncio.sleep(2)
    return {"notification": "Email"}

async def get_dashboard():

    user, book, notification = await asyncio.gather(
        get_user(),
        get_book(),
        get_notification(),
        return_exceptions=True      ## It works when exception occurred at any method
    )
    return {"user": user, "book": book, "notification": notification}

async def main():
    result = await get_dashboard()
    print(result)

asyncio.run(main())


