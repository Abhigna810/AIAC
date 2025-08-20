# user_data_collection.py

def collect_user_data():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    email = input("Enter your email: ")
    user_data = {
        "name": name,
        "age": age,
        "email": email
    }
    return user_data

def main():
    data = collect_user_data()
    print("Collected Data:", data)

if __name__ == "__main__":
    main()

# --- Data Protection & Anonymization Comments ---
# 1. Avoid storing sensitive data in plain text files.
# 2. Use hashing (e.g., hashlib) for sensitive fields like email.
# 3. Remove or mask personally identifiable information (PII) before sharing or storing.
# 4. Use encryption libraries (e.g., cryptography) to encrypt data at rest.
# 5. Limit data access to authorized users only.
# 6. Regularly delete data that is no longer needed.