# Derivatives of BERT / Flavors of BERT

BERT architecture was the base for various derivative architectures. Few popular BERT derivative architectures are:

- **RoBERTa:**
    - Robistly Optimized BERT Approach
    - It claims that BERT is under-trained
    - RoBERTa training data = 10x BERT training data ***(Training)***
    - Addition of parameters: 15% ***(Architecture)***
    - Removal of NSP task. ***(Training)***
    - Dynamic Masking Pattern which is 4x the masking tasks to learn from. ***(Training)***

- **DistilBERT:**
    - ***Distillation*** is a training technique where a **student** model is to replicate a **teacher** model.
    - 40% lesser parameters ***(Architecture)***
    - 60% faster ***(Architecture)***
    - 97% equivalent to BERT's performance ***(Architecture)***
    - Training done using knowledge distillation ***(Training)***

- **ALBERT:**
    - A Light BERT
    - 90% fewer parameters
    - Factorize the token embeddings to make them much smaller (Factorized embedding parameterization) ***(Architecture)***
    - Cross-Layer parameter sharing ***(Architecture)***
    - NSP task becomes the Sentence Order Prediction task (SOP) ***(Training)***
        - SOP: Takes in 2 consecutive parts of the same document as a positive class. Then swap the order to use it as a negative example
        - ***Example:*** We have 2 sentences S1 and S2, For the training the order S1 - S2 will be considered Yes and S2 - S1 will be considered No.


Each derivative tends to enhance BERT by either altering its architecture and/or its pre-training.

--- 

## Codes

- [Implementing derivative architectures using Python](codes/bert_derivatives.ipynb)