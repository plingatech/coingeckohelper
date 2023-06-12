from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder

import logging
from logging.handlers import SysLogHandler
import const
import coingeckoApi
import mapHelper

logger = logging.getLogger('my_logger')
logger.setLevel(logging.INFO)
handler = SysLogHandler(address='/dev/log')
handler.setLevel(logging.DEBUG)

# تنظیم فرمت پیام‌های لاگ
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# اضافه کردن handler به logger
logger.addHandler(handler)



app = FastAPI()
#print(coingeckoApi.getTokenDetail("tether"))
#print(mapHelper.mustCoinIdAdd("binance-usd"))
#print(mapHelper.correctCoinList(coingeckoApi.getCoins()))
#print(mapHelper.correctCoingeckoCoin("tether",coingeckoApi.getTokenDetail("tether")))
print(mapHelper.generateAddressForCoingeckoPrice("0xbD07cf23A43f13078716A015F3Cc27F7a1661e65"))


@app.get("/api/v1/coins/list")
def getCoinListWithPlatform(include_platform : str):
    logger.info(f"platform is {include_platform}")
    result = mapHelper.correctCoinList(coingeckoApi.getCoins())
    cleaned_json_str = jsonable_encoder(result)
    logger.info(result)
    return cleaned_json_str

@app.get("/api/v1/coins/{id}")
def getCoin(id : str):
    result = mapHelper.correctCoingeckoCoin("tether",coingeckoApi.getTokenDetail("tether"))
    return result


@app.get("/api/v1/simple/token_price/{platform}?vs_currencies={currency}&include_market_cap=true&contract_addresses={joined_addresses}")
async def getCoin(platform, vs_currencies, contract_addresses):
    result = await mapHelper.correctCoingeckoCoin("tether",coingeckoApi.getTokenDetail("tether"))
    return result



