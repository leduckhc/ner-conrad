# Problem Description

Imagine that we would like to deliver a new feature for enhancing our sellers' journey when onboarding new products on our Conrad Marketplace.

For that, we would like to provide a service that automatically detects the brand of added products from the related unstructured data it has e.g. title

For legal reasons, we are providing products titles extracted from publicly available amazon reviews dataset (https://nijianmo.github.io/amazon/index.html).

**Tasks**:

1. Transform the provided dataset into the needed format for training a Named Entity recognition model
2. Train a model of your choice for tagging provided products titles
3. Provide the evaluation result of the trained model, and explain why the selected evaluation metric was used in this case
4. Implement a simple Rest API with an endpoint getting as a parameter a product title and returning the tagged text
5. Implement a unit test to make sure that the data transformation process implemented in task 1 is working as expected
6. Provide a Dockerized version of the API

**Optional**:

7. Implement an integration test for the implemented API route

# Training Results

Training Spacy small model for 200 iterations resulted in accuracy of 0.75
