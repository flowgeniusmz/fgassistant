# Peer to Peer Data Flow

![Peer to Peer Data Flow](file-vCnpvqMj8CXmtZQJdt01BLbg)

This diagram details the flow of data in a peer-to-peer network within an environmental monitoring context. IoT sensors emit data using different protocols, which are then sent to Power Automate. Power Automate checks the completeness of the data before forwarding it to OpenAI, which performs further data completeness checks, calculations, and accuracy assessments. The verified data is logged in the Supabase database and finally presented to the user through a dashboard UI. This process exemplifies the integration of IoT data streams for comprehensive analysis and visualization in real-time applications.
