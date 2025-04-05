# Pre-Training GPT

As GPT is auto-regressive, hence the pre-training tasks in BERT are not suitable for it:

### 1. **Masked Language Model (MLM) in BERT vs. Autoregressive in GPT**:
   - **BERT (Masked Language Model)**: In BERT, a portion of the input tokens is randomly masked, and the model is trained to predict those masked tokens. Since BERT processes text bidirectionally (i.e., it looks at the context on both sides of the masked word), it learns the meaning of a token by considering both its left and right context.
   - **GPT (Autoregressive)**: GPT, on the other hand, generates tokens one by one in a left-to-right manner. It predicts the next token in the sequence, conditioning only on the tokens to the left. This is a key difference: GPT doesn't need to mask tokens, as its training objective is simply to predict the next token given the previous context.

### 2. **Next Sentence Prediction (NSP) in BERT vs. GPT's Training**:
   - **BERT (Next Sentence Prediction)**: BERT was trained with a task where it was given pairs of sentences and had to predict if the second sentence followed the first in the original text. This task was designed to help BERT understand relationships between sentences and is particularly useful for tasks like question answering and natural language inference.
   - **GPT**: GPT does not have the need for NSP since it is autoregressive and focuses on predicting the next token in a sequence. There's no inherent need to understand the relationship between two separate sentences because the model generates text sequentially without any notion of sentence boundaries or adjacent sentence tasks.

## Pretraining for GPT

GPT is pretrained on auto-regressive language model task with a dataset - WebText(large text corpora - 40GB text).

