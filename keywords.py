import io
from pdfminer3.layout import LAParams
from pdfminer3.pdfpage import PDFPage
from pdfminer3.pdfinterp import PDFResourceManager
from pdfminer3.pdfinterp import PDFPageInterpreter
from pdfminer3.converter import TextConverter
from collections import Counter
from nltk.corpus import stopwords

resource_manager = PDFResourceManager()
fake_file_handle = io.StringIO()
converter = TextConverter(resource_manager, fake_file_handle, laparams=LAParams())
page_interpreter = PDFPageInterpreter(resource_manager, converter)

# Edit this line to change target file
with open('resources/SocialRecovery.pdf', 'rb') as file:

    for page in PDFPage.get_pages(file,
                                  caching=True,
                                  check_extractable=True):
        page_interpreter.process_page(page)

    text = fake_file_handle.getvalue()

converter.close()
fake_file_handle.close()

words = text\
    .lower()\
    .replace('fig', '').replace('1', '').replace('2', '').replace('3', '').replace('4', '').replace('5', '')\
    .replace('6',   '').replace('7', '').replace('8', '').replace('9', '').replace('0', '').replace(',', '')\
    .replace('\n', ' ').replace('.', '').replace('?', '').replace('!', '').replace('(', '').replace(')', '')\
    .replace('-',   '').replace('_', '').replace('=', '')\
    .split(' ')

words = list(filter(''.__ne__, words))

stop_words = set(stopwords.words('english'))
filtered_words = []

for x in words:
    if x not in stop_words:
        filtered_words.append(x)

word_frequency = Counter(filtered_words)

# Edit x in '.most_common(x)' to set number of keywords
keywords = word_frequency.most_common(10)

print(keywords)

input("Press Enter to exit.")
