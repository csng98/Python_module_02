# Garden Guardian: Data Engineering for Smart Agriculture 🌱

Welcome to **Garden Guardian**, a project focused on building fault-tolerant data pipelines and robust monitoring workflows for smart greenhouse and IoT sensor networks.

## 🚀 Project Overview
In modern agriculture, real-time streams (soil pH, temperature, humidity) are prone to telemetry corruption and hardware dropouts. This project implements advanced defensive programming using Python's exception-handling matrix to ensure data pipeline integrity without system crashes.

## 🛠️ Tech Stack & Standards
- **Language:** Python 3.12.3
- **Code Quality:** `flake8` linter compliant
- **Type Checking:** Strict type hints verified via `mypy`
- **Patterns:** Built-in and classical custom exception hierarchies, transactional resource cleanup

## 📂 Project Structure
```text
📂 garden-guardian/
├── 📁 ex0/
│   └── 📄 ft_first_exception.py       # Basic String-to-Int Telemetry Validation
├── 📁 ex1/
│   └── 📄 ft_raise_exception.py       # Bound Checking & Threshold Exceptions
├── 📁 ex2/
│   └── 📄 ft_different_errors.py      # Multi-Exception Handling Blocks
├── 📁 ex3/
│   └── 📄 ft_custom_errors.py         # Custom Inherited Exceptions (GardenError)
├── 📁 ex4/
│   └── 📄 ft_finally_block.py         # Safe Context Cleanup & Resource Management
└── 📄 README.md
