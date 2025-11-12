# JSON TOON Converter

**json-toon-converter** is a powerful Python library that helps you easily convert data between **JSON** and **TOON** formats. The TOON format is a compact, human-readable serialization format, perfect for reducing token usage in applications such as AI-driven models and data serialization. This package allows you to convert both JSON and TOON with minimal effort.

Python Version: 3.8+  
PyPI Version: [json-toon-converter](https://pypi.org/project/json-toon-converter)  
License: MIT License  
Downloads: Available on [PyPI](https://pypi.org/project/json-toon-converter)

[![PyPI version](https://badge.fury.io/py/json-toon-converter.svg)](https://badge.fury.io/py/json-toon-converter)
[![Downloads](https://static.pepy.tech/badge/json-toon-converter)](https://pepy.tech/project/json-toon-converter)
[![Python versions](https://img.shields.io/pypi/pyversions/json-toon-converter.svg)](https://pypi.org/project/json-toon-converter/)
[![License](https://img.shields.io/pypi/l/json-toon-converter.svg)](https://pypi.org/project/json-toon-converter/)
## 🌟 Key Features

- 🔄 **Bidirectional Conversion**: Convert **JSON to TOON** and **TOON to JSON** effortlessly.
- 🎯 **Flexible Integration**: Simple API for integrating into your Python projects.
- 🏷️ **Token Savings**: Save tokens when working with language models and APIs.
- 💡 **Customizable Prompts**: You can specify prompts for targeted description or formatting.
- 📝 **Type Hints**: Full type hints for better development experience.
- 🌐 **CLI Support**: Command-line interface for quick conversions and batch processing.

## 📦 Installation

To install the package, use `pip`:

```bash
pip install json-toon-converter

# 🚀 Quick Start

Import the package and use the provided functions to convert between **JSON** and **TOON** formats.

### Convert JSON to TOON

```python
from json_to_toon_converter import json_to_toon

json_data = {
    "name": "Alice",
    "age": 25,
    "city": "Wonderland"
}

toon_data = json_to_toon(json_data)
print(toon_data)
```

### Convert TOON to JSON

```python
from json_to_toon_converter import toon_to_json

toon_data = '(name "Alice") (age 25) (city "Wonderland")'
json_data = toon_to_json(toon_data)
print(json_data)

```

# 🤝 Contributing

We welcome contributions! Here's how you can help:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Your contributions are greatly appreciated!

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.
