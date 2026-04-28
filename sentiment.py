from transformers import pipeline

# Load model
classifier = pipeline("sentiment-analysis")

def analyze_sentiment(text):
    # Input validation
    if not isinstance(text, str):
        return "Error: Input must be a string"
    if text.strip() == "":
        return "Error: Input cannot be empty"

    result = classifier(text)[0]

    label = result['label']
    score = result['score']

    # Handle neutral using confidence
    if score < 0.6:
        sentiment = "Neutral"
    elif label == "POSITIVE":
        sentiment = "Positive"
    else:
        sentiment = "Negative"

    return {
        "text": text,
        "sentiment": sentiment,
        "confidence": round(score, 3)
    }


# Test sentences (12 total)
test_sentences = [
    # Positive
    "I love this product!",
    "This is amazing work.",
    "I am very happy today.",
    "Everything is going great.",

    # Negative
    "I hate this.",
    "This is terrible.",
    "I am very disappointed.",
    "Worst experience ever.",

    # Neutral
    "The meeting is at 5 PM.",
    "I have a pen.",
    "It is a cloudy day.",
    "She went to the store."
]

print("\n--- TEST RESULTS ---\n")

for sentence in test_sentences:
    print(analyze_sentiment(sentence))
print("\n---USER INPUT TEST---\n")
user_text=input("Enter a sentence:")
print(analyze_sentiment(user_text))
print("\n--- INTERACTIVE MODE ---")
print("Type 'exit' to stop\n")

while True:
    user_input = input("Enter text: ")

    if user_input.lower() == "exit":
        print("Exiting...")
        break

    result = analyze_sentiment(user_input)
    print(result)