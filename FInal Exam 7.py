def is_valid_url(url):
    """
    Returns True if url looks like a valid http/https URL using simple rules:
    scheme + host (domain) with basic hostname restrictions, optional path/query/fragment.
    """

    if url is None:
        return False

    # Must be a string and must not contain spaces
    url = str(url)
    if " " in url or len(url) == 0:
        return False

    lower = url.lower()

    # Scheme check (restrict to what you typically see in class/exams)
    if lower[:7] == "http://":
        rest = url[7:]
    elif lower[:8] == "https://":
        rest = url[8:]
    else:
        return False

    # Split off the host from the rest (path/query/fragment)
    slash_pos = rest.find("/")
    if slash_pos == -1:
        host = rest
    else:
        host = rest[:slash_pos]

    if len(host) == 0:
        return False

    # Basic domain checks
    host_lower = host.lower()

    # Must contain at least one dot: example.com
    if "." not in host_lower:
        return False

    parts = host_lower.split(".")
    # No empty labels (e.g., "example..com" or ".com")
    for p in parts:
        if len(p) == 0:
            return False

    # TLD check: last part letters only, length >= 2
    tld = parts[-1]
    if len(tld) < 2:
        return False
    for ch in tld:
        if not ("a" <= ch <= "z"):
            return False

    # Label rules: letters/digits/hyphen; cannot start/end with hyphen
    for label in parts:
        if label[0] == "-" or label[-1] == "-":
            return False
        for ch in label:
            ok = ("a" <= ch <= "z") or ("0" <= ch <= "9") or (ch == "-")
            if not ok:
                return False

    return True

# Testing

print(is_valid_url("https://example.com"))                 # True
print(is_valid_url("http://sub.domain.co.uk/path?q=1#x"))  # True
print(is_valid_url("https://-bad.com"))                    # False
print(is_valid_url("https://bad-.com"))                    # False
print(is_valid_url("https://example"))                     # False
print(is_valid_url("https://exa mple.com"))                # False