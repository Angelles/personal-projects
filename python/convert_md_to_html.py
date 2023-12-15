import markdown 

# Open the Markdown file and read it.

with open('example.md', 'r') as file:
    text = file.read()
    html = markdown.markdown(text)


# Write the file contents to an HTML file.

with open('example.html', 'w') as file:
    file.write(html)
