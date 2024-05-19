# BINI-Chat Data Pipeline 🏗️

The Bini-Fan Data Pipeline is a specialized system designed to scrape, process, and query data from a fan wiki page dedicated to the girl group BINI. The pipeline leverages various advanced AI and data processing technologies to ensure the relevance and accuracy of responses. This document outlines the modules and technologies used in the pipeline.

## Features 🌟

### Data Collection and Ingestion

- **Web Scraping**: The pipeline begins by scraping text data from various pages of the BINI fan wiki using the `requests` and `BeautifulSoup` modules. The scraped data is then saved as individual text files.

### Data Processing and Conversion

- **Text to PDF Conversion**: The collected text files are converted into PDF format using the `pdfkit` library, allowing for better document management and compatibility with subsequent processing steps.
- **PDF Processing**: The PDF files are processed using the `PyMuPDF` library and `LlamaParse` to extract and structure the textual data. This structured data is then prepared for indexing and querying.

### Indexing and Storage

- **Node Parsing**: The extracted text is parsed into smaller nodes using `SimpleNodeParser` from `Llama Index`. These nodes form the basis for creating a searchable index.
- **Vector Store Creation**: The parsed nodes are embedded into vector representations using the `OpenAIEmbedding` model, which captures the semantic meaning of the text beyond simple keyword matching. These embeddings are stored in a `Pinecone` vector store, ensuring efficient and scalable search capabilities.
- **Index Management**: The `Pinecone` vector store is managed using the `Pinecone` module, with a serverless setup to ensure smooth operation without requiring extensive infrastructure management.

### Query Processing

- **Hybrid Search**: The pipeline employs a hybrid search approach, combining traditional keyword-based search with vector-based semantic search to deliver highly relevant results. The querying is handled by a `VectorStoreIndex` initialized with the vector store and embedding model.
- **Query Interface**: A `Streamlit`-based user interface facilitates user interaction, allowing users to submit queries and receive responses directly from the indexed data.

## Module Overview 📦

- **requests and BeautifulSoup**: For web scraping and extracting text data from web pages.
- **pdfkit**: For converting text files into PDF format.
- **PyMuPDF**: For processing PDF files and extracting textual content.
- **tqdm**: For displaying progress bars during data processing steps.
- **LlamaParse**: For loading and processing PDF data into structured formats.
- **SimpleNodeParser and SentenceSplitter**: For parsing text into nodes suitable for indexing.
- **OpenAIEmbedding**: For generating vector embeddings of text data.
- **PineconeVectorStore**: For storing and managing vector embeddings.
- **Streamlit**: For creating an interactive user interface.

## Cloud Setup and Infrastructure ☁️

- **Pinecone**: The vector store is hosted on Pinecone, utilizing a serverless setup to ensure scalability and efficiency.
- **API Integration**: The pipeline integrates with OpenAI and Pinecone APIs to leverage their advanced AI and storage capabilities.

## Usage Scenarios 🎯

The Bini-Fan Data Pipeline is designed for fans and researchers interested in detailed information about the BINI girl group. It provides an efficient way to query and retrieve relevant data from a comprehensive fan wiki, ensuring users get accurate and contextually relevant information.

## Future Enhancements 🔮

- **Scalability Improvements**: Transitioning to more scalable storage solutions as the dataset grows.
- **Performance Metrics**: Implementing mechanisms to measure and optimize the performance of the data pipeline.
- **User Feedback**: Exploring ways to incorporate user feedback into the query results to continuously improve relevance and accuracy.

This README provides an overview of the Bini-Fan Data Pipeline, emphasizing the modules and technologies used to build a robust and efficient data querying system.
