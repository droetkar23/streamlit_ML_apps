#!/bin/bash

conda run \
--no-capture-output -n streamlit_ml_apps \
streamlit run /app/st_app/streamlit_app.py \
--server.port=8501 \
--server.address=0.0.0.0 \
--server.runOnSave=true \
--server.fileWatcherType="poll"