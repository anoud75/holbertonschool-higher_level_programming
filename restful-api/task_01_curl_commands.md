# Consuming APIs with curl

## 1. Check curl Version
```bash
curl --version
```

## 2. Fetch a Web Page
```bash
curl http://example.com
```

## 3. Fetch Posts from JSONPlaceholder
```bash
curl https://jsonplaceholder.typicode.com/posts
```

## 4. Fetch a Single Post
```bash
curl https://jsonplaceholder.typicode.com/posts/1
```

## 5. Fetch Only Headers
```bash
curl -I https://jsonplaceholder.typicode.com/posts
```

## 6. Make a POST Request
```bash
curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts
```

## Common curl Flags

| Flag | Description |
|------|-------------|
| -I | Fetch headers only |
| -X | Specify HTTP method (GET, POST, PUT, DELETE) |
| -d | Send data in request body |
| -H | Add custom header |
| -v | Verbose output |
| -o | Write output to file |

## Example Outputs

### Headers Response
```
HTTP/2 200
content-type: application/json; charset=utf-8
cache-control: max-age=43200
```

### POST Response
```json
{
  "title": "foo",
  "body": "bar",
  "userId": "1",
  "id": 101
}
```
