# 0. Basics of HTTP/HTTPS

## HTTP vs HTTPS

HTTP (Hypertext Transfer Protocol) is the protocol used to transfer data
between a client (e.g. a browser) and a server. It is plain text: any data
sent over HTTP (headers, cookies, body) can be read or modified by anyone
who intercepts the traffic (a proxy, a router on the path, someone
sniffing the network, etc).

HTTPS (HTTP Secure) is HTTP layered on top of SSL/TLS. Before any HTTP
data is exchanged, the client and server perform a TLS handshake that:

- Encrypts the traffic, so eavesdroppers only see ciphertext, not the
  actual request/response content.
- Authenticates the server via its TLS certificate, so the client knows
  it is really talking to the intended server and not an impostor
  (man-in-the-middle).
- Guarantees integrity, so data can't be silently tampered with in
  transit without detection.

Main differences:

| | HTTP | HTTPS |
|---|---|---|
| Port | 80 | 443 |
| Encryption | None | TLS/SSL |
| Data confidentiality | No | Yes |
| Server authentication | No | Yes (via certificate) |
| Performance | Slightly faster (no handshake) | Small overhead for handshake/encryption |
| Typical use | Static, non-sensitive content | Anything with logins, payments, personal data |

In short: HTTPS = HTTP + encryption + authentication + integrity. Any
site handling passwords, personal data or payments should use HTTPS.

## Structure of an HTTP request

```
GET /api/users/42 HTTP/1.1
Host: example.com
User-Agent: Mozilla/5.0
Accept: application/json
Authorization: Bearer <token>

(optional body, e.g. for POST/PUT)
```

- **Request line**: method + path + HTTP version (`GET /api/users/42 HTTP/1.1`).
- **Headers**: key/value metadata about the request (Host, content type,
  authentication, accepted formats, etc).
- **Blank line**: separates headers from the body.
- **Body** (optional): data sent with the request, typically used with
  `POST`, `PUT`, `PATCH`.

## Structure of an HTTP response

```
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 58

{"id": 42, "name": "Alice"}
```

- **Status line**: HTTP version + status code + reason phrase
  (`HTTP/1.1 200 OK`).
- **Headers**: metadata about the response (content type/length,
  caching, cookies, etc).
- **Blank line**: separates headers from the body.
- **Body** (optional): the actual data returned (HTML, JSON, file, ...).

## Common HTTP methods

| Method | Description | Use case |
|---|---|---|
| GET | Retrieves data from the server, no side effects | Fetching a web page or data from an API (e.g. `GET /users`) |
| POST | Sends data to the server to create a new resource | Creating a new user account (`POST /users`) |
| PUT | Replaces an existing resource entirely with the sent data | Updating a whole user record (`PUT /users/42`) |
| DELETE | Removes the specified resource | Deleting a user (`DELETE /users/42`) |
| PATCH | Partially updates an existing resource | Updating just one field, e.g. a user's email |

## Common HTTP status codes

| Code | Description | Scenario |
|---|---|---|
| 200 OK | Request succeeded | A `GET` request successfully returns the requested data |
| 201 Created | Resource successfully created | After a successful `POST /users` that creates a new user |
| 301 Moved Permanently | Resource has a new permanent URL | The requested page has been permanently moved to a new address |
| 400 Bad Request | The request is malformed or invalid | The client sends invalid JSON or missing required fields |
| 401 Unauthorized | Authentication is required or has failed | Accessing a protected endpoint without a valid token |
| 404 Not Found | Requested resource doesn't exist | Requesting `/users/9999` when no such user exists |
| 500 Internal Server Error | Server encountered an unexpected error | A bug or crash in the server-side code while processing the request |

(Status codes are grouped by first digit: 1xx informational, 2xx
success, 3xx redirection, 4xx client error, 5xx server error.)
