## repo to deploy models from ML projects and trying out streamlit



```yml
services:
  streamlit_ml_apps:
    container_name: streamlit_ml_apps
    build:
      dockerfile: ./Dockerfile
      context: ./
    ports:
      - 8501:8501
    volumes:
      - ./st_app_example:/app/st_app
```
