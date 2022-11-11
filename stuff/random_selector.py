import random
from datetime import datetime
from settings import settings
import json


class VanillaRandomSelector:
    def __init__(self, path, sep="\n") -> None:
        self.already_used =  set()
        with open(path, "r") as f:
            self.content = set([l for l in f.read().split(sep)])

    def give_random(self, n):
        retval = random.sample(list(self.content), min(len(self.content), n))
        self.already_used.update(retval)
        return retval

class RandomDocBodyGenerator:
    def __init__(self, path=settings["main_txt_file"], url_path=settings["urls_file"], sep=".",\
        min_chap= settings["min_chapters"], max_chap=settings["max_chapters"],\
        min_sections=settings["min_sections"], max_sections=settings["max_sections"],\
        min_paragraphs=settings["min_paragraphs"], max_paragraphs=settings["max_paragraphs"],\
        min_sentences=settings["min_sentences"], max_sentences=settings["max_sentences"],\
         text_prob=settings["text_to_other_prob"]) -> None:

        with open(path, "r") as f, open(url_path, "r") as f1:
            self.sentences = tuple(line for line in f.read().split(sep))
            self.urls = tuple(line for line in f1.read().split("\n"))
        

        self.min_chap = min_chap
        self.max_chap = max_chap

        self.min_paragraphs = min_paragraphs
        self.max_paragraphs = max_paragraphs

        self.min_sections = min_sections
        self.max_sections = max_sections

        self.min_sentences = min_sentences
        self.max_sentences = max_sentences

        self.text_prob = text_prob

    def generate_random_document_body(self):
        chapters_num = random.randint(self.min_chap, self.max_chap)
        chapters = []
        for n in range(chapters_num):
            chapters.append(self.create_chapter())
        return {"DocumentBody":chapters}

    def create_chapter(self):

        paragraphs_num = random.randint(self.min_paragraphs, self.max_paragraphs)
        paragraphs = []
        for m in range(paragraphs_num):
            paragraphs.append(self.create_paragraph())
        return {"Chapter" : {"Title" : self.get_random_sentence(), "Paragraphs" : paragraphs}}

    def create_paragraph(self):
        
        sections_num = random.randint(self.min_sections, self.max_sections)
        sections =  []
        for l in range(sections_num):
            sections.append(self.create_section())
        return {"Paragraph" : {"Title" : self.get_random_sentence(), "Sections": sections}}


    def create_section(self):
        if random.random() <= self.text_prob:
            return self.create_text()
        else:
            return self.create_url()

    def create_text(self):
        text = "".join(random.sample(self.sentences, random.randint(self.min_sentences, self.max_sentences)))
        return {"text":text}

    def create_url(self):
        url = random.choice(self.urls)
        return {"url": url}

    def get_random_sentence(self):
        return random.choice(self.sentences)
if __name__ == "__main__":
    with open("ciro.json","w") as f:
        json.dump(RandomDocBodyGenerator().generate_random_document_body(), f, indent=1)