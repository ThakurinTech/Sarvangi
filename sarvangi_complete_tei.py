from bs4 import BeautifulSoup

# Create and add the new header
new_header_content = """
<teiHeader>
  <fileDesc>
    <titleStmt>
      <title>The Sarvāṅgī of Gopāldās</title>
    </titleStmt>
  </fileDesc>
  <sourceDesc>
    <p>Gopāladāsa, Sarvāṅgī (abbrev. GopS)</p>
    <p>Source: Winand Callewaert, The Sarvāṅgī of Gopāldās, New Delhi, Manohar Book Publications, 1993; 520pp.; text pp. 119-521.</p>
    <p>The text below of The Sarvāṅgī of Gopāldās is a revised version of the printed text referred to above. Working on the Dictionary of Bhakti and checking the manuscript once more has yielded some useful corrections which in the text below are highlighted in yellow.</p>
  </sourceDesc>
</teiHeader>
"""

lg_map = {
    "[S]": "sākhī",
    "[P]": "pada",
    "[K]": "kavitta",
    "[A]": "arilla",
    "[Ś]": "śloka",
    "[C]": "caupāī",
    "[SAVAI]": "savaiye",
}

tei = """<?xml version="1.0" encoding="utf-8"?>
<TEI xmlns="http://www.tei-c.org/ns/1.0">"""
tei += new_header_content
tei += "<text><body>"
for i in range(1, 127):
    file_path = f"section{i}.xml"
    with open(file_path, "r", encoding="utf-8") as file:
        section_content = file.read()
    soup = BeautifulSoup(section_content, "xml")
    for lg in soup.find_all("lg"):
        if "type" in lg.attrs:
            lg["type"] = lg_map.get(lg["type"], lg["type"]).title()
    tei += soup.div.prettify()
tei += "</text></body>"
tei += "</TEI>"

soup = BeautifulSoup(tei, "xml")
with open("sarvangi_of_gopaldas.xml", "w", encoding="utf-8") as file:
    file.write(soup.prettify())
