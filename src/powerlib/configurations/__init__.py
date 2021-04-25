from .model import Configuration
from threading import Lock
from .model import Configuration
from .loader import CfgFileConfigurationLoader, EnvvarConfigurationLoader

_APP_PREFIX = 'messenger'
_LOADER_CLASSES = [CfgFileConfigurationLoader, EnvvarConfigurationLoader]

_CONFIG = None
_CONFIG_LOCK = Lock()

def load_config() -> Configuration:
    global _CONFIG
    if _CONFIG is None:
        with _CONFIG_LOCK:
            if _CONFIG is None:
                _CONFIG = _load_config()
    return _CONFIG


def _load_config() -> Configuration:
    config = Configuration.empty()
    for loader_class in _LOADER_CLASSES:
        config.merge(loader_class(_APP_PREFIX))
    return config
