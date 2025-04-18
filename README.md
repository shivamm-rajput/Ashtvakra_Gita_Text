# Text Extractor

This project is a Python-based text extractor designed to download, parse, and save verses from the Ashtavakra Gita. The text is sourced from the GRETIL plain text version, and the extracted verses are saved in a JSON format.

## Features

- Download text from a specified URL.
- Parse verses and their indices from the downloaded text.
- Save the extracted verses to a JSON file.

## Installation

To set up the project, you need to have Python installed on your machine. You can then install the required dependencies using pip.

1. Clone the repository:
   ```
   git clone <repository-url>
   cd text-extractor
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the text extractor, execute the following command in your terminal:

```
python src/text_extractor.py
```

This will download the Ashtavakra Gita text, parse the verses, and save them to a file named `ashtavakra_verses.json`.

## Dependencies

- `requests`: For making HTTP requests to download the text.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.