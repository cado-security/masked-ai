# masked-openai
Masked Python SDK wrapper for OpenAI API. Use public LLM APIs securely by reducing sensetive data before sending requests to OpenAI api, and then construct the data back before presenting to the user.


## Examples
```python
from masked_openai import Masker

data = "Text with potential sensitive data"

masker = Masker(data)
respinse = openai(masker.masked())
```

## How to contribute:



## License
This is licensed under the GPL. Please contact us if this does not work for your use case - we may be able to alternatively license under a non-copyleft license such as the Apache License. We're friendly! As this software is licensed under the GPL and used in our commercial product, we ask any contributors to sign a simple Contributor License Agreement (CLA).
