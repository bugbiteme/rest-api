# demo-app

RestAPI to test with RHDH

Code, pipeline, and deployment.

## Running with Podman

Build the container image from the repository root:

```bash
podman build -t demo-app -f Containerfile .
```

Run the container, mapping port 8000:

```bash
podman run --rm -p 8000:8000 demo-app
```

Test the API:

```bash
curl http://localhost:8000/api/v1/hello
```

Expected response:

```json
{"message":"hello world"}
```

### Swagger UI

FastAPI serves interactive API docs at `/docs`. With the container running, open:

http://localhost:8000/docs

From there you can explore and try the `GET /api/v1/hello` endpoint.