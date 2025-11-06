import re

def clean_address_header(address_text: str) -> str:
    """
    Remove headers like 'YOUR BILLING ADDRESS' or 'YOUR DELIVERY ADDRESS'
    and clean extra spaces/newlines.
    """
    cleaned = re.sub(r'YOUR\s+(BILLING|DELIVERY)\s+ADDRESS', '', address_text, flags=re.I)
    cleaned = re.sub(r'\s+', ' ', cleaned)
    return cleaned.strip()
