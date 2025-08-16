# Watson Orchestrate Agent Deployment Guidelines

## Credential Setup
When deploying agents with context variables, ensure proper credential configuration:

1. Set BOTH of these credential pairs in your `.env` file:
   ```
   # Watson Orchestrate credentials
   WO_INSTANCE=https://api.dl.watson-orchestrate.ibm.com/instances/[your-instance-id]
   WO_API_KEY=[your-api-key]
   
   # WatsonX AI credentials (required for context variable validation)
   WATSONX_SPACE_ID=[your-space-id] 
   WATSONX_APIKEY=[your-api-key]
   ```

2. Optional settings:
   ```
   WO_DEVELOPER_EDITION_SOURCE=orchestrate
   WO_DEVELOPER_EDITION_SKIP_LOGIN=true
   ```

## Context Variable Format
When defining context variables in YAML files, use the simplified format:

```yaml
context_variables:
- variable_name:Description of the variable:default_value
- another_variable:Another description:default_value
```

Do NOT use the complex format (which will fail validation):
```yaml
context_variables:
  - name: variable_name
    description: Description of the variable
    type: string
    default: "default_value"
```

## Deployment Process
1. Start the server with credentials:
   ```bash
   orchestrate server start -e .env
   ```

2. Import your agent:
   ```bash
   orchestrate agents import -f your_agent.yaml
   ```

3. Start the chat UI:
   ```bash
   orchestrate chat start
   ```

4. Access the chat interface at:
   ```
   http://localhost:3000/chat-lite
   ```

## Troubleshooting
- If you see "All context_variables must be non-empty strings" error, check your context variable format and ensure WATSONX credentials are set.
- If agents don't appear in the UI, make sure to start the chat service with `orchestrate chat start`.
- Creating agents via CLI works differently from importing via YAML; use exported agents as reference for correct format.
- Always check server logs for detailed errors when deployments fail.

## ADK Version Info
These guidelines are specific to IBM Watson Orchestrate ADK version 1.8.1.
