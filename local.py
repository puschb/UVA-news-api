import UVA_news_api as api
import json
import asyncio

#example local usage


async def main():
  api_resposne = await api.get_recent(10)
  with open("example.json", "w", encoding='utf-8') as f:
    f.write(json.dumps(api_resposne, ensure_ascii=False))

asyncio.run(main())