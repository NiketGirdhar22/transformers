# Pretraining BERT

Pre-Training is where BERT starts to stand out and it is pre-trained on 2 tasks:

- The Masked Language Model (MLM)
    - Replace 15% of words in corpus with a special [MASK] token and BERT is asked to fill it
    - Example: "Isnanbul is a great [MASK] to visit."
    - Like [CLS] and [SEP], [MASK] is one of the special tokens that BERT recognizes
    - Process:
        - Input a sequence.
        - It is converted to contextless tokens including [MASK].
        - This contextless tokenized sequence is then fed to encoder stack.
        - Encoder stack converts the contextless tokens to contextful tokens.
        - For MLM, on top of contextful representation, a FeedForward layer is added
        - FeedForward layer performs classification on all possible words in the vocabulary

- Next Sentence prediction

These 2 tasks help BERT learn how words/language works in general.

