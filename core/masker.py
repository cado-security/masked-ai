"""
"""
from core.masks import _MaskBase


class Masker:
    """
    """
    def __init__(self, data: str) -> None:
        self.original_data = data
        self._mask_lookup = {}

        for mask in _MaskBase.__subclasses__:
            data = mask.mask(data)

    def unmask_data(self, data: str) -> str:
        """
        """
        for k, v in self._mask_lookup.items():
            data.replace(k, v)
        return data
