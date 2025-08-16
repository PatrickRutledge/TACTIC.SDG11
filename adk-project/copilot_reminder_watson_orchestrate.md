# Copilot Self-Reminder: Watson Orchestrate Agent Deployment

IMPORTANT: If assisting with Watson Orchestrate ADK agent deployment, refer to the deployment guide located at:
`/home/patrickrutledge/tactic.sdg11/adk-project/agent_deployment_guide.md`

KEY FACTS TO REMEMBER:
1. ADK Version: 1.8.1
2. Required credentials in `.env`:
   - Both WO_API_KEY/WO_INSTANCE AND WATSONX_APIKEY/WATSONX_SPACE_ID
   - YAML agent deployment fails without both credential sets

3. Context variables format in YAML:
   - CORRECT: `- variable_name:Description:default_value`
   - WRONG: Complex nested format with name/description/type/default

4. Commands sequence:
   - Start server: `orchestrate server start -e .env`
   - Import agent: `orchestrate agents import -f agent.yaml`
   - Start UI: `orchestrate chat start`
   - Access at: http://localhost:3000/chat-lite

5. Debug strategies:
   - Create test agent via CLI to see proper format
   - Export working agent to compare YAML structure
   - Check for error: "All context_variables must be non-empty strings"

This is crucial information that resolved previous deployment issues. Always check the `.env` file first for proper credential setup, then verify context variable format in any agent YAML files.

Do not create new credential files - update the existing `.env` file in the project root.
