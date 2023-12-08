# System Architecture Integration via MQTT and HTTP

![System Architecture Integration via MQTT and HTTP](Sequence - System Architecture (MQTT and HTTP).PNG)

This diagram displays a system architecture that integrates data flow using MQTT and HTTP protocols. An 'IoT Emitter' sends data to a 'MQTT Data Broker (Case 1)', which is then processed via 'Power Automate'. The data undergoes a completeness check by 'OpenAI Data Completeness' before calculations are performed by 'OpenAI Data Calculations'. Following accuracy and compliance checks, the data is stored in a 'Supabase Database' and finally displayed through a 'Streamlit Frontend'. This sequence ensures a robust and secure data handling system from collection to presentation.
