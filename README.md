Create venv:
    python3 -m venv .myvenv
Enter in venv (inside project directory)
    source health_venv/bin/activate

Deactivate
    deactivate

## Install the deps
pip install -r requirements.txt

## How to launch JupyterLab with:
jupyter lab


## How to launch Jupyter notebook with:
jupyter notebook

### 5. Run the streamlit app
> streamlit run main.py



# vector dbs
1. Pinecone
2. Chroma
3. Weaviate

# Articles:
1. https://www.livemint.com/market/live-blog/tata-motors-share-price-today-latest-live-updates-on-21-feb-2025-11740105011362.html
2. https://www.moneycontrol.com/news/business/markets/tata-motors-m-m-hyundai-motor-india-fall-up-to-6-on-reports-of-govt-easing-ev-import-rules-12947075.html
3. https://www.businesstoday.in/markets/company-stock/story/tata-motors-stock-slips-from-52-week-high-is-it-a-value-buy-465282-2025-02-20


### Key concepts
## 1. Loader
## Text Splitter module:
    1. Fixed Size Splitting vs RecursiveCharacterTextSplitter 
        Fixed Size Splitting: can cut words at mid
        RecursiveCharacterTextSplitter Splits intelligently, trying paragraphs → sentences → words. Best for LLMs.
    2. chunk overlap for Maintaining Context
    Why ?
    Token Limit: LLMs have a maximum token limit (e.g., GPT-3.5 ~16K tokens, GPT-4 ~128K tokens).
    Efficient Retrieval: When storing text in a vector database (FAISS, Pinecone, Chroma), splitting helps retrieve relevant chunks efficiently.
    Better Context for LLMs: If the input text is too large, it gets truncated by the model. Smaller chunks ensure the model receives complete, meaningful content.

    Q & A:
    Why Split Text?
    → LLMs have token limits, and smaller chunks improve retrieval & performance.
    What Does RecursiveCharacterTextSplitter Do?
    → Splits intelligently (paragraphs → sentences → words).
    Why chunk_overlap?
    → Preserves context across chunks, preventing missing info.


### Embedding
Embeddings are useful when you need to search, compare, or retrieve information from a large set of documents efficiently.