import os
import shutil
from markdown_to_html_node import markdown_to_html_node
from extract_title import extract_title

src_dir = "static"
dest_dir = "public"

def main():
    # 1) Clean public directory
    copy_content()
    # 2) Generate all pages recursively
    generate_pages_recursive(
        dir_path_content="content",
        template_path="template.html",
        dest_dir_path="public"
    )
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    """
    Recursively crawl dir_path_content, generate HTML files for each markdown file using template_path,
    and write them to dest_dir_path, preserving directory structure.
    """
    for root, dirs, files in os.walk(dir_path_content):
        for file in files:
            if file.endswith(".md"):
                md_path = os.path.join(root, file)
                # Compute relative path from content dir
                rel_path = os.path.relpath(md_path, dir_path_content)
                # Change .md to .html
                html_filename = os.path.splitext(rel_path)[0] + ".html"
                dest_path = os.path.join(dest_dir_path, html_filename)
                generate_page(
                    from_path=md_path,
                    template_path=template_path,
                    dest_path=dest_path
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
