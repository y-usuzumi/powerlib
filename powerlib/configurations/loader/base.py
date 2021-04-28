from ..model import Configuration


class BaseConfigurationLoader:
    def __init__(self, *, app_name: str):
        self._app_name = app_name

    def load(self) -> Configuration:
        raise NotImplementedError
