# PubMed JSON Data Extractor

The PubMed JSON Data Extractor is a Python program that allows you to extract JSON data from PubMed articles and convert it into HTML format. This can be particularly useful for researchers and developers who need to process and present PubMed article data in a more accessible and structured way.

## Installation

To use the PubMed JSON Data Extractor, follow these steps:

1. Clone the GitHub repository to your local machine using the following command or by downloading the repository as a ZIP file and extracting it:

   ```bash
   git clone https://github.com/vishal-ravi/PubMedJsonDataExtractor.git
   ```

2. Download the JSON file of the PubMed article you want to process. Visit the following URL, replacing `[PMCid]` with the actual PMC ID of the article:

   ```
   https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_xml/[PMCid]/unicode
   ```

   This will download the JSON file for the article. Rename the downloaded JSON file to `inputs.json`.

3. Copy the `inputs.json` file to the program directory (where the `PubMedJsonDataExtractor.py` file is located).

Your program directory structure should now look like this:

```
PubMedJsonDataExtractor/
├── PubMedJsonDataExtractor.py
├── inputs.json
└── README.md
```

## Usage

1. Ensure you have Python 3.x installed on your machine.

2. Open a terminal or command prompt and navigate to the program directory:

   ```bash
   cd /path/to/PubMedJsonDataExtractor
   ```

3. Run the program using the following command:

   ```bash
   python PubMedJsonDataExtractor.py
   ```

4. The program will process the `inputs.json` file and generate an HTML file containing the extracted data.

5. Open the generated HTML file in a web browser to view the extracted data in a structured format.

## Contributing

Contributions are welcome! If you find any issues or would like to suggest improvements, please feel free to open an issue or submit a pull request on the [GitHub repository](https://github.com/vishal-ravi/PubMedJsonDataExtractor).

## License

This project is licensed under the [MIT License](LICENSE).

---

Feel free to reach out to the project owner, Vishal Ravi, with any questions or feedback. You can also explore the [GitHub repository](https://github.com/vishal-ravi/PubMedJsonDataExtractor) for more information and updates.
