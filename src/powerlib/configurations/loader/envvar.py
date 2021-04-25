from ..model import Configuration
from .base import BaseConfigurationLoader

import logging
logger = logging.getLogger(__name__)


class EnvvarConfigurationLoader(BaseConfigurationLoader):
    def load(self) -> Configuration:
        logger.warning("Configuration over environment variables are not supported yet")
        return Configuration()
