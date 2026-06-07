# Surgical Robotic Arm Response Delay Optimization

Professional simulation and diagnostics for the RBA-2201 surgical robotic arm.

## Project Overview
This repository contains a simulation-driven investigation into response delays observed in the `rotate_joint` control command of the RBA-2201 surgical robotic arm. The goal is to identify root causes, apply lightweight optimizations to the control code, and measure before/after response-time improvements suitable for surgical applications.

Key outcomes:
- Reduced `rotate_joint` response time from ~0.50s to ~0.14s (simulated)
- Demonstrated a 20% improvement in control efficiency via algorithmic changes

## Features
- Command simulation and timing utilities
- Diagnostic analysis and logging
- Performance benchmarking and comparison (before / after)
- Well-documented Python module (`src/simulation.py`)
- Jupyter notebooks with executable examples

## Installation
Recommended: use a virtual environment.

```bash
python -m venv .venv
source .venv/bin/activate     # macOS / Linux
.venv\\Scripts\\Activate.ps1   # Windows PowerShell
pip install -r requirements.txt
```

## Quick Usage
1. Run the simulation module for a quick CLI demo:

```bash
python -m src.simulation
```

2. Open the notebooks to reproduce experiments and plots:
- `Control_System_Diagnostic_Notebook.ipynb`
- `Robotic_Arm_Design_Simulation.ipynb`

## Documentation
See the `docs/` directory for implementation details and usage examples.

## Results (summary)
- `rotate_joint` simulated time: ~0.50s → ~0.14s after optimizations
- Control-level responsiveness increased by ~20%

## Future Improvements
- Integrate real actuator models and hardware-in-the-loop testing
- Replace sleep-based simulation with event-driven timing and async I/O
- Add unit tests and CI to validate performance regressions

## License
This project is released under the MIT License — see `LICENSE`.

## Contact
For questions about the simulation or to request supporting materials, open an issue in this repository.
<p align="center">
  <img src="./github_assets.png" alt="Johnson & Johnson MedTech Logo" width="400">
</p>

## File Overview

### Task 1: Control System Diagnostics
- **Notebook**: `Control_System_Diagnostics_Notebook.ipynb`
  - Diagnose and optimize the robotic arm’s control system.
  - Identify delays in commands like `rotate_joint`, `move_arm`, and `adjust_grip`.
- **Resource**: [Diagnostics Guide](./Diagnostics_Guide.pdf)
  - Detailed instructions on troubleshooting and optimizing control code.

### Task 2: Design Optimization
- **Notebook**: `Robotic_Arm_Design_Simulation.ipynb`
  - Simulate design modifications for improved response times and durability.
  - Test factors like efficiency and reinforcement using provided tools.
- **Resource**: [Design Optimization Principles](./Design_Optimization_Principles.pdf)
  - Learn the fundamentals of design optimization and real-world applications.

---

## How to Use

1. Open the relevant `.ipynb` file in Jupyter Notebook or a compatible Python environment.
2. Follow the step-by-step instructions in each notebook to complete the tasks.
3. Use the provided templates and guides for documentation and proposals.

---

## Contribution Guidelines
We welcome contributions to improve the repository! If you have suggestions or find issues, please create a pull request or submit an issue.

---

## License
This repository is for educational purposes as part of the Johnson & Johnson Robotics Control System Simulation Program. The content and tools are not intended for commercial use.

---

## Disclaimer
The robotic designs and simulations provided in this repository are educational approximations. They do not represent actual Johnson & Johnson robotic systems.
