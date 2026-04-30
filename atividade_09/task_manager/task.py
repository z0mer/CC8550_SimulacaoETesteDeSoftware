from datetime import datetime
from enum import Enum, IntEnum
from dataclasses import dataclass, field
from typing import Optional


class Priority(IntEnum):
    BAIXA = 1
    MEDIA = 2
    ALTA = 3


class Status(Enum):
    PENDENTE = "PENDENTE"
    EM_PROGRESSO = "EM_PROGRESSO"
    CONCLUIDA = "CONCLUIDA"


_TRANSICOES_VALIDAS = {
    Status.PENDENTE: [Status.EM_PROGRESSO],
    Status.EM_PROGRESSO: [Status.CONCLUIDA],
    Status.CONCLUIDA: [],
}


@dataclass
class Task:
    titulo: str
    descricao: str
    prioridade: Priority
    prazo: datetime
    id: Optional[int] = None
    status: Status = field(default=Status.PENDENTE)

    def validar(self):
        """Valida regras basicas antes de salvar a tarefa."""
        if len(self.titulo) < 3:
            raise ValueError("Título deve ter pelo menos 3 caracteres.")
        if self.prazo < datetime.now():
            raise ValueError("O prazo não pode estar no passado.")

    def atualizar_status(self, novo_status: Status):
        """Move a tarefa apenas para um status permitido."""
        if novo_status not in _TRANSICOES_VALIDAS[self.status]:
            raise ValueError(
                f"Transição inválida de {self.status.value} para {novo_status.value}."
            )
        self.status = novo_status
