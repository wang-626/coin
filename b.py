import asyncio
from binance import AsyncClient, BinanceSocketManager

async def coin_main(coin):
    client =  await AsyncClient.create()
    bm = BinanceSocketManager(client)
    ts = bm.symbol_miniticker_socket(coin)
    # enter the context manager
    await ts.__aenter__()
    # receive a message
    msg = await ts.recv()
    # exit the context manager
    await ts.__aexit__(None, None, None)
    await client.close_connection()
    return msg

async def task(coin1,coin2,coin3,coin4,coin5):
    c1,c2,c3,c4,c5= await asyncio.gather(
         coin_main(coin1),
         coin_main(coin2),
         coin_main(coin3),
         coin_main(coin4),
         coin_main(coin5)
         )
    return c1,c2,c3,c4,c5

def coin_price(coin1,coin2,coin3,coin4,coin5):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    return asyncio.run(task(coin1,coin2,coin3,coin4,coin5))

if __name__ == "__main__":
    x,x2,x3,x4,x5=coin_price('BTCUSDT','ETHUSDT','BNBUSDT','ADAUSDT','LUNAUSDT')
    print('%.2f'%float(x['c']))
    