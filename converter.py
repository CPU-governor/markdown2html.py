import markdown

# Function to convert Markdown to HTML
def convert_md_to_html(md_content):
    return markdown.markdown(md_content)

# Read the Markdown file
with open('example.md', 'r') as md_file:
    md_content = md_file.read()

# Convert to HTML
html_content = convert_md_to_html(md_content)

# Save the HTML content to a file
with open('example.html', 'w') as html_file:
    html_file.write(html_content)

print("Markdown converted to HTML and saved to example.html")

# to use change example to actual file name and or path
