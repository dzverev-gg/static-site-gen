from prepare_public import prepare_public
from generate_page import generate_pages_recursively


def main():
    prepare_public()
    generate_pages_recursively("content/", "template.html", "public/")


main()
