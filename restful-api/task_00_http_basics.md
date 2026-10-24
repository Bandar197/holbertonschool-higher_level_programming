# Task 0: Basics of HTTP/HTTPS

## HTTP vs. HTTPS

- **HTTP (Hypertext Transfer Protocol):** Transfers requests and responses without encrypting the data. Intermediaries may be able to read or modify the traffic. A typical HTTP URL starts with `http://` and uses port 80.
- **HTTPS (HTTP Secure):** Sends HTTP over TLS, providing encryption, server authentication through certificates, and protection against tampering in transit. A typical HTTPS URL starts with `https://` and uses port 443.
- Both use the same basic HTTP methods, requests, responses, and status codes. HTTPS protects data **in transit**; it does not automatically make the website or its application code secure.

## Example HTTP request

```http
GET /posts HTTP/1.1
Host: example.com
Accept: application/json
User-Agent: example-client/1.0

```

The request consists of a request line (method, path, protocol version), headers, a blank line, and an optional body (commonly used for POST/PUT/PATCH).

## Example HTTP response

```http
HTTP/1.1 200 OK
Content-Type: application/json

{"ok": true}
```

The response consists of a status line (protocol version, status code, reason phrase), headers, a blank line, and an optional response body.

## Common HTTP methods

| Method | Description | Example use case |
| --- | --- | --- |
| GET | Retrieve a resource without requesting a change | Read a blog post |
| POST | Submit data or create a resource | Create a user account |
| PUT | Replace a resource with the supplied representation | Replace a user's profile |
| PATCH | Partially update a resource | Change only a user's city |
| DELETE | Remove a resource | Delete a post |

## Common HTTP status codes

| Code | Meaning | Example scenario |
| --- | --- | --- |
| 200 | OK | A GET request successfully retrieves a page |
| 201 | Created | A POST request creates a user |
| 301 | Moved Permanently | An old URL permanently redirects to a new URL |
| 400 | Bad Request | A request body contains invalid JSON |
| 401 | Unauthorized | Authentication credentials are missing or invalid |
| 403 | Forbidden | A signed-in user tries to access an admin-only route |
| 404 | Not Found | A requested post does not exist |
| 500 | Internal Server Error | An unexpected server-side exception occurs |

Status classes: 1xx informational, 2xx success, 3xx redirection, 4xx client errors, 5xx server errors.

## Inspect requests and responses

In your browser, open Developer Tools > Network, reload a site, select a request, and inspect its method, URL, request headers, status code, response headers, and response body.
