

def build_prompt(data):
    # Start building the prompt using the feature name from input data
    prompt = f"Generate Python code for {data['feature']}.\n\n"

    # Add Requirements section header
    prompt += "Requirements:\n"
    
    # Loop through each requirement and add it as a bullet point
    for req in data["requirements"]:
        prompt += f"- {req}\n"

    # Add a new section for validations
    prompt += "\nValidations:\n"
    
    # Loop through each validation rule and add it as a bullet point
    for val in data["validations"]:
        prompt += f"- {val}\n"

    # Add final instruction for generating test cases
    prompt += "\nAlso generate test cases."

    # Return the final constructed prompt
    return prompt