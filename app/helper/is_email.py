from email_validator import validate_email, EmailNotValidError

def is_email(value: str) -> bool:
    try:
        validate_email(value)
        return True
    except EmailNotValidError:
        return False