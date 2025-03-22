# BERT

**BERT (Bidirectional Encoder Representations from Transformers)** is a powerful language model developed by Google, designed to improve natural language understanding.

- **Bi-directional**: BERT reads text from both left-to-right **and** right-to-left, capturing full context for better word understanding.
- **Auto-encoding**: It is an auto-encoding model that predicts missing words in a sentence based on surrounding context, unlike autoregressive models that predict the next word.
- **Encoder**: BERT uses the **encoder** from the Transformer architecture, focusing on processing input text to generate contextualized word embeddings.
- **Representation**: It relies on **self-attention**, which allows it to understand relationships between all words in a sentence, regardless of position.
- **Transformer**: The encoder, built from the **Transformer** architecture, processes text in parallel, enabling more efficient and powerful language modeling.

**NOTE:** We can pass either one or two sequences into BERT based on task.
    - 1 Sequence: If task is something like sequence classification i.e. assigning a category to a sequence of tokens.
    - 2 Sequence: If task is something like question answering where first sequence is the question and second sequence is the paragraph for context to answer the question.

---

### CLS token

The **[CLS] token** is a special token used specifically in the BERT (Bidirectional Encoder Representations from Transformers) architecture.

- **Purpose**: The [CLS] token stands for **"classification"** and is used to represent the entire input sequence as a single vector embedding.
- **Position**: It is placed at the very beginning of the input sequence during training and inference.
- **Embedding Representation**: After passing through the layers of the BERT model, the final hidden state corresponding to the [CLS] token is typically used as a summary representation of the input sequence.
- **Applications**: This representation is often used for tasks like:
  - **Text classification** (e.g., sentiment analysis, spam detection).
  - **Question answering** (the representation helps in answering the question based on context).
  - **Sequence labeling** and other downstream tasks.
  
---

### SEP token

The **SEP token** (short for **Separator** token) is indeed specific to the **BERT (Bidirectional Encoder Representations from Transformers)** architecture, which is a popular pre-trained transformer model used for natural language processing tasks.

Here’s how the SEP token works:

1. **Separator Between Sequences:**
   - In tasks like **question answering** or **sentence pair classification**, BERT often takes two sequences as input. The SEP token is used to separate these two sequences. For example, in a question-answering task, the first sequence could be the question, and the second sequence could be the context (passage). The SEP token helps the model distinguish where one sequence ends and the other begins.
2. **Usage in Input Format:**
   - When feeding input into BERT, both sequences are typically concatenated with a special token like `[CLS]` at the beginning, followed by the first sequence, then the SEP token, and finally the second sequence. For example, the input might look like this:
     ```
     [CLS] Question: What is the capital of France? [SEP] Paris is the capital of France. [SEP]
     ```
   - The `[CLS]` token is often used for classification tasks, while the `[SEP]` token helps BERT differentiate between distinct segments of the input.
3. **Positioning and Role:**
   - The SEP token plays a key role in helping BERT understand the structure of the input, allowing it to learn relationships between multiple segments. It's especially useful for tasks like **sentence similarity**, **entailment detection**, or **pair classification**, where distinguishing between multiple sequences is essential.

---

## BERT models

BERT comes in various sizes: 

- **BERT-small :**
    - ***Encoder Layers:*** 4
    - ***Learnable Parameters:*** 15 M

- **BERT-base :**
    - ***Encoder Layers:*** 12
    - ***Learnable Parameters:*** 110 M

- **BERT-large :**
    - ***Encoder Layers:*** 24
    - ***Learnable Parameters:*** 340 M

And there are many more
We can sometimes shift to a smaller model to get a speed boost if needs meet

---

## Processing word sequences for BERT

Before the word sequences are given as input to encoder stack, they are tokenized and embedded into vectors.

- **Tokens:** 
  - Words and tokens are not one and the same. 
  - Splitup of word sequence into smaller chunks is called tokenization and each chunk is called token.
  - Token may or may not be a word in the sentence.

- **Embeddings:**
- Embeddings are dense vector representations of tokens that capture semantic meaning.
- Each token is converted into a vector that represents its meaning in a higher-dimensional space, allowing the model to understand relationships between words.
- **Types of Embeddings:**
  - **Word Embeddings:** Traditional models like Word2Vec and GloVe represent each word as a fixed vector.
  - **Contextual Embeddings:** In models like BERT, embeddings are dynamic and change based on the context of the token within the sentence.
- **BERT Embeddings:**
  - In BERT, embeddings are the sum of three components:
    1. **Token Embeddings:** Each token is represented as a vector, usually learned during pretraining.
    2. **Segment Embeddings:** BERT can handle sentence pairs (e.g., Question-Answering tasks), and segment embeddings help distinguish between sentences in these pairs.
    3. **Positional Embeddings:** Since BERT is a transformer model and doesn't have a built-in understanding of the order of tokens, positional embeddings are added to capture the relative position of tokens in the sequence.

---

## Wordpiece tokenizer

This is the method used to tokenize a word sequence in BERT model.

This is done so by dividing the sequence into words that are in the tokenizer dictionary/vocabulary as it has over 30k words.
- **SEQUENCE:** "Today is a beautiful day"
- **Tokenized output:** ["[CLS]","Today","is","a","beautiful","day","[SEP]"]

In case there is any word in the sequence not in the volabulary of the tokenizer, BERT deals with that scenario by splitting the words into pieces which are included in the vocabulary.
- **SEQUENCEL** "Sinan loves to travel"
    - ***Sinan doesn't exist in the tokenizer vocabulary so it does the following tokenization.
- **Tokenized output:** ["[CLS]","Sin","##an","loves","to","travel","[SEP]"]
    - **##** indicates that the word is a subword.