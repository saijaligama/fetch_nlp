
# Fetch Intelligent Search Tool

## Overview
The Fetch Intelligent Search Tool is a web-based application aimed at providing users the ability to search for offers intelligently using a text input. The tool leverages fuzzy string matching techniques to suggest relevant offers based on user queries.

## Features
- **Web-based Interface**: Allows users to enter their search queries easily.
  
- **Fuzzy String Matching**: Implemented using the FuzzyWuzzy Python library to find the most similar category, brand, or retailer to the given input.

- **Intelligent Suggestions**: The tool prioritizes suggestions based on similarity scores, making sure users get the most relevant offers.

## Technical Stack
- **Backend**: Python with Flask for web serving.
  
- **String Matching**: FuzzyWuzzy for approximate string matching.

- **Data Source**: CSV files containing data about brand categories, categories, and offer retailers.

## Getting Started

The application should be live on http://18.209.174.175:8000/ 
this should be live untill 08/31/2023 

Or else

1. **Clone the repository**:
   ```
   git clone https://github.com/saijaligama/fetch_nlp
   ```

2. **Navigate to the project directory**:
   ```
   cd [project-directory-name]
   ```

3. **Install required libraries**:
   ```
   pip install -r requirements.txt
   ```

4. **Run the tool**:
   ```
   python main.py
   ```
   The application will start running on `http://127.0.0.1:8005/`.

## Using the Tool
- Open a web browser and navigate to `http://127.0.0.1:8005/`.
  
- Enter a search term (category, brand, or retailer) into the provided input box.
  
- The application will provide a list of relevant offers based on the entered term, alongside the similarity score.

## Future Enhancements
Advanced NLP Techniques: Implement sophisticated NLP techniques for a more context-aware search. This will help in:
Semantic Search: Understand the intent behind user queries by embedding both the search terms and offers into a semantic space using models like BERT or Word2Vec. This can capture deeper contextual meanings and provide more relevant results.

Named Entity Recognition (NER): Extract specific entities like brand names, product types, and more from user queries. This can refine the search process, especially when users provide longer or more complex queries.

Query Expansion: Expand user queries with synonyms or related terms to broaden the search horizon and capture more potential offers. For instance, if a user searches for "soda", the tool can also look for offers related to "cola", "soft drink", and "carbonated beverage".

Spell Check and Correction: Integrate a spell-checking mechanism to handle and correct potential typos or misspellings in user queries, ensuring they still get relevant results.

Live Database Integration: Transition from static CSV files to a live database for real-time, up-to-date offers and faster query processing.
## Notes
Make sure to have your CSV datasets (`brand_category.csv`, `categories.csv`, `offer_retailer.csv`) present in the `static/data/` directory.

---

Please replace placeholders (like `[URL-of-your-GitHub-repository]`) with actual details. This README provides a clear introduction to your project, a brief overview of its features, technical details, and instructions on how to set it up and use it.
