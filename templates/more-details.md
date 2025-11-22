1. ### Document Loader:
Provides the initial input for further processing, such as splitting and embedding.
2. ### Text Splitter: 
Breaks documents into manageable chunks for efficient processing and retrieval.
##### Why chunking?

- **Fits within memory/compute limits**: Large documents can overwhelm memory or cause slow processing. Splitting into smaller chunks makes handling data more manageable for both storage and compute.
- **Improved search and retrieval**: Vector databases (like FAISS, Pinecone, Chroma) operate more efficiently when content is indexed as smaller, focused chunks, which improves retrieval of the most relevant information.
- **Prevents context loss for LLMs**: LLMs (Large Language Models) have input size limits. Feeding smaller chunks avoids truncating important information and improves the quality of generated answers.
- **Faster & parallel processing**: Processing smaller chunks enables faster batch and parallel operations versus a single large block of text.
- **Granular reference & source tracing**: Small chunks make it easier to identify, attribute, and cite specific information sources when answering queries.


##### Fixed Size Splitting vs RecursiveCharacterTextSplitter 
Fixed Size Splitting: can cut words at mid
RecursiveCharacterTextSplitter Splits intelligently, trying paragraphs → sentences → words. Best for LLMs.
→ Chunk overlap for Maintaining Context


3. ### Embedding 
Embeddings convert text into numerical vectors for efficient search and retrieval (e.g., using HuggingFace's sentence-transformers). For example, HuggingFace's `all-MiniLM-L6-v2` model turns sentences into embeddings for document similarity search.

- #### Embedding model: huggingface
- #### Transformers: 
Transformers are powerful neural network architectures that use attention mechanisms to understand the context of text. They generate contextualized embeddings, which are numerical representations of text that capture semantic meaning.
    ##### How Transformers Create Embeddings:

	- **Tokenization**: The input text is first broken down into smaller units called tokens (words or subwords).

	- **Input Embedding**: Each token is converted into an initial embedding vector.

	- **Transformer Layers**: The sequence of token embeddings is then passed through multiple layers of transformer blocks. 
		- self-attention mechainism: Every token **attends** to all other tokens in the sequence. Every token is assigned weight (attention scores) based on its importance.
		- Feedforward Layers: <to add>
	- **Contextualized Embeddings**: The transformer layers refine the initial token embeddings, creating contextualized embeddings. This means that the embedding for a word depends on the surrounding words in the sentence. For example, the word "bank" will have a different embedding in the sentence "I deposited money in the bank" than in the sentence "The river bank was eroding."

	- **Pooling (for sentence embeddings)**: For sentence embeddings, a pooling operation is often applied to the contextualized token embeddings to create a single vector representation of the entire sentence. Common pooling methods include:

		1. Mean Pooling: Averages the token embeddings.

		3. Max Pooling: Takes the maximum value across each dimension of the token embeddings.

		5. CLS Token: Some models (like BERT) have a special "CLS" token at the beginning of the input sequence. The embedding of this token is often used as the sentence embedding.
- #### PyTorch:


4. ### RAG 
RAG (Retrieval-Augmented Generation) is an AI approach that integrates information retrieval (such as searching a database or document collection) with generative large language models (LLMs). Instead of relying solely on what the LLM "knows" from its pretraining, RAG first retrieves relevant external documents and then passes them, along with the user query, to the LLM. This enables the LLM to generate more up-to-date, accurate, and context-aware responses, especially when dealing with domain-specific or proprietary knowledge.
   
RAG extends the already powerful capabilities of LLMs to specific domains or an organization's internal knowledge base, all without the need to retrain the model. It is a cost-effective approach to improving LLM output so it remains relevant, accurate, and useful in various contexts.

Retrieval => retrieve the external data (knowledge base)
Generation => generate more precise, informative, and engaging responses by combining the re knowledge base with LLM

#### How RAG Works ? 
**Without RAG**, the LLM takes the user input and creates a response based on information it was trained on—or what it already knows. 
**With RAG**, an information retrieval component is introduced that utilizes the user input to first pull information from a new data source. The user query and the relevant information are both given to the LLM. The LLM uses the new knowledge and its training data to create better responses.


### what is hallucinations ?


### Alternatives for FAISS vector store
- Pinecone
- Chroma
- Weaviate