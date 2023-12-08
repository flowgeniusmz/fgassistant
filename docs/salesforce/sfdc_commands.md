# AI Assistant Salesforce Request Handling Guide

This guide details how an AI assistant should identify and respond to Salesforce-related requests using the `simple_salesforce` Python library.

## Command Types

The AI assistant should recognize and handle four primary types of requests:

1. **getrecords**: Retrieve a list of records using SOSL or SOQL queries.
2. **getrecord**: Fetch details for a single record (e.g., an account or lead).
3. **createrecord**: Create a new record (e.g., a new account).
4. **updaterecord**: Update an existing record with new or different information.

### 1. getrecords

#### User Request Examples and Ideal Responses:

- **Low Complexity**: "Show me all open opportunities."
  - **Ideal Response**: `getrecords`
- **Medium Complexity**: "Can you list accounts created last month?"
  - **Ideal Response**: `getrecords`
- **High Complexity**: "I need a list of leads with 'pending' status who are from the technology sector."
  - **Ideal Response**: `getrecords`

### 2. getrecord

#### User Request Examples and Ideal Responses:

- **Low Complexity**: "What are the details of account ID 12345?"
  - **Ideal Response**: `getrecord`
- **Medium Complexity**: "Can I get the contact information for lead John Doe?"
  - **Ideal Response**: `getrecord`
- **High Complexity**: "Please provide the last interaction details for the contact Jane Smith."
  - **Ideal Response**: `getrecord`

### 3. createrecord

#### User Request Examples and Ideal Responses:

- **Low Complexity**: "Create a new lead with name John Smith."
  - **Ideal Response**: `createrecord`
- **Medium Complexity**: "Can you add a new account for Acme Corp with basic details?"
  - **Ideal Response**: `createrecord`
- **High Complexity**: "Set up a new opportunity for XYZ Inc. with detailed specifications and expected revenue."
  - **Ideal Response**: `createrecord`

### 4. updaterecord

#### User Request Examples and Ideal Responses:

- **Low Complexity**: "Update the phone number of lead John Doe."
  - **Ideal Response**: `updaterecord`
- **Medium Complexity**: "Change the status of opportunity 45678 to 'Closed Won'."
  - **Ideal Response**: `updaterecord`
- **High Complexity**: "For account ABC Corp, update the address, main contact, and add a note about the recent meeting."
  - **Ideal Response**: `updaterecord`

## Handling Requests

The AI assistant should analyze the user's input to determine the command type. The ideal response to each user request should be the name of the corresponding command only.
