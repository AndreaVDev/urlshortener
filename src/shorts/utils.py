import string
import secrets

def generate_short_code(length: int = 6) -> str:
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(length))

def generate_short_url(short_code: str) -> str:
    # Assuming the base URL for the shortener service is "http://short.ly/"
    base_url = "http://short.ly/"
    return f"{base_url}{short_code}"