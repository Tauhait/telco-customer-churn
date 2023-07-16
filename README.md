# telco-customer-churn
Predict behavior to retain customers

Data from https://www.kaggle.com/blastchar/telco-customer-churn

## Use-Case
Suppose we have a service for running marketing campaigns. For each customer, it needs to determine the probability of churn, and if it’s high enough, it will send a promotional email with discounts. Of course, this service needs to use our model to decide whether it should send an email.

## Method
we need to create a churn service — a service in Python that will serve the
churn model. Given the features of a customer, it will respond with the probability of
churn for this customer. For each customer, the campaign service will ask the churn
service for the probability of churn, and if it’s high enough, then we send a promotional email
<picture>
 <source media="(prefers-color-scheme: dark)" srcset="imgs/churn-service.png">
 <source media="(prefers-color-scheme: light)" srcset="imgs/churn-service.png">
 <img alt="churn-service" src="imgs/churn-service.png">
</picture>

## Steps
✅ Gets the customer data in a request
✅ Invokes predict_simple to score the customer
✅ Responds with the probability of churn in JSON

• Assigns the /predict route to the predict function
• Gets the content of the request in JSON
• Scores the customer 
• Prepares the response
• Converts the response to JSON

## Serving flask app
<picture>
 <source media="(prefers-color-scheme: dark)" srcset="imgs/Serving-Flask.png">
 <source media="(prefers-color-scheme: light)" srcset="imgs/Serving-Flask.png">
 <img alt="Serving-Flask" src="imgs/Serving-Flask.png">
</picture>

## How to setup - install all the required libraries from Pipenv.lock
> pipenv install

# AWS: https://299721932716.signin.aws.amazon.com/console