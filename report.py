from transformers import pipeline

text_generator = pipeline("text2text-generation", model="google/flan-t5-large")

def test_transformer():
    prompt = "Summarize this security incident: A person entered a restricted area."
    report = text_generator(prompt, max_length=500, do_sample=True)
    print(report[0]["generated_text"])

test_transformer()

def generate_report(incident_details):
    """Generate a textual report based on detected anomalies."""
    print(f"Incident Details: {incident_details}")  # Debugging
    if not incident_details or incident_details.lower() == "none":
        incident_details = "No specific incident details were provided."
    prompt = f"Generate a detailed incident report in English based on the following details: {incident_details}. Include a summary, potential causes, and recommended actions."
    report = text_generator(prompt, max_length=500, do_sample=True,temperature=0.7)
    return report[0]["generated_text"]



