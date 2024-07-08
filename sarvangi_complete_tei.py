#Code for combining 126 sections

import os
from bs4 import BeautifulSoup

# Function to remove headers and return body content
def remove_headers(section_content):
    soup = BeautifulSoup(section_content, 'lxml')
    for header in soup.find_all('head'):
        header.decompose()
    return soup.body

# Directory containing the section files
directory = '/Users/shikha/Desktop/Sarvangi/Sarvangi'

# Read each section and process it
combined_body = BeautifulSoup('<div></div>', 'lxml').div
for i in range(1, 127):
    file_path = os.path.join(directory, f'section{i}.xml')
    if not os.path.isfile(file_path):
        print(f"File not found: {file_path}")
        continue
    with open(file_path, 'r', encoding='utf-8') as file:
        section_content = file.read()
    section_body = remove_headers(section_content)
    combined_body.append(section_body)

# Create and add the new header
new_header_content = '''
<teiHeader>
  <fileDesc>
    <titleStmt>
      <title>Introduction</title>
    </titleStmt>
  </fileDesc>
  <sourceDesc>
    <p>Gopāladāsa, Sarvāṅgī (abbrev. GopS)</p>
    <p>Source: Winand Callewaert, The Sarvāṅgī of Gopāldās, New Delhi, Manohar Book Publications, 1993; 520pp.; text pp. 119-521.</p>
    <p>The text below of The Sarvāṅgī of Gopāldās is a revised version of the printed text referred to above. Working on the Dictionary of Bhakti and checking the manuscript once more has yielded some useful corrections which in the text below are highlighted in yellow.</p>
  </sourceDesc>
</teiHeader>
'''
new_header = BeautifulSoup(new_header_content, 'lxml')
combined_body.insert(0, new_header)

# Debugging: print the combined body before wrapping in <TEI> tags
print("Combined Body (before wrapping in <TEI> tags):")
print(combined_body.prettify())

# Wrap the combined body in <TEI> tags
combined_document = BeautifulSoup('<TEI></TEI>', 'lxml')
tei_element = combined_document.find('tei')
if tei_element is not None:
    tei_element.append(combined_body)
else:
    print("Error: <TEI> element not found in the document.")

# Debugging: print the combined document after wrapping
print("Combined Document (after wrapping in <TEI> tags):")
print(combined_document.prettify())

# Save the combined document
output_file = '/Users/shikha/Desktop/Sarvangi/Sarvangi/combined_document.xml'
with open(output_file, 'w', encoding='utf-8') as file:
    file.write(combined_document.prettify())

print(f"Combined document saved to {output_file}")



