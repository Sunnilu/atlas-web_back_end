In this project, you will learn what the authentication process means and implement a Basic Authentication on a simple API.

There are two interfaces provided by this module. The modern interface supports encoding bytes-like objects to ASCII bytes, and decoding bytes-like objects or strings containing ASCII to bytes. Both base-64 alphabets defined in RFC 3548 (normal, and URL- and filesystem-safe) are supported.

The legacy interface does not support decoding from strings, but it does provide functions for encoding and decoding to and from file objects. It only supports the Base64 standard alphabet, and it adds newlines every 76 characters as per RFC 2045. Note that if you are looking for RFC 2045 support you probably want to be looking at the email package instead.

base64.b64decode(s, altchars=None, validate=False)
Decode the Base64 encoded bytes-like object or ASCII string s and return the decoded bytes.

Optional altchars must be a bytes-like object or ASCII string of at least length 2 (additional characters are ignored) which specifies the alternative alphabet used instead of the + and / characters.

A binascii.Error exception is raised if s is incorrectly padded.