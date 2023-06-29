import grequests
from urllib.request import urlopen
import time
import asyncio

urls = [
    'https://news.virginia.edu/content/all-news?page=0',
    'https://news.virginia.edu/content/all-news?page=1',
    'https://news.virginia.edu/content/all-news?page=2',
    'https://news.virginia.edu/content/all-news?page=3',
    'https://news.virginia.edu/content/all-news?page=4',
    'https://news.virginia.edu/content/all-news?page=5',
    'https://news.virginia.edu/content/all-news?page=6',
    'https://news.virginia.edu/content/all-news?page=7',
    'https://news.virginia.edu/content/all-news?page=8',
    'https://news.virginia.edu/content/all-news?page=9',
    'https://news.virginia.edu/content/all-news?page=10',
    'https://news.virginia.edu/content/all-news?page=11',
    'https://news.virginia.edu/content/all-news?page=12',
    'https://news.virginia.edu/content/all-news?page=13',
    'https://news.virginia.edu/content/all-news?page=14',
    'https://news.virginia.edu/content/all-news?page=15'
]
print(time.perf_counter())
rs = (grequests.get(u) for u in urls)

list_of_responses = grequests.map(rs)

print("here")
print(time.perf_counter())

print(list(list_of_responses))
print(time.perf_counter())

