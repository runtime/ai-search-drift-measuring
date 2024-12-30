# AI Search Drift Detection and monitoring system

### Python application that measures drift on a models responses to user queries.

This python application is a framework for drift detection on an LLM and consequential messaging for low tensors scores.


```
Stack:
>sentence-transformers
>fastapi
>psychopg2
>postgresql
>tbd messaging service
>next.js
>tailwind
```

Note: Current build does not use an LLM and does not directly take user queries, instead it is placeholder for the end to end process being established in an mvp.'

Todo:  messaging, docker container,  implement next.js and tailwind, drift data viz, add actual llm to detect drift against


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