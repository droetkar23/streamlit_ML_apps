FROM condaforge/mambaforge:latest as conda_env_base

WORKDIR /app/setup/

# RUN git clone https://github.com/streamlit/streamlit-example.git .

COPY environment.yml .
RUN mamba env create -f environment.yml && mamba clean -ayf


FROM conda_env_base


# Make RUN commands use the new environment:
SHELL ["conda", "run", "-n", "myenv", "/bin/bash", "-c"]

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

COPY entrypoint.sh .
WORKDIR /app/st_app/
ENTRYPOINT ["/app/setup/entrypoint.sh"]