# Attention and Language Models

## Introdiction to NLP
Natural Language Processing (NLP) is a field within Artificial Intelligence (AI) focused on enabling computers to interpret, understand, and interact with human language in a way that is both meaningful and useful.

NLP combines:
- ***Computational Linguistics:*** which involves designing rule-based models for parsing and understanding human language.
- ***Machine Learning (ML):*** which allows systems to improve over time by learning patterns from large datasets of human language.

Computer tends to understand the text by converting the to a vector of numbers called embeddings

---

## Word embeddings

Word embeddings are a way of representing words as vectors in a high-dimensional space. These vectors are learned from large text corpora, and words that have similar meanings are positioned near each other in the vector space.

- ***Example:*** The words "king" and "queen" would be closer to each other than "king" and "dog" in the embedding space.
- ***Why is it important?*** Embeddings preserve the semantic relationships between words, allowing algorithms to perform tasks like analogies (e.g., "man" is to "woman" as "king" is to "queen") and clustering (e.g., grouping similar words together).

The main challenge with word embeddings is that they are influenced by the biases in the training data.
***The algorithm used to learn text embeddings: Word2Vec, GloVe etc.***

---

## Bias in large text corpora

Bias in NLP systems can emerge both directly and indirectly, and it is critical to understand these forms of bias as they can lead to unfair, stereotypical, or harmful outcomes.

- ***Direct Bias:*** Say terms like sports are inherently closer to male words where murse / air hostess is closer to female words
- ***Indirect Bias:*** More nuanced correlations in the learned embeddings leading to teacher being closer to volleyball than football, due to their larger female associations.

---

## Attention

