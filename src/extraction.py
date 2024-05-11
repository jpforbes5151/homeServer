import re

def extract_markdown_images(text):
    if text is None:
        raise ValueError("No Text has been submitted to be parsed.")
    parsed = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return parsed

#text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
#print(extract_markdown_images(text))
# expected output: [("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")]


def extract_markdown_links(text):
    if text is None:
        raise ValueError("No Text has been submitted to be parsed.")
    parsed = re.findall(r"\[([^\]]+)\]\(([^)]+)\)", text)
    return parsed

#text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
#print(extract_markdown_links(text))
#expected output:  [("link", "https://www.example.com"), ("another", "https://www.example.com/another")]