import argparse
from UVA_news_api import *
import asyncio
import json


parser = argparse.ArgumentParser()
parser.add_argument("api_action", 
                    choices= ["query", "recent", "update", "author", "url", "name"])
parser.add_argument("parameter")
args = parser.parse_args()

async def main():
    if args.api_action == "query":
        api_output = await get_query(args.parameter)
        server_output = json.dumps(api_output,ensure_ascii=False)
        print(server_output)
    elif args.api_action == "recent":
        if not args.parameter.isnumeric():
            print("Invalid input for get_recent")
        else:
            api_output =await get_recent(int(args.parameter))
            print(json.dumps(api_output,ensure_ascii=False))
    elif args.api_action == "update":
        api_output = await update(args.parameter)
        print(json.dumps(api_output,ensure_ascii=False))
    elif args.api_action == "author":
        api_output = await get_by_author(args.parameter)
        print(json.dumps(api_output,ensure_ascii=False))
    elif args.api_action == "url":
        api_output = await get_by_url(args.parameter)
        print(json.dumps(api_output,ensure_ascii=False))
    elif args.api_action == "name":
        api_output =await get_by_name(args.parameter)
        print(json.dumps(api_output,ensure_ascii=False))

asyncio.run(main())


