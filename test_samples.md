# Test Results – Phishing URL Awareness Checker

## Test 1
- **URL:** `https://www.example.com/login`
- **Expected:** No listed warning signs found.
- **Actual:** No listed warning signs found. This does NOT prove safety.
- **Status:** (Pass)

## Test 2
- **URL:** `http://192.0.2.10/account`
- **Expected:** IP address warning and HTTP warning.
- **Actual:**  Uses an IP address instead of a familiar domain.Uses HTTP. HTTPS alone does not prove trust.
               Never enter passwords from unexpected links.
- **Status:** (Pass)

## Test 3
- **URL:** `http://example.com@sample.invalid/login`
- **Expected:** @ symbol warning and HTTP warning.
- **Actual:** - Contains an @ symbol; inspect carefully. Uses HTTP. HTTPS alone does not prove trust.
                Never enter passwords from unexpected links.
- **Status:** (Pass)

## Test 4
- **URL:** `https://a.b.c.d.e.example.invalid/path`
- **Expected:** Many hostname segments warning.
- **Actual:**  Contains many hostname segments/subdomains.
               Never enter passwords from unexpected links.
- **Status:** (Pass)

## Test 5
- **URL:** `https://xn--example.invalid/`
- **Expected:** Punycode-style hostname warning.
- **Actual:**  Contains a punycode-style hostname.
                Never enter passwords from unexpected links.
- **Status:** (Pass)
