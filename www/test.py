import orm
from models import User, Blog, Comment
import asyncio

async def test():
    await orm.create_pool(loop=loop, host='localhost', port=3306, user='www-data', password='www-data', db='awesome')

    u = User(name='test', email='test@example.com', password='1234567890', image='about:blank')

    await u.save()

    'another sql check code'
    data = await User.findAll()
    for d in data:
        print(d)

    await orm.destory_pool()

# 获取EventLoop:
loop = asyncio.get_event_loop()

#把协程丢到EventLoop中执行
loop.run_until_complete(test())

#关闭EventLoop
loop.close()

