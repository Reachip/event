import threading
import requests


class HttpDownloadEvent(object):
    def __init__(self):
        self.callbacks = {}
        self.urls = []
        self.urls_contents = []

    def add(self, url):
        """ Add the given URL to the list of URLs whose contents you want to download """
        self.urls.append(url)

        return self

    def on_start(self, callback):
        """ A decorator where his callback is called when the download starts """
        self.callbacks[self.on_start.__name__] = callback

        return callback

    def on_finish(self, callback):
        """ A decorator where his callback is called when the download ends """
        self.callbacks[self.on_finish.__name__] = callback

        return callback

    def on_error(self, callback):
        """ A decorator where his callback is called when the download encounters an error """
        self.callbacks[self.on_error.__name__] = callback

        return callback

    def start(self):
        """ The main methord called to start the download """
        try:
            http_request = lambda url: self.urls_contents.append(
                requests.get(url, headers=self.headers).content
            )

            self.callbacks[self.on_start.__name__]()

            threads = [
                threading.Thread(target=http_request, args=(url,)) for url in self.urls
            ]

            [thread.start() for thread in threads]
            [thread.join() for thread in threads]

            self.callbacks[self.on_finish.__name__](self.urls_contents)

        except Exception as error:
            self.callbacks[self.on_error.__name__](error)
