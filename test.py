# import os
# from bs4 import BeautifulSoup

# input_folder = '/Users/shikha/Desktop/Sarvangi/Sarvangi'  # Replace with your input folder path
# output_file = '/Users/shikha/Desktop/Sarvangi/Sarvangi/combined_document.xml'  # Replace with your output file path

# # Create a BeautifulSoup object for the combined document
# combined_document = BeautifulSoup('<TEI xmlns="http://www.tei-c.org/ns/1.0"><text><body><div></div></body></text></TEI>', 'xml')

# # Create and add the new TEI header
# new_header_content = '''
# <teiHeader>
#   <fileDesc>
#     <titleStmt>
#       <title>Combined Document</title>
#     </titleStmt>
#     <publicationStmt>
#       <p>Publication Information</p>
#     </publicationStmt>
#     <sourceDesc>
#       <p>Source Description</p>
#     </sourceDesc>
#   </fileDesc>
# </teiHeader>
# '''
# new_header = BeautifulSoup(new_header_content, 'xml')
# combined_document.TEI.insert(0, new_header.teiHeader)

# # Print the combined document structure for debugging
# print("Combined document structure after adding the header:")
# print(combined_document.prettify())

# # Find the <div> element where content will be appended
# div_element = combined_document.find('div')
# if div_element is None:
#     print("Error: <div> element not found in the combined document.")
#     exit(1)

# # Iterate through each file in the input folder
# for filename in os.listdir(input_folder):
#     if filename.endswith('.xml'):
#         input_file = os.path.join(input_folder, filename)
        
#         # Read the content of the input file
#         with open(input_file, 'r', encoding='utf-8') as f:
#             content = f.read()
        
#         # Parse the content using BeautifulSoup
#         soup = BeautifulSoup(content, 'xml')
        
#         # Remove <teiHeader> if it exists
#         if soup.find('teiHeader'):
#             soup.teiHeader.decompose()
        
#         # Remove the outer <TEI> tags
#         tei_content = soup.find('TEI')
#         if tei_content:
#             tei_content.unwrap()
        
#         # Find the <body> content
#         body_content = soup.find('body')
#         if body_content:
#             # Extract the <div> content inside the <body>
#             inner_div = body_content.find('div')
#             if inner_div:
#                 div_element.append(inner_div.extract())
#             else:
#                 print(f"No <div> found in the body of {filename}")
#         else:
#             print(f"No <body> found in {filename}")

#     else:
#         print(f'Skipped file: {filename} (not an XML file)')

# # Save the combined document
# with open(output_file, 'w', encoding='utf-8') as fout:
#     fout.write(combined_document.prettify())

# print(f"Combined document saved to {output_file}")


# import os
# from bs4 import BeautifulSoup

# # Function to remove <teiHeader> and wrap content within <body> tags
# def remove_headers_and_wrap_body(section_content):
#     soup = BeautifulSoup(section_content, 'xml')
#     # Remove <teiHeader> if it exists
#     if soup.find('teiHeader'):
#         soup.teiHeader.decompose()
#     # Remove <TEI> tags and get the content inside them
#     tei_content = soup.find('text')
#     if tei_content:
#         body_content = tei_content.decode_contents()
#     else:
#         body_content = soup.decode_contents()

#     # Parse the body content to remove any <head> tags
#     body_soup = BeautifulSoup(body_content, 'xml')
#     for header in body_soup.find_all('head'):
#         header.decompose()
    
#     # Return body content wrapped in <body> tags
#     return body_soup

# # Directory containing the section files
# input_folder = '/Users/shikha/Desktop/Sarvangi/Sarvangi'
# output_file = '/Users/shikha/Desktop/Sarvangi/Sarvangi/2combined_document.xml'

# # Create the combined document structure
# combined_document = BeautifulSoup('<TEI xmlns="http://www.tei-c.org/ns/1.0"><teiHeader><fileDesc><titleStmt><title>Combined Document</title></titleStmt><publicationStmt><p>Publication Information</p></publicationStmt><sourceDesc><p>Source Description</p></sourceDesc></fileDesc></teiHeader><text><body><div></div></body></text></TEI>', 'xml')

# # Get the <div> element where the content will be appended
# div_element = combined_document.find('div')

# # Read each section and process it
# for i in range(1, 127):
#     file_path = os.path.join(input_folder, f'section{i}.xml')
#     if not os.path.isfile(file_path):
#         print(f"File not found: {file_path}")
#         continue
#     with open(file_path, 'r', encoding='utf-8') as file:
#         section_content = file.read()
#     section_body = remove_headers_and_wrap_body(section_content)
#     div_element.append(section_body)

# # Debugging: print the combined document after wrapping
# print("Combined Document (after wrapping in <TEI> tags):")
# print(combined_document.prettify())

# # Save the combined document
# with open(output_file, 'w', encoding='utf-8') as file:
#     file.write(combined_document.prettify())

# print(f"Combined document saved to {output_file}")


