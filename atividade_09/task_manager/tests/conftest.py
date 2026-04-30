import sys
from pathlib import Path

# Adiciona task_manager/ ao sys.path para que os módulos sejam encontrados
sys.path.insert(0, str(Path(__file__).parent.parent))
