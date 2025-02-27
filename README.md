Create venv:
>   python3 -m venv .myvenv

Enter in venv (inside project directory)
>    source .myvenv/bin/activate

Deactivate
>    deactivate

### Install the deps
> pip install -r requirements.txt

### Run the streamlit app
> streamlit run main.py



### Test Articles about Tata motors stock
1. https://www.livemint.com/market/live-blog/tata-motors-share-price-today-latest-live-updates-on-21-feb-2025-11740105011362.html
2. https://www.moneycontrol.com/news/business/markets/tata-motors-m-m-hyundai-motor-india-fall-up-to-6-on-reports-of-govt-easing-ev-import-rules-12947075.html
3. https://www.businesstoday.in/markets/company-stock/story/tata-motors-stock-slips-from-52-week-high-is-it-a-value-buy-465282-2025-02-20


## Key concepts

### Document Loader:
### Text Splitter:

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

- #### Embedding model: huggingface
- #### Transformers:
- #### PyTorch:


### What is RAG? 
RAG (Retrieval-Augmented Generation) is an AI framework that combines the strengths of traditional information retrieval systems (such as search and databases) with the capabilities of generative large language models (LLMs).
RAG extends the already powerful capabilities of LLMs to specific domains or an organization's internal knowledge base, all without the need to retrain the model. It is a cost-effective approach to improving LLM output so it remains relevant, accurate, and useful in various contexts.

Retrieval => retrieve the external data (knowledge base)
Generation => generate more precise, informative, and engaging responses by combining the re knowledge base with LLM

### How RAG Works ? 
1. Without RAG, the LLM takes the user input and creates a response based on information it was trained on—or what it already knows. 
2. With RAG, an information retrieval component is introduced that utilizes the user input to first pull information from a new data source. The user query and the relevant information are both given to the LLM. The LLM uses the new knowledge and its training data to create better responses.


### what is hallucinations ?


### Alternatives for FAISS vector store
- Pinecone
- Chroma
- Weaviate