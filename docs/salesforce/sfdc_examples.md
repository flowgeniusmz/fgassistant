
# Salesforce AI Assistant Example Outputs

## Example Outputs for Various Request Types

### 1. `getrecords` Without Secondary Fields/Objects
**User Request**: "Retrieve all accounts in the New York region."

```json
{
    "requesttype": "getrecords",
    "primaryobject": "Account",
    "primaryobjectfields": [
        {"field": "Region", "value": "New York"}
    ],
    "secondaryobject": null,
    "secondaryobjectfields": null
}
```

### 2. `getrecords` With Secondary Fields/Objects
**User Request**: "Get all opportunities with products attached in the technology sector."

```json
{
    "requesttype": "getrecords",
    "primaryobject": "Opportunity",
    "primaryobjectfields": [
        {"field": "Sector", "value": "Technology"}
    ],
    "secondaryobject": "Product",
    "secondaryobjectfields": null
}
```

### 3. `getrecord` Without Secondary Fields/Objects
**User Request**: "Show details of the contact named Emily Clark."

```json
{
    "requesttype": "getrecord",
    "primaryobject": "Contact",
    "primaryobjectfields": [
        {"field": "Name", "value": "Emily Clark"}
    ],
    "secondaryobject": null,
    "secondaryobjectfields": null
}
```

### 4. `getrecord` With Secondary Fields/Objects
**User Request**: "Fetch the account details for XYZ Corp, including their primary contact information."

```json
{
    "requesttype": "getrecord",
    "primaryobject": "Account",
    "primaryobjectfields": [
        {"field": "Name", "value": "XYZ Corp"}
    ],
    "secondaryobject": "Contact",
    "secondaryobjectfields": [
        {"field": "AccountId", "value": "XYZ Corp ID"}
    ]
}
```

### 5. `updaterecord` Without Secondary Fields/Objects
**User Request**: "Update the phone number of the lead, Jane Doe, to 987-654-3210."

```json
{
    "requesttype": "updaterecord",
    "primaryobject": "Lead",
    "primaryobjectfields": [
        {"field": "Name", "value": "Jane Doe"},
        {"field": "Phone", "value": "987-654-3210"}
    ],
    "secondaryobject": null,
    "secondaryobjectfields": null
}
```

### 6. `updaterecord` With Secondary Fields/Objects
**User Request**: "Change the status of the case #12345 to 'Resolved' and update the related customer's email to customer@example.com."

```json
{
    "requesttype": "updaterecord",
    "primaryobject": "Case",
    "primaryobjectfields": [
        {"field": "CaseNumber", "value": "12345"},
        {"field": "Status", "value": "Resolved"}
    ],
    "secondaryobject": "Contact",
    "secondaryobjectfields": [
        {"field": "Email", "value": "customer@example.com"}
    ]
}
```

### 7. `createrecord` Without Secondary Fields/Objects
**User Request**: "Create a new lead for Michael Smith in the automotive industry."

```json
{
    "requesttype": "createrecord",
    "primaryobject": "Lead",
    "primaryobjectfields": [
        {"field": "Name", "value": "Michael Smith"},
        {"field": "Industry", "value": "Automotive"}
    ],
    "secondaryobject": null,
    "secondaryobjectfields": null
}
```

### 8. `createrecord` With Secondary Fields/Objects
**User Request**: "Add a new account for BlueTech Inc with John Doe as the primary contact."

```json
{
    "requesttype": "createrecord",
    "primaryobject": "Account",
    "primaryobjectfields": [
        {"field": "Name", "value": "BlueTech Inc"}
    ],
    "secondaryobject": "Contact",
    "secondaryobjectfields": [
        {"field": "Name", "value": "John Doe"}
    ]
}
```
