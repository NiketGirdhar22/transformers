# MLOps

MLOps is built on top of traditional Devops principles of system-wide Automation + Testing

It extends Devops principles to provide similar tools and ideas to test + automate data pipelines as well as model training + serving

---

### Model registeries

Model registeries are important to keep models versioned whcih can come in handy when `rolling back` is included. 

Example: mlflow on databricks

- Versioning is important due to **Drift**
    - Drift means change in data, enviornment and/or model

---

## **Types of Drift**

**1. Concept Drift**

* **Definition**: Change in the relationship between input features and the target variable, i.e., a shift in **P(Y | X)**.
* **Example**:

  * Before 2020: The term *"Corona"* commonly referred to a **beer** brand.
  * After 2020: The same term became widely associated with the **COVID-19 virus**.
* **Impact**: The meaning or behavior associated with certain features changes, affecting how the model should interpret inputs.

**2. Prediction Drift**

* **Definition**: Change in the model’s predictions for the same input distribution, i.e., a shift in **P(Ŷ | X)** (Ŷ = predicted label).
* **Cause**: Often occurs when the model encounters edge cases or scenarios it was not trained for.
* **Impact**: The model might appear "broken," even though the underlying data hasn't changed, simply because it wasn’t equipped to handle new patterns.

**3. Label Drift**

* **Definition**: Change in the distribution of the **true labels**, i.e., a shift in **P(Y)**.
* **Example**:

  * Day 1: Customers ask for refunds (label: *refund request*).
  * Day 3: Customers ask about the **status** of refunds (label: *refund inquiry*).
  * Day 5: Refunds are completed and support questions decrease.
* **Impact**: Even with consistent input features, the prevalence of certain classes or intents may shift over time.

**4. Data Drift (Feature Drift)**

* **Definition**: Change in the distribution of input features, i.e., a shift in **P(X)**.
* **Example**:

  * A model trained on data from desktop users starts receiving more mobile user data.
* **Impact**: The model may underperform unless retrained or updated with data that reflects the new distribution.

---

Here’s a structured and expanded version of your **“Detecting Drifts”** section, detailing both **explicit** and **implicit** checking methods:

---

## **Detecting Drifts**

To maintain reliable machine learning models in production, it's important to monitor for drifts and performance degradation. Drift detection methods fall into two broad categories:

### **1. Explicitly Checking**

These are **direct methods** that actively test for changes in data or model behavior.

**Statistical Tests**

* Use statistical tests to compare distributions over time.
* Examples:

  * **Kolmogorov-Smirnov test**: For continuous data drift detection.
  * **Chi-squared test**: For categorical features.
  * **Jensen-Shannon Divergence / KL Divergence**: For comparing probability distributions.

**Drift Detection Algorithms**

* Dedicated algorithms to detect concept or data drift:

  * **DDM (Drift Detection Method)**
  * **ADWIN (Adaptive Windowing)**
  * **Page-Hinkley Test**
  * **EARLIEST (Early Drift Detection Method)**

**Monitoring Feature Distributions**

* Periodically compare feature distributions (e.g., histograms) from:

  * **Training data**
  * **Live/production data**

**Label Monitoring**

* If ground truth labels are available with delay, track changes in:

  * Label distribution (label drift)
  * Model accuracy, precision, recall, etc.

### **2. Implicitly Checking**

These are **indirect methods** that flag potential drift based on performance or behavioral anomalies.

**Performance Monitoring**

* Track model metrics over time:

  * Accuracy, F1 score, ROC-AUC, etc.
* A sharp decline may indicate concept or data drift.

**Prediction Distribution Shift**

* Compare distributions of predicted classes/values over time.
* Sudden or gradual shifts can indicate:

  * Label drift
  * Data drift

**Feedback Loops**

* Use user interaction or post-deployment feedback (e.g., chatbot thumbs-up/down, support tickets) to infer model misalignment.

**Shadow Models**

* Run a **shadow model** (new version) alongside the current one.
* Compare predictions to identify divergence in behavior over time.

**Alert Systems & Thresholds**

* Set thresholds for certain metrics (e.g., drift score, prediction variance).
* Trigger alerts if thresholds are exceeded.