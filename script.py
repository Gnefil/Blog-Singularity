import os

directory = "./source/_drafts/zh/"
reference_file = "./scaffolds/post.md"
mapping = {"subtitle": "excerpt"}

def process_to_current_page_scaffold(directory: str = "./source/_drafts/en/", reference_file: str = "./scaffolds/post.md", mapping: dict = {"subtitle": "excerpt"}):
    """
    In-place process all markdown files imported from the old blog to the current blog. Refactor the front matter to the current blog's front matter.
    
    Only old attributes with the same name are kept in the new version. Any other changes in attribute names must be specified in the mapping dictionary.

    Args:
        directory (str): The directory where the markdown files are located. 
        reference_file (str): The reference file that contains the front matter of the current blog.
        mapping (dict): A dictionary that maps the old attribute names to the new attribute names.
    """
    preserved_attributes = dict()
    with open(reference_file, "r", encoding="utf-8") as f:
        for line in f.readlines():
            if line == "---\n" or line == "\n":
                continue
            preserved_attributes[line.split(":")[0]] = None

            
    for basename in os.listdir(directory):
        filename = os.path.join(directory, basename)

        if not filename.endswith(".md"):
            continue

        with open(filename, "r+", encoding="utf-8") as f:
            all_lines = f.readlines()[1:]

            separator = all_lines.index("---\n")
            header = all_lines[:separator]
            rest = all_lines[separator:]

            attributes = {key: value for key, value in preserved_attributes.items()}

            for line in header:
                first_colon = line.index(":")
                key = line[:first_colon]
                value = line[first_colon+2:]

                if key in mapping.keys():
                    key = mapping[key]

                if key not in attributes.keys():
                    continue

                attributes[key] = value


            f.seek(0)
            f.write("---\n")
            for key, value in attributes.items():
                if value is None:
                    value = "\n"
                f.write(f"{key}: {value}")
            f.writelines(rest)

if __name__ == "__main__":
    process_to_current_page_scaffold(directory, reference_file, mapping)