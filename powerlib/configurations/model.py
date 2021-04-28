from __future__ import annotations


class Configuration(dict):
    def merge(self, other: Configuration) -> Configuration:
        # Currently, the merge is shallow. Not sure I should implement
        # deepmerge or not.
        return Configuration(self | other)

    def __getitem__(self, key):
        val = super().__getitem__(key)
        if isinstance(val, dict):
            return Configuration(val)
        return val

    def get(self, key):
        val = super().get(key)
        if isinstance(val, dict):
            return Configuration(val)
        return val

    def __repr__(self):
        return f"Configuration({super().__repr__()})"
