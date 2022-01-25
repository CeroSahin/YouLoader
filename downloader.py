from pytube import YouTube


class Downloader(YouTube):
    def __init__(self, title, path, link):
        super(Downloader, self).__init__(title, path, link)
        self.title = title
        self.path = path
        self.link = link

    def create_yt(self):
        yt = YouTube(self.link)
        yt.set_filename(self.title)
