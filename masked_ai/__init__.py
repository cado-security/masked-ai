"""
"""
import sys
import logging
from typing import Optional
import argparse
import subprocess

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
                    logging.info(f"Skipping mask {mask.__name__}")
                continue

            to_mask = mask.find(self.masked_data)
            for i, item in enumerate(to_mask):
                lookup_name = f"<{mask.__name__}_{i+1}>"
                self._mask_lookup[lookup_name] = item
                self.masked_data = self.masked_data.replace(item, lookup_name)

    def list_masks(self) -> list[str]:
        return [mask.__name__ for mask in MaskBase.__subclasses__()]

    def get_lookup(self) -> dict:
        return self._mask_lookup

    def unmask_data(self, data: str) -> str:
        """
        """
        unmasked = data
        for k, v in self._mask_lookup.items():
            unmasked = unmasked.replace(k, v)
        return unmasked


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Cado Security Masked-AI")
    parser.add_argument("--debug", action="store_true", help="Enable debug mode")
    parser.add_argument("--text", action="store", dest="text", help="The text to mask", default=None)
    parser.add_argument("command", help="The command to run")
    parser.add_argument("args", nargs=argparse.REMAINDER, help="The arguments for the command, make sure to unclde {replace} somewhere, this will be replaced with the masked text}")
    args = parser.parse_args()

    if not args.text:
        raise SystemExit("--text must be provided. Make sure to add it before the command")

    if not args.command:
        raise SystemExit("No command was found, make sure to add it after the --text argument (i.e. masker --text bla bla echo '{replace}')")

    command = " ".join([args.command] + ["'" + arg + "'" if not arg.startswith("-") else arg for arg in args.args])
    masker = Masker(args.text)
    cleaned_command = command.replace("{replace}", masker.masked_data)

    if args.debug:
        print("************ DEBUG MODE ************")
        print(" - Before masking: ", args.text)
        print(" - After masking: ", masker.masked_data)
        print(" - Lookup: ", masker.get_lookup())
        print(" - COMMAND: ", "".join(cleaned_command))

    output_bytes = subprocess.check_output(cleaned_command, stderr=subprocess.STDOUT, shell=True)
    output = output_bytes.decode("utf-8").strip()
    unmask = masker.unmask_data(output)

    if args.debug:
        print(" - Raw output: ", output)
        print('-------')
        print(" - Unmask output: ", unmask)
        print("************************************")
    else:
        sys.stdout.write(unmask)
        sys.stdout.flush()
