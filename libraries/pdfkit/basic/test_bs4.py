import bs4

html = """
<!DOCTYPE html>
<html>
<head>
  <title>Informe</title>
  <style>
    ...
  </style>
</head>
<body>
  ...
</body>
</html>
"""

soup = bs4.BeautifulSoup(html, "html.parser")

h1_tags = soup.find_all("h1", text="Informe")

if h1_tags:
  h1_tag = h1_tags[0]
else:
  h1_tag = bs4.BeautifulSoup.new_tag(soup, "h1")
  h1_tag.string = "Informe"
  soup.body.insert(0, h1_tag)

h2_tag = bs4.BeautifulSoup.new_tag(soup, "h2")
h2_tag.string = "Título del informe"
h1_tag.insert_after(h2_tag)

html = soup.prettify()

print(html)
