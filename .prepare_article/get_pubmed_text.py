import html2text

h = html2text.HTML2Text()
h.ignore_links = True
h.ignore_tables = True
h.ignore_images = True
h.decode_error = "ignore"

EXAMPLE1 = ".prepare_example/COVID-19 related thrombosis_ A mini-review - PMC.html"

with open(EXAMPLE1, "r", encoding="utf-8") as infile:
    html = infile.read()

text = h.handle(html)

with open("pubmed1.txt", "w", encoding="utf-8") as outfile:
    outfile.write(text)
