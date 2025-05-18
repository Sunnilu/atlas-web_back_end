What authentication means
What Base64 is
How to encode a string in Base64
What Basic authentication means
How to send the Authorization header

✅ Explanation
✅ path is None: → True (authentication required)

✅ excluded_paths is None or empty: → True (authentication required)

✅ Ensures slash-tolerance: path=/api/v1/status becomes /api/v1/status/

✅ Returns False if the normalized path is in excluded_paths

It fully satisfies:

Returns True if path is None

Returns True if excluded_paths is None or empty

Returns False if path matches an excluded path (with trailing slash normalization)

You can extend authorization_header and current_user in future steps.

✅ What This Includes
require_auth: Returns True if the given path is not in the excluded_paths, with slash-tolerant matching.

authorization_header: Returns the value of the Authorization header if present, None otherwise.

current_user: Stub method that currently returns None (you'll override this in subclasses like BasicAuth or SessionAuth).

What this does
Returns None if:

authorization_header is None

authorization_header is not a string

it doesn’t start with "Basic "

Otherwise, returns everything after "Basic " — the Base64-encoded credentials.