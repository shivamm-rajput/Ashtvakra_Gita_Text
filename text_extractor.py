import requests
import re
import json

# URL of the GRETIL plain text version of the Ashtavakra Gita
SOURCE_URL = "https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/plaintext/sa_aSTAvakragItA.txt"

def download_text(url):
    """Download the raw text from the given URL."""
    try:
        res = requests.get(url)
        if res.status_code == 200:
            return res.text
        else:
            print("Failed to fetch text. Status code:", res.status_code)
            return ""
    except Exception as e:
        print("Error fetching text:", e)
        return ""

def parse_verses(text):
    """
    Extract verses and their indices.
    Each verse ends with something like: // Avg_1.5
    """
    verse_list = []

    # To match two lines followed by // Avg_1.5
    matches = re.findall(r"([^\n]+)\n([^\n]+)\s+// Avg_(\d+\.\d+)", text)

    for first_line, second_line, index in matches:
        verse = {
            "verse": f"{first_line.strip()}\n{second_line.strip()}",
            "index": index
        }
        verse_list.append(verse)

    return verse_list

def write_to_file(data, filename="ashtavakra_verses.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Saved {len(data)} verses to {filename}")

def main():
    print("Downloading Ashtavakra Gita text...")
    raw_text = download_text(SOURCE_URL)

    if not raw_text:
        print("No text to process.")
        return

    print("Parsing verses...")
    verses = parse_verses(raw_text)

    print("Writing to JSON...")
    write_to_file(verses)

if __name__ == "__main__":
    main()