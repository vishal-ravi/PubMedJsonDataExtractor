import json

# Load JSON data from input.json
with open('inputs.json', 'r') as json_file:
    data = json.load(json_file)

# Define the desired section types and types
desired_mappings = [
    {"section_type": "TITLE", "type": ["title","front" ,"title_1", "title_2", "title_3"]},
    {"section_type": "ABSTRACT", "type": ["paragraph", "front", "abstract"]},
    {"section_type": "INTRO", "type": ["paragraph"]},
    {"section_type": "METHODS", "type": ["paragraph", "title"]},
    {"section_type": "RESULTS", "type": ["paragraph","title"]},
    {"section_type": "DISCUSS", "type": ["paragraph"]}
]

# Create an HTML file
with open('output.html', 'w') as html_file:
    # Write the initial HTML structure
    html_file.write("<html><head><title>Extracted Text</title></head><body>")

    # Extract and write the "text" content based on the desired mappings
    for mapping in desired_mappings:
        section_type = mapping["section_type"]
        desired_types = mapping["type"]
        
        html_file.write(f"<h1>{section_type}</h1>")
        
        for passage in data['documents'][0]['passages']:
            if passage['infons']['section_type'] == section_type and passage['infons']['type'] in desired_types:
                section_text = passage['text']
                
                html_file.write(f"<p>{section_text}</p>")
                html_file.write("<hr>")

    # Close the HTML file
    html_file.write("</body></html>")
