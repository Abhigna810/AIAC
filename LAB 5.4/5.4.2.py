import re

def preprocess_text(text):
    """
    Basic text preprocessing: lowercase, remove punctuation, etc.
    """
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    return text

def simple_sentiment_analysis(text, positive_words, negative_words):
    """
    Simple rule-based sentiment analysis.
    Returns 'positive', 'negative', or 'neutral'.
    """
    text = preprocess_text(text)
    words = text.split()
    pos_count = sum(1 for w in words if w in positive_words)
    neg_count = sum(1 for w in words if w in negative_words)
    if pos_count > neg_count:
        return 'positive'
    elif neg_count > pos_count:
        return 'negative'
    else:
        return 'neutral'

def detect_and_handle_bias(text, bias_words):
    """
    Detects presence of potentially biased words and warns the user.
    """
    text = preprocess_text(text)
    found_bias = [w for w in bias_words if w in text.split()]
    if found_bias:
        print(f"[Bias Warning] The following potentially biased words were detected: {', '.join(found_bias)}")
        print("Please consider revising your input to avoid unintended bias.")
    return found_bias

def main():
    # Example word lists (in real applications, use larger, curated lists)
    positive_words = {'good', 'great', 'excellent', 'happy', 'love', 'wonderful', 'fantastic', 'positive', 'enjoy'}
    negative_words = {'bad', 'terrible', 'awful', 'sad', 'hate', 'horrible', 'negative', 'poor', 'dislike'}
    # Example bias words (could be expanded for real use)
    bias_words = {'always', 'never', 'everyone', 'nobody', 'obviously', 'clearly'}

    print("Sentiment Analysis Tool (with Bias Detection)")
    user_input = input("Enter a sentence for sentiment analysis: ").strip()
    if not user_input:
        print("No input provided.")
        return

    # Bias detection
    detect_and_handle_bias(user_input, bias_words)

    # Sentiment analysis
    sentiment = simple_sentiment_analysis(user_input, positive_words, negative_words)
    print(f"Sentiment detected: {sentiment.capitalize()}")

    # Transparency and fairness note
    print("\n[Ethical Note]")
    print("This tool uses a simple word-list approach and may not capture all nuances of language.")
    print("We attempt to detect and warn about potentially biased language, but this is not exhaustive.")
    print("For fairer and more accurate results, use diverse and representative data and regularly review word lists.")

if __name__ == "__main__":
    main()
