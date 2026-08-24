from urllib.parse import urlsplit, urlunsplit, parse_qsl, urlencode

TRACKING = {
    "utm_source", "utm_medium", "utm_campaign",
    "utm_term", "utm_content", "fbclid",
    "gclid", "dclid", "msclkid"
}

def clean_url(url):
    p = urlsplit(url.strip())
    query = [
        (k, v) for k, v in parse_qsl(p.query, keep_blank_values=True)
        if k.lower() not in TRACKING
    ]
    return urlunsplit((
        p.scheme, p.netloc, p.path,
        urlencode(query), p.fragment
    ))

print(clean_url("https://example.com/page?utm_source=test&id=123"))
