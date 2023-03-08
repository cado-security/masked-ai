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
        self.masked_data = data
        self._mask_lookup = {}
        for mask in MaskBase.__subclasses__():
            if skip and mask.__name__ in skip:
                if debug:
                    logging.info(f'Skipping mask {mask.__name__}')
                continue

            to_mask = mask.find(self.masked_data)
            for i, item in enumerate(to_mask):
                lookup_name = f'<{mask.__name__}_{i+1}>'
                self._mask_lookup[lookup_name] = item
                self.masked_data = self.masked_data.replace(item, lookup_name)

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
    data = "Adam Cohen Hillel this is a test 127.0.0.1 and my link is www.google.com"
    print('data: ', data)
    masker = Masker("Adam Cohen Hillel this is a test 127.0.0.1 and my link is www.google.com")
    print('masked: ', masker.masked_data)
    lookup = masker.get_lookup()
    print('lookup: ', lookup)
    print('unmasked: ', masker.unmask_data(masker.masked_data))
