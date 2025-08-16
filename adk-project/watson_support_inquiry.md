# Watson Support Inquiry: Context Variables Validation Issue in ADK 1.8.1

## Issue Description
When attempting to import agent YAML files with context variables, we consistently encounter the validation error:
`All context_variables must be non-empty strings`

This occurs despite defining non-empty strings for all context variables in the YAML file.

## Environment
- ADK Version: 1.8.1
- Credentials: Both WO_API_KEY/WO_INSTANCE and WATSONX_APIKEY/WATSONX_SPACE_ID are properly set
- Agent YAML: Contains context variables with non-empty default values

## Resolution Found
We discovered that the validation succeeds when using a simplified format for context variables:
```yaml
context_variables:
- variable_name:Description:default_value
```

And fails when using the complex format:
```yaml
context_variables:
  - name: variable_name
    description: Description
    type: string
    default: "default_value"
```

## Questions
1. Is this simplified format the officially recommended approach for context variables in ADK 1.8.1?
2. Is there documentation clarifying the proper format for context variables in YAML files?
3. Why does the CLI agent creation succeed with context variables while YAML imports fail unless using the simplified format?
4. Will future versions of the ADK support the complex format for better readability and maintainability?

We'd appreciate clarification on the proper format for context variables to ensure our deployment processes are aligned with best practices.

Thank you for your assistance!
