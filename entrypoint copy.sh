#!/bin/bash --login
# The --login ensures the bash configuration is loaded,
# enabling Conda.

# Enable strict mode.
set -euo pipefail
# ... Run whatever commands ...

# Temporarily disable strict mode and activate conda:
set +euo pipefail
conda init
conda activate streamlit_ml_apps

# Re-enable strict mode:
set -euo pipefail

# exec the final command:
exec streamlit hello #run streamlit_app.py --server.port=8501 --server.address=0.0.0.0