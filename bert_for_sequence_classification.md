# Fine-tuning BERT for sequence classification

![BERT for sequence classification](images/seq_classification_bert.png)

## Steps to be followed:

- Take a pre-trained BERT.
- Feed a single sequence to the pre-trained model.
- The output of sequece when passed through pre-trained BERT will be a tokenzied sequence.
- Just consider the representation of the [CLS] token as it contains the overall context for the entire sequence in the NSP task using the pooler attribute.
- Add another FeedForward layer after the pooler to map it to any n number of  classes the user wants.
- **Example:**
    - ***Sequence -*** "Istanbul is a great city"
    - ***Sequence classes -*** Positive / Negative

## Code

[Implementation of Sequence Classification for BERT in Python](bert_seq_classification.ipynb)