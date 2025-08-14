import re

def extract_urls(text):
    # Regex pattern to match URLs (http, https, www)
    url_pattern = r'(https?://[^\s]+|www\.[^\s]+)'
    return re.findall(url_pattern, text)

# Example usage
if __name__ == "__main__":
    sample_text = """
    Visit our website at https://www.example.com or follow us at http://twitter.com/example.
    You can also check www.testsite.org for more info.
    """
    urls = extract_urls(sample_text)
    print(urls)