import json
import logging
from datetime import UTC, datetime

_ATRIBUTOS_PADRAO = set(logging.makeLogRecord({}).__dict__)


class FormatadorJson(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        dados = {
            "timestamp": datetime.fromtimestamp(record.created, tz=UTC).isoformat(),
            "nivel": record.levelname,
            "logger": record.name,
            "mensagem": record.getMessage(),
        }
        for chave, valor in record.__dict__.items():
            if chave not in _ATRIBUTOS_PADRAO:
                dados[chave] = valor
        if record.exc_info:
            dados["excecao"] = self.formatException(record.exc_info)
        return json.dumps(dados, ensure_ascii=False, default=str)


def configurar_logging(nivel: int = logging.INFO) -> None:
    raiz = logging.getLogger()
    raiz.setLevel(nivel)
    if any(isinstance(h.formatter, FormatadorJson) for h in raiz.handlers):
        return
    handler = logging.StreamHandler()
    handler.setFormatter(FormatadorJson())
    raiz.addHandler(handler)
