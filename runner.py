# código importado por terceiros, para poder rodar o projeto sem ter acesso a um terminal

import sys
from streamlit.web import cli as stcli

sys.argv = ["stramlit", "run", "test.py"]
sys.exit(stcli.main())
