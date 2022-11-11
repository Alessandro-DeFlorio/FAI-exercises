from random_selector import *
from settings import settings
class Document:
    def __init__(self, names, titles, main_text, max_chapters, max_sections, text_to_pic_odds) -> None:
        self.names = VanillaRandomSelector(settings["names_file"])
        self.titles= VanillaRandomSelector(settings["titles_file"])
        self.text = VanillaRandomSelector(settings["main_txt_file"], sep=".")

    def weird_shit(self):
        print(self.names.give_random(2))
        print(self.titles.give_random(1))
        print(self.text.give_random(7))

a= Document("ciao.txt","ciao.txt", "text.txt", 1,1,1)
a.weird_shit()