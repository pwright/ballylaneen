#!/usr/bin/env python3

from datetime import datetime
import os

# Define the file path
docs_dir = "docs"
today_md_path = os.path.join(docs_dir, "today.md")

# Ensure the docs directory exists
os.makedirs(docs_dir, exist_ok=True)

# Generate the link for today's Wikipedia page
current_year = datetime.now().year
wiki_url = f"https://en.wikipedia.org/wiki/Deaths_in_{current_year}"
content = f"# Today\n\n[Deaths in {current_year}]({wiki_url}){{ .md-button }}"

# Write to the file
with open(today_md_path, "w") as f:
    f.write(content)

print(f"'today.md' created at {today_md_path} with link to {wiki_url}.")
