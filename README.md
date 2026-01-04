## CrediTrust Financial Complaint Intelligence System

## Project Overview

CrediTrust Financial is a financial services provider offering products such as credit cards, savings accounts, personal loans, and money transfer services. Like many institutions in the financial sector, CrediTrust receives a large volume of consumer complaints that contain valuable insights into customer pain points, recurring issues, and operational risks.

This project aims to build a **Complaint Intelligence System** that leverages natural language processing and vector-based retrieval to enable semantic analysis and question answering over consumer complaint narratives. The system is designed to support internal teams by surfacing trends, identifying problem areas, and enabling evidence-based decision-making.

---

## Project Objectives

The main objectives of this project are to:

- Explore and understand a large-scale consumer complaint dataset
- Clean and preprocess unstructured complaint narratives for semantic analysis
- Normalize inconsistent product labels into canonical categories
- Prepare the data for embedding and vector database storage
- Enable semantic search and question answering over complaints in later stages

---

## Dataset Description

The dataset used in this project is sourced from the **Consumer Financial Protection Bureau (CFPB)** and contains approximately **9.6 million consumer complaints** across various financial products.

Key characteristics of the dataset:

- 21 unique product labels with overlapping semantics
- A large proportion of complaints do not include free-text narratives
- Complaint narratives vary significantly in length, from very short entries to long, detailed descriptions
- Product labeling inconsistencies require normalization before analysis

The primary field of interest for this project is the **Consumer complaint narrative**, which provides unstructured textual descriptions of consumer issues.

---

## Project Tasks and Workflow

### Task 1: Exploratory Data Analysis and Preprocessing

Task 1 focuses on understanding the data and preparing a high-quality text corpus for downstream tasks.

Key steps performed:

- Initial exploratory data analysis to inspect dataset structure, columns, and missing values
- Analysis of complaint distribution across all product categories
- Identification of the number of complaints with and without narratives
- Calculation and visualization of complaint narrative lengths using word counts
- Canonical normalization of product labels to address inconsistent naming
- Filtering the dataset to include only the target product categories:
  - Credit card
  - Personal loan
  - Savings account
  - Money transfers
- Removal of records with empty complaint narratives
- Cleaning of text narratives, including:
  - Lowercasing
  - Removal of CFPB PII masking tokens
  - Removal of common boilerplate phrases
  - Filtering of non-semantic characters
  - Whitespace normalization

The output of Task 1 consists of filtered raw and cleaned datasets that are suitable for embedding and retrieval tasks.

---

### Task 2: Embedding and Vector Store Preparation

Task 2 focuses on transforming cleaned complaint narratives into dense vector representations and preparing them for semantic retrieval.

Planned activities include:

- Validation or regeneration of text embeddings
- Analysis of embedding dimensionality and quality
- Preparation of data for storage in a vector database
- Initialization of a ChromaDB vector store

This task builds directly on the cleaned and normalized output from Task 1.

---

### Task 3: Semantic Search and Question Answering

Task 3 aims to enable natural language querying of consumer complaints.

Key goals include:

- Implementing semantic search over complaint embeddings
- Supporting natural language questions about customer issues
- Demonstrating how the system can surface insights across products
- Highlighting the business value of semantic complaint analysis

---

## Repository Structure
```
├── ChromaDB
│ └──vectir_store
├── data
│ ├── raw
│ │ └── complaints.csv
│ └── processed
│ ├── filtered_complaints_raw.csv
│ └── filtered_complaints_clean.csv
├── notebooks
│ └── eda_preprocessing.ipynb
├── README.md
├── requirements.txt
```

---

## Environment and Reproducibility

- Python version: **3.10.x**
- Key libraries include:
  - pandas
  - numpy
  - matplotlib
  - seaborn
  - regex-based text processing libraries

To install dependencies:

```bash
pip install -r requirements.txt
```
*The project notebooks are designed to be run sequentially, starting with exploratory analysis and preprocessing.*

### Key Design Decisions

Canonical product normalization was used instead of direct string matching to handle inconsistent product labels.

Buy Now, Pay Later (BNPL) is not treated as a standalone product in Task 1 because it does not exist as an explicit CFPB product label. BNPL-related complaints are expected to be identified through semantic analysis in later tasks.

Raw and cleaned narratives are stored separately to preserve traceability while optimizing storage and downstream processing.

Limitations and Future Improvements

Canonical product mapping is rule-based and may miss ambiguous edge cases

Complaint narratives vary significantly in length and may require chunking during embedding

Some residual boilerplate or implicit sensitive information may remain despite cleaning

These limitations will be addressed progressively in Tasks 2 and 3.

Status

Task 1: Completed

Task 2: In progress

Task 3: Planned

Task 4: Planned

Author
Yonatan ML engineer 