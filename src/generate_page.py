from markdown_to_html import markdown_to_html_node, extract_title
import os


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as f:
        md = f.read()
        f.close()
    with open(template_path, "r") as f:
        template = f.read()
        f.close()
    html_node = markdown_to_html_node(md)
    html_text = html_node.to_html()
    title = extract_title(md)
    result_html = template.replace("{{ Title }}", title)
    result_html = result_html.replace("{{ Content }}", html_text)
    if not os.path.exists(os.path.dirname(dest_path)):
        os.makedirs(os.path.dirname(dest_path))
    with open(dest_path, "w") as f:
        f.write(result_html)
        f.close()

    return


def generate_pages_recursively(dir_path_content, template_path, dest_dir_path):
    files = os.listdir(dir_path_content)
    for file in files:
        from_path = os.path.join(dir_path_content, file)
        dest_path = os.path.join(dest_dir_path, file.replace(".md", ".html"))
        if os.path.isfile(from_path) and ".md" in file:
            generate_page(from_path, template_path, dest_path)
        else:
            os.mkdir(dest_path)
            generate_pages_recursively(from_path, template_path, dest_path)

    return
