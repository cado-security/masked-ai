"""
"""
import re
from abc import ABC, abstractmethod
from typing import Dict, Tuple


class _MaskBase(ABC):
    """Instruct how to implement new mask
    """

    @staticmethod
    @abstractmethod
    def mask(data: str) -> Tuple[str, Dict[str, str]]:
        """Implement this method

        :param data: Data to mask

        :return: New, masked data, and the loopup table to reconstruct it
        """
        return NotImplemented


class IPMask(_MaskBase):
    """Mask IP Addresses in text
    """

    def mask(data: str) -> Tuple[str, Dict[str, str]]:
        """IP Mask

        :param data: Data to mask

        :return: New, masked data, and the loopup table to reconstruct it
        """
        ips = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", data)
        masked: Dict[str, str] = {}
        for i, ip in enumerate(ips):
            masked[ip] = f"<IP_{i}>"
            data.replace(ip, masked[ip])
        return data, masked
