# Basics of HTTP/HTTPS

## Differences Between HTTP and HTTPS

| Feature | HTTP | HTTPS |
|---------|------|-------|
| Full Name | Hypertext Transfer Protocol | Hypertext Transfer Protocol Secure |
| Port | 80 | 443 |
| Security | No encryption, data sent in plain text | Encrypted using SSL/TLS |
| URL Prefix | http:// | https:// |
| Data Protection | Vulnerable to eavesdropping | Protected from eavesdroppers |
| Certificate | Not required | Requires SSL certificate |
| Use Case | Non-sensitive data | Sensitive data (banking, login, etc.) |

### Summary
HTTP transmits data in plain text, making it vulnerable to interception. HTTPS adds a security layer using SSL/TLS encryption, ensuring data confidentiality and integrity. The "s" in HTTPS stands for "secure".

---

## Structure of HTTP Request and Response

### HTTP Request Structure
```
[METHOD] [PATH] HTTP/[VERSION]
[Headers]

[Body (optional)]
```

**Example:**
```
GET /index.html HTTP/1.1
Host: www.example.com
User-Agent: Mozilla/5.0
Accept: text/html
```

### HTTP Response Structure
```
HTTP/[VERSION] [STATUS CODE] [STATUS MESSAGE]
[Headers]

[Body]
```

**Example:**
```
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 1234

<html>...</html>
```

---

## Common HTTP Methods

| Method | Description | Use Case |
|--------|-------------|----------|
| GET | Retrieves data from the server | Fetching a web page or API data |
| POST | Sends data to the server to create a resource | Submitting a form, creating a new user |
| PUT | Updates an existing resource completely | Updating a user's profile information |
| DELETE | Removes a resource from the server | Deleting a user account |
| PATCH | Partially updates a resource | Updating only the email of a user |

---

## Common HTTP Status Codes

| Status Code | Description | Scenario |
|-------------|-------------|----------|
| 200 OK | Request succeeded | Successfully fetching a web page |
| 201 Created | Resource successfully created | After successfully creating a new user |
| 301 Moved Permanently | Resource has been moved to a new URL | Website URL change, redirecting old to new |
| 400 Bad Request | Server cannot process due to client error | Sending malformed JSON in a request |
| 401 Unauthorized | Authentication required | Trying to access a protected resource without login |
| 403 Forbidden | Server refuses to authorize | User doesn't have permission to access resource |
| 404 Not Found | Resource not found | Requesting a page that doesn't exist |
| 500 Internal Server Error | Server encountered an error | Database connection failure on the server |

### Status Code Categories
- **1xx**: Informational responses
- **2xx**: Successful responses
- **3xx**: Redirection messages
- **4xx**: Client error responses
- **5xx**: Server error responses
