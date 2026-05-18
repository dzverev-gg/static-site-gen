from prepare_public import prepare_struct
from generate_page import generate_pages_recursively
import sys


def main():
    if len(sys.argv) > 1:
        base_path = sys.argv[1]
    else:
        base_path = "/"

    prepare_struct("docs/")
    generate_pages_recursively("content/", "template.html", "docs/", base_path)


main()
