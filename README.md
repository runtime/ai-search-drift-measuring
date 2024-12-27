# AI Search Drift Detection and monitoring system

### Python application that measures drift on a models response choices and if it is under a certain tensor it will send you a message

##### to use:
```
uvicorn app.main:app --reload
```

##### load:
```
http://127.0.0.1:8000
```

##### returns
```
{"message": "Welcome to the AI Search Drift Measuring API!"}

```