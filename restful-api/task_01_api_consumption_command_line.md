# 1. Consume data from an API using command line tools (curl)

## 1. Checking the curl installation

```
$ curl --version
curl 7.81.0 (x86_64-pc-linux-gnu) libcurl/7.81.0 OpenSSL/3.0.2 zlib/1.2.11 ...
Release-Date: 2022-01-05
Protocols: dict file ftp ftps gopher gophers http https imap imaps ldap ldaps
           mqtt pop3 pop3s rtmp rtsp scp sftp smb smbs smtp smtps telnet tftp
Features: alt-svc AsynchDNS brotli GSS-API HSTS HTTP2 HTTPS-proxy IDN IPv6
          Kerberos Largefile libz NTLM NTLM_WB PSL SPNEGO SSL TLS-SRP
          UnixSockets zstd
```

`curl --version` confirms curl is installed and lists the protocols and
features it was built with (HTTP, HTTPS, FTP, SSL/TLS support, HTTP/2, etc).

## 2. Fetching data from an API

```
$ curl https://jsonplaceholder.typicode.com/posts
```

Output (truncated, showing the first two entries of the JSON array):

```json
[
  {
    "userId": 1,
    "id": 1,
    "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
    "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
  },
  {
    "userId": 1,
    "id": 2,
    "title": "qui est esse",
    "body": "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla"
  },
  ...
]
```

The endpoint returns a JSON array of 100 posts. Each object has 4 fields:
`userId` (which user created it), `id` (the post's unique identifier),
`title` and `body`.

## 3. Fetching only the headers (`-I`)

```
$ curl -I https://jsonplaceholder.typicode.com/posts
```

Output:

```
HTTP/2 200
date: Fri, 28 Aug 2026 20:15:35 GMT
content-type: application/json; charset=utf-8
access-control-allow-credentials: true
cache-control: max-age=43200
etag: W/"6b80-Ybsq/K6GwwqrYkAsFxqDXGC7DoM"
server: cloudflare
vary: Origin, Accept-Encoding
x-content-type-options: nosniff
x-powered-by: Express
x-ratelimit-limit: 1000
x-ratelimit-remaining: 999
...
```

`-I` sends a `HEAD` request instead of `GET`: it returns only the status
line and headers, no body. It's useful to quickly check the status code,
content type, caching rules and rate-limit information without
downloading the full payload.

## 4. Making a POST request (`-X POST -d`)

```
$ curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts
```

Output:

```json
{
  "title": "foo",
  "body": "bar",
  "userId": "1",
  "id": 101
}
```

- `-X POST` explicitly sets the HTTP method to `POST` (curl defaults to
  `GET` unless `-d`/`-X` says otherwise).
- `-d "title=foo&body=bar&userId=1"` sends form-encoded data as the
  request body.
- JSONPlaceholder is a fake/mock API: it doesn't persist the new post,
  but it simulates the creation and responds with the submitted data
  plus a generated `id` (always `101`, since the fake DB already has
  100 posts).

## Summary

| Flag | Purpose |
|---|---|
| (none) | Sends a `GET` request and prints the response body |
| `-I` | Sends a `HEAD` request, prints only the status line + headers |
| `-X <METHOD>` | Overrides the HTTP method (e.g. `POST`, `PUT`, `DELETE`) |
| `-d "<data>"` | Sends data in the request body (also switches the method to `POST` if `-X` isn't set) |

Piping any of these through `jq` (e.g. `curl -s ... | jq`) pretty-prints
and color-highlights the JSON output for easier reading.
