import io
import os
from pdfminer3.layout import LAParams
from pdfminer3.pdfpage import PDFPage
from pdfminer3.pdfinterp import PDFResourceManager
from pdfminer3.pdfinterp import PDFPageInterpreter
from pdfminer3.converter import TextConverter
from collections import Counter


# Edit filename to set target PDF file
filename = 'resources/SocialRecovery.pdf'

# Edit keyword_num to set number of keywords
keyword_num = 10


resource_manager = PDFResourceManager()
fake_file_handle = io.StringIO()
converter = TextConverter(resource_manager, fake_file_handle, laparams=LAParams())
page_interpreter = PDFPageInterpreter(resource_manager, converter)

with open(filename, 'rb') as file:

    for page in PDFPage.get_pages(file,
                                  caching=True,
                                  check_extractable=True):
        page_interpreter.process_page(page)

    text = fake_file_handle.getvalue()

converter.close()
fake_file_handle.close()

words = text\
    .lower().replace('\n', ' ').split(' ')

words = list(filter(''.__ne__, words))

stopwords = set(open(str(os.path.dirname(os.path.abspath(__file__))) + '/stopwords_english', 'r').read().splitlines())

filtered_words = []


def filter_function(x):
    if x not in stopwords:
        filtered_words.append(x)


list(map(filter_function, words))

word_frequency = Counter(filtered_words)

keywords = word_frequency.most_common(keyword_num)

print('Keywords: ' + str(keywords))

input("Press Enter to exit.")
