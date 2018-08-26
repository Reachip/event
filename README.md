# Example : 

```python 
import json
import pprint

from event import HttpDownloadEvent

download = HttpDownloadEvent()

download.add("https://jsonplaceholder.typicode.com/photos")
download.add("https://jsonplaceholder.typicode.com/comments")
download.add("https://jsonplaceholder.typicode.com/todos")

@download.on_start
def start():
    print("The download start ...")

@download.on_finish
def finish(urls_contents):
    pp = pprint.PrettyPrinter(indent=4)

    for content in urls_contents:
        print("The API return :")
        pp.pprint(json.loads(content))

@download.on_error
def error(error):
    print(f"A error occured : {error}")

download.start()
```
