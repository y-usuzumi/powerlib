import os
import yaml
import traceback
from ..model import Configuration
from .base import BaseConfigurationLoader

import logging
logger = logging.getLogger(__name__)


class CfgFileConfigurationLoader(BaseConfigurationLoader):
    def load(self) -> Configuration:
        filename = os.path.join(os.path.expanduser('~'), '.config', self._app_name + ".config.yaml")

        try:
            with open(filename) as f:
                config = yaml.load(f)
                return Configuration(config)
        except FileNotFoundError:
            logger.info("Config file does not exist. Skipping.")
            return Configuration()
        except yaml.YAMLError:
            logger.error(f"Error in config file {filename}:")
            raise
