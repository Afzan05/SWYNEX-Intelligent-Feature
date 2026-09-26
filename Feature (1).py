import time

# ==========================================
# 1. Core Intelligent Feature & Error Handling
# ==========================================
def analyze_customer_intent(user_prompt):
    """
    Simulates an LLM or NLP model classifying a customer's text intent.
    Includes built-in error handling for invalid inputs.
    """
    # Error Handling: Check for empty or invalid input
    if not isinstance(user_prompt, str):
        return {"status": "error", "message": "Input must be a text string."}
    if len(user_prompt.strip()) == 0:
        return {"status": "error", "message": "Input cannot be empty."}
    if len(user_prompt) > 500:
        return {"status": "error", "message": "Input exceeds the 500-character limit."}

    # Simulated Model Processing (Prompt Evaluation)
    text = user_prompt.lower()
    intent = "Unknown"
    confidence = 0.0

    if "refund" in text or "money back" in text:
        intent = "Refund Request"
        confidence = 0.95
    elif "broken" in text or "not working" in text or "error" in text:
        intent = "Technical Support"
        confidence = 0.88
    elif "buy" in text or "price" in text:
        intent = "Sales Inquiry"
        confidence = 0.92
    else:
        intent = "General Inquiry"
        confidence = 0.50

    return {
        "status": "success",
        "prompt_evaluated": user_prompt,
        "predicted_intent": intent,
        "confidence_score": confidence
    }

# ==========================================
# 2. Prompt / Model Evaluation Examples
# ==========================================
print("--- MODEL EVALUATION EXAMPLES ---")
success_cases = [
    "I need a refund for my recent order, it arrived late.",
    "The software is throwing a 404 error and not working.",
    "What is the price of the premium subscription?"
]

for i, case in enumerate(success_cases, 1):
    result = analyze_customer_intent(case)
    print(f"Example {i}: {result['predicted_intent']} (Confidence: {result['confidence_score']})")


# ==========================================
# 3. Failure Cases & Error Handling Demo
# ==========================================
print("\n--- FAILURE CASES & ERROR HANDLING ---")
failure_cases = [
    "",                      # Empty string
    12345,                   # Wrong data type
    "A" * 600                # Exceeds character limit
]

for i, case in enumerate(failure_cases, 1):
    result = analyze_customer_intent(case)
    print(f"Failure Case {i} Result: {result['message']}")


# ==========================================
# 4. Simple Interface / Demo
# ==========================================
print("\n--- SIMPLE INTERFACE DEMO ---")
def run_demo():
    print("Welcome to the Intelligent Intent Analyzer. Type 'exit' to quit.")
    while True:
        user_input = input("Enter customer message: ")
        if user_input.lower() == 'exit':
            print("Exiting demo...")
            break
        
        print("Analyzing...")
        time.sleep(0.5) # Simulate latency
        response = analyze_customer_intent(user_input)
        
        if response['status'] == 'success':
            print(f"-> Detected Intent: {response['predicted_intent']} ({response['confidence_score']*100}%)\n")
        else:
            print(f"-> Error: {response['message']}\n")

# Uncomment the line below to run the interactive demo in your notebook
# run_demo()
