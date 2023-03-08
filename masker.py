"""
"""
import logging
from typing import Optional

from core.masks import MaskBase


class Masker:
    """Interface
    """
    def __init__(
        self,
        data: str,
        skip: Optional[list] = None,
        debug: bool = False
    ) -> None:
        """
        """
        self.original_data = data
        self._mask_lookup = {}
        for mask in MaskBase.__subclasses__():
            if skip and mask.__name__ in skip:
                if debug:
                    logging.info(f'Skipping mask {mask.__name__}')
                continue

            to_mask = mask.find(data)
            for i, item in enumerate(to_mask):
                lookup_name = f'<{mask.__name__}_{i+1}>'
                self._mask_lookup[lookup_name] = item
                data.replace(item, lookup_name)

        self.masked_data = data

    def list_masks(self) -> list[str]:
        return [mask.__name__ for mask in MaskBase.__subclasses__()]

    def get_lookup(self):
        return self._mask_lookup

    def unmask_data(self, data: str) -> str:
        """
        """
        for k, v in self._mask_lookup.items():
            data.replace(k, v)
        return data


if __name__ == "__main__":
    logging.info('ABC')
    masker = Masker("this is a test 127.0.0.1 and my link is www.google.com")
    lookup = masker.get_lookup()
    print('************', lookup)
