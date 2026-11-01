
import re
from urllib.parse import urlparse


def inspect_url(raw_url):
    """Check visible URL text for selected warning signs."""

    url = raw_url.strip()
    findings = []

    if not url:
        return ["No URL entered."]

    # Add a default scheme if the user does not provide one
    candidate = url if "://" in url else "http://" + url

    try:
        parsed = urlparse(candidate)
        host = (parsed.hostname or "").lower()
    except ValueError:
        return ["Invalid URL format. Please check the URL text."]

    if not host:
        return ["Could not identify a hostname."]

    # Check 1: @ symbol
    if "@" in candidate:
        findings.append("Contains an @ symbol; inspect carefully.")

    # Check 2: URL length
    if len(url) > 100:
        findings.append("Unusually long URL (over 100 characters).")

    # Check 3: IP address as hostname
    if re.fullmatch(r"(?:\d{1,3}\.){3}\d{1,3}", host):
        findings.append(
            "Uses an IP address instead of a familiar domain."
        )

    # Check 4: Five or more hostname segments
    labels = [part for part in host.split(".") if part]

    if len(labels) >= 5:
        findings.append(
            "Contains many hostname segments/subdomains."
        )

    # Check 5: Punycode marker
    if "xn--" in host:
        findings.append("Contains a punycode-style hostname.")

    # Check 6: HTTP instead of HTTPS
    if parsed.scheme.lower() == "http":
        findings.append(
            "Uses HTTP. HTTPS alone does not prove trust."
        )

    if not findings:
        findings.append(
            "No listed warning signs found. This does NOT prove safety."
        )

    return findings



def main():
    print("======================================")
    print("   EWB Phishing URL Awareness Checker")
    print("======================================")

    print("Text checks only - this program does not open URLs.")

    while True:
        raw_url = input("\nEnter a URL to inspect (or type 'quit' to exit): ")

        if raw_url.strip().lower() == "quit":
            print("\nThank you for using the checker!")
            break

        findings = inspect_url(raw_url)

        print("\nResult:")

        for item in findings:
            print("- " + item)

        # Warning summary
        if findings == ["No listed warning signs found. This does NOT prove safety."]:
            print("\nSummary: No listed warning signs detected.")
        elif findings == ["No URL entered."]:
            print("\nSummary: Please enter a URL.")
        else:
            print("\nSummary: Review this URL carefully!")

        print("\nRemember: Never enter passwords on unexpected websites.")


if __name__ == "__main__":
    main()

