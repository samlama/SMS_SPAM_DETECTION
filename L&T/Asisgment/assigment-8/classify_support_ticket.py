def classify_support_ticket(description):
    lower_description = description.lower()
    if 'account' in lower_description and ('login' in lower_description or 'log in' in lower_description):
        return "Account Access Issue"
    elif 'payment' in lower_description or 'billing' in lower_description:
        return "Payment/Billing Issue"
    elif 'technical' in lower_description or 'error' in lower_description:
        return "Technical Issue"
    else:
        return "Other Issue"

sample_input = "Can't log into my Account. Its showing the payment limit"

# Classify the support ticket
classified_output = classify_support_ticket(sample_input)

print(classified_output)
