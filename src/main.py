import os
import shutil
from markdown_to_html_node import markdown_to_html_node
from extract_title import extract_title

src_dir = "static"
dest_dir = "public"

def main():
    # 1) Clean public directory
    copy_content()
    # 2) Generate index page
    generate_page(
        from_path="content/index.md",
        template_path="template.html",
        dest_path="public/index.html",
    )

def copy_content():
    if os.path.isdir(dest_dir):
        shutil.rmtree(dest_dir)
    os.mkdir(dest_dir)
    current_dir = src_dir
    copy_files_and_folder(current_dir)
    


def copy_files_and_folder(current_dir):
    if os.path.isdir(current_dir):
        print(os.listdir(current_dir))
        for file in os.listdir(current_dir):
            file_handle = current_dir + "/" + file
            if os.path.isdir(file_handle):
                os.mkdir(file_handle.replace(src_dir, dest_dir))
                copy_files_and_folder(file_handle)
            else:
                shutil.copy(file_handle, file_handle.replace(src_dir, dest_dir))


def generate_page(from_path: str, template_path: str, dest_path: str):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    # Read markdown
    with open(from_path, "r", encoding="utf-8") as f:
        markdown = f.read()

    # Read template
    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()

    # Convert markdown to HTML and extract title
    html_node = markdown_to_html_node(markdown)
    html_content = html_node.to_html()
    title = extract_title(markdown)

    # Replace placeholders
    output_html = template.replace("{{ Title }}", title).replace("{{ Content }}", html_content)

    # Ensure directory exists
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    # Write output
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(output_html)


main()
