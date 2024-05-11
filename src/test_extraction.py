import unittest

from extraction import(
    extract_markdown_images,
    extract_markdown_links,
)

class TestExtractionMethods(unittest.TestCase):
    def eq_markdown_images(self):
        text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
        want = [("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")]
        got = extract_markdown_images(text)
        self.assertEqual(want, got)

    def eq_markdown_links(self):
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        want = [("link", "https://www.example.com"), ("another", "https://www.example.com/another")]
        got = extract_markdown_links(text)
        self.assertEqual(want, got)

    def test_extract_markdown_links_no_links(self):
        text = "This is plain text with no links."
        got = extract_markdown_links(text)
        want = []
        self.assertEqual(got, want)

    def test_extract_markdown_links_empty_input(self):
        text = ""
        got = extract_markdown_links(text)
        want = []
        self.assertEqual(got, want)

    def test_extract_markdown_links_none_input(self):
        with self.assertRaises(ValueError):
            extract_markdown_links(None)

if __name__ == "__main__":
    unittest.main()