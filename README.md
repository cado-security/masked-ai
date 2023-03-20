# Masked-AI
![ci](https://github.com/cado-security/masked-ai/actions/workflows/app-ci.yml/badge.svg?branch=main)
<!-- [![PyPI version](https://badge.fury.io/py/masked-ai.svg)](https://badge.fury.io/py/masked-ai) -->
Masking data for OpenAI API. A Python SDK + CLI wrappers to enable the usage of public LLM APIs securely, by reducing sensetive data before sending requests to the API, and then construct the data back before presenting to the user.

### Flow:
![](docs/flow.png)

## How to use
You can use the CLIO tool with
#### CLI:
Download the binary and run:
**Note:** that in the command argument, there is a special string `{replace}`, this is what `Masked-AI` will replace the safe string with
```bash
masker --text "This is a text I want to mask, for example my name Adam" --command "echo {replace}"
```

And here is how you can use `Masked-AI` CLI with OpenAI API:
```
masker --text "This is a text I want to mask, for example my name Adam" --command " \
curl https://api.openai.com/v1/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{"model": "text-davinci-003", "prompt": {replace}}' \
"
Again, note the `{replace}` string in the curl command, where your safe, masked `--text` will go.
The output of the command will be the return value from [OpenAI API](https://platform.openai.com/docs/api-reference/completions/create), but after `masked-ai` has reconsrcueted it using the lookup. Use `--debug` to see the steps more clearly
```

#### Python:
If you want to use it within your Python code, you can do the following
```python
import os
import openai
from masked_ai import Masker

# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv("OPENAI_API_KEY")

debug = False
data = "Text with potential sensitive data"

masker = Masker(data)

if debug:
    print('Masking: ', data)
    print('Masked: ', masker.masked_data)
    print('Lookup: ', masker.get_lookup())

response = openai.Completion.create(model="text-davinci-003", prompt=masker.masked_data)

if debug:
    print('Raw response: ', response)

unmasked = masker.unmask_data(response)
print('Result:', unmasked)
```


## How to contribute:
The main area to contribute is to add more Masks, for example, we currently have: `IPMask`, `EmailMask`, `CreditCardMask`, and more - but there is always more to add.
Clone the repo, create a new branch, and simply go to `core/masks.py`, create a new class that inherent from `MaskBase` (in the same module), and implement the `find` method: `def find(data: str) -> Tuple[str, Dict[str, str]]:`. Once you created the class, it will automatically be part of the masking process.
Here is an example for masking IP addresses:
```Python
class IPMask(MaskBase):
    """IP addresses
    """
    @staticmethod
    def find(data: str) -> Tuple[str, Dict[str, str]]:
        return re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", data)
```
And don't forget to add tests `tests/core/test_masks.py`! :)

## License
This is licensed under the GPL. Please contact us if this does not work for your use case - we may be able to alternatively license under a non-copyleft license such as the Apache License. We're friendly! As this software is licensed under the GPL and used in our commercial product, we ask any contributors to sign a simple Contributor License Agreement (CLA).
