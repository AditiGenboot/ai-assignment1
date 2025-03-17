import requests
from bs4 import BeautifulSoup

def fetch_webpage(url):
    """Fetch the content of a webpage."""
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.text
    else:
        print("Failed to fetch the webpage. Status Code:", response.status_code)
        return None

def extract_text(html_content):
    """Extract visible text from the HTML content using BeautifulSoup."""
    soup = BeautifulSoup(html_content, 'html.parser')

    # Remove scripts and styles
    for script in soup(["script", "style"]):
        script.decompose()

    # Get text
    text = soup.get_text(separator=' ')
    return text

def find_best_match(text, query):
    """Find the sentence with the most word overlap with the query."""
    sentences = text.split(". ")  # Split text into sentences
    query_words = set(query.lower().split())  # Convert query into a set of words

    best_match = None
    max_overlap = 0

    for sentence in sentences:
        sentence_words = set(sentence.lower().split())  # Convert sentence into words
        overlap = len(query_words & sentence_words)  # Find common words

        if overlap > max_overlap:  # Update if a better match is found
            max_overlap = overlap
            best_match = sentence

    return best_match if best_match else "No relevant information found."

def main():
    url = input("Enter the URL: ")

    html_content = fetch_webpage(url)
    if not html_content:
        return

    text = extract_text(html_content)

    while True:
        query = input("\nEnter your search query (or type 'exit' to quit): ")
        if query.lower() == 'exit':
            print("Exiting...")
            break

        answer = find_best_match(text, query)
        print("\nBest matching answer:", answer)

if __name__ == "__main__":
    main()


