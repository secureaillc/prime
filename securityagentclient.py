from prime_guardrails import SecurityAgent

agent = SecurityAgent(api_key="your-api-key")

# Guard input before LLM
result = agent.guard_input("User's message here")
if not result.is_safe:
    return "Request blocked"

# Guard output before returning
result = agent.guard_output(llm_response, reference_docs=["context"])
return result.sanitized_content or llm_response
