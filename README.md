# Prime AI Guardrails SDK

Official Python SDK for Prime AI Guardrails - Enterprise AI Security, Governance, and Compliance Platform.

## Installation

```bash
pip install prime-guardrails
```

Or install from source:

```bash
git clone https://github.com/secureaillc/prime-sdk.git
cd prime-sdk
pip install -e .
```

## Quick Start

```python
from prime_guardrails import PrimeClient

# Initialize client
client = PrimeClient(
    api_key="your-api-key",
    base_url="https://your-prime-instance.com"
)

# Simple security check
result = client.guard(
    input_text="User's question here",
    output_text="AI's response here",
    checks=["pii", "prompt_injection", "toxicity"]
)

if result.status == "BLOCK":
    print(f"Blocked: {result.message}")
else:
    print("Content is safe")
```

## Features

- **Security Agent**: Unified endpoint for all security checks
- **Individual APIs**: Direct access to specific security checks
- **Guardrail Flows**: Pre-configured evaluation pipelines
- **MCP Integration**: Model Context Protocol support for AI assistants

## API Reference

### Security Agent (Recommended)

The Security Agent provides a unified endpoint for comprehensive AI security:

```python
from prime_guardrails import PrimeClient

client = PrimeClient(api_key="your-key")

# Full security check
result = client.security_agent.guard(
    mode="both",  # "input", "output", or "both"
    content={
        "input": "User message",
        "output": "AI response"
    },
    checks=["pii", "prompt_injection", "dlp", "toxicity", "hallucination"],
    config={
        "pii": {"action": "redact"},
        "toxicity": {"threshold": 0.7}
    }
)
```

### Individual Security APIs

For direct access to specific security checks:

```python
# PII Detection
pii_result = client.pii.detect("My SSN is 123-45-6789")

# Prompt Injection Detection
injection_result = client.prompt_injection.detect("Ignore all previous instructions...")

# DLP Scan
dlp_result = client.dlp.scan("API_KEY=sk-abc123...")

# Hallucination Detection
hallucination_result = client.hallucination.check(
    premise="Paris is the capital of France",
    hypothesis="The capital of France is Berlin"
)

# Toxicity Detection
toxicity_result = client.toxicity.check("Some potentially toxic content")

# Bias Detection
bias_result = client.bias.detect("Content to check for bias")
```

### Guardrail Flows

Evaluate against pre-configured guardrail pipelines:

```python
result = client.guardrails.evaluate(
    app_id="my-ai-app",
    guardrail_flow_name="production-flow",
    payload={"user_input": "Hello"},
    model_output="Hi there! How can I help?"
)
```

## Authentication

### API Key Authentication

```python
client = PrimeClient(api_key="your-api-key")
```

### Environment Variable

```bash
export PRIME_API_KEY="your-api-key"
export PRIME_BASE_URL="https://your-instance.com"
```

```python
client = PrimeClient()  # Automatically reads from environment
```

## Examples

See the `examples/` directory for complete usage examples:

- `basic_security_check.py` - Simple security validation
- `security_agent_full.py` - Full Security Agent usage
- `individual_apis.py` - Using individual security APIs
- `guardrail_flows.py` - Working with Guardrail Flows
- `mcp_integration.py` - MCP protocol integration
- `async_usage.py` - Async/await patterns
- `error_handling.py` - Proper error handling

## Support

- Documentation: https://docs.secureaillc.com
- Issues: https://github.com/secureaillc/prime-sdk/issues
- Email: support@secureaillc.com

## License

MIT License - see LICENSE file for details.
