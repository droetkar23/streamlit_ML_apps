FROM condaforge/mambaforge:latest as conda_env_base

WORKDIR /app

RUN git clone https://github.com/streamlit/streamlit-example.git .

COPY environment.yml .
RUN mamba env create -f environment.yml


FROM conda_env_base

# Make RUN commands use the new environment:
SHELL ["conda", "run", "-n", "myenv", "/bin/bash", "-c"]
# RUN echo "conda init" >> ~/.bashrc
# RUN echo "conda activate streamlit_ml_apps" >> ~/.bashrc
# SHELL ["/bin/bash", "--login", "-c"]

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

COPY entrypoint.sh .
ENTRYPOINT ["./entrypoint.sh"]