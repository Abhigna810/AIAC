import logging
from flask import Flask, request, jsonify

app = Flask(__name__)

# Configure logging
class SensitiveInfoFilter(logging.Filter):
    """
    Filter to remove sensitive information from logs.
    """
    SENSITIVE_KEYS = {'password', 'token', 'secret', 'ssn', 'credit_card'}

    def filter(self, record):
        # If the log record has an 'extra' dict, sanitize it
        if hasattr(record, 'args') and isinstance(record.args, dict):
            sanitized = {}
            for k, v in record.args.items():
                if k.lower() in self.SENSITIVE_KEYS:
                    sanitized[k] = '[REDACTED]'
                else:
                    sanitized[k] = v
            record.args = sanitized
        return True

logger = logging.getLogger('webapp')
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter(
    '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
)
handler.setFormatter(formatter)
handler.addFilter(SensitiveInfoFilter())
logger.addHandler(handler)

@app.route('/login', methods=['POST'])
def login():
    data = request.json or {}
    username = data.get('username')
    # Do NOT log the password or sensitive info
    logger.info("Login attempt", extra={'username': username})
    # ... authentication logic ...
    return jsonify({"message": "Login attempted"}), 200

@app.route('/update_profile', methods=['POST'])
def update_profile():
    data = request.json or {}
    # Remove sensitive fields before logging
    safe_data = {k: ('[REDACTED]' if k.lower() in SensitiveInfoFilter.SENSITIVE_KEYS else v)
                 for k, v in data.items()}
    logger.info("Profile update", extra=safe_data)
    # ... profile update logic ...
    return jsonify({"message": "Profile updated"}), 200

if __name__ == '__main__':
    app.run(debug=True)
