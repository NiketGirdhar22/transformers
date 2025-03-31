# GPT

GPTs (Generative Pre-trained Transformers) 

- Auto-regressive language models i.e it predicts tokens based on the past contexts.
- Decoders are trained on huge corpora of data
- Decoders are used from the transformers architecture

---

## GPT models

- ***GPT-1*** .117B parameters
- ***GPT-2*** 1.5B parameters
    - **GPT-2 Small** 117M parameters
    - **GPT-2 Medium** 345M parameters
    - **GPT-2 Large** 762M parameters
    - **GPT-2 Extra Lagre** 1542M parameters
- ***GPT-3*** 175B parameters

---

## How GPT works?

GPT and BERT are similar in the sense that they both use [Scaled Dot Product Attention](how_transformers_use_attention.md) to infuse context into the tokens.

For GPT we work explicitly for decoders instead of encoders which was the case for BERT

---

## GPT Tokenization

GPT has Byte-level tokenization as compared to BERT's wordpiece tokenization:

***Sample Sequence:*** I am Niket Girdhar

***Tokenized Sequence:*** ["I","am","Niket""Girdhar","<|endoftext|>"] `This is just a sample and not the actual tokenization.`

`<|endoftext|>` is a special token that is used to indicate the end of sentence.

The tokenization happens by splitting the list of tokens into the vocabulary of over 50,000 words and adding `<|endoftext|>` token in end.

GPT's tokenizatuon also uses the simialar format to BERT for dealing with unknown tokens i.e. break them into smaller chunks.


---

## Code

[Experimenting with GPT architecture in python](codes/gpt/gpt.ipynb)