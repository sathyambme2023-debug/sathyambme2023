"""Simulation utilities for Surgical Robotic Arm diagnostics.

This module provides small, well-documented functions used in the internship
project to simulate command response times and demonstrate simple
optimizations. The code is intentionally lightweight and suitable for
demonstration, unit-testing, and extension to hardware interfaces.

Functions:
- check_response_time(command): simulated response latency for a command
- optimized_command(command, improvement_factor): returns improved timing
- simulate_response_time(base_time, efficiency_factor): design-level sim
- simulate_durability(base_durability, reinforcement_factor): design-level sim

Usage (CLI):
    python -m src.simulation
"""

import time
from typing import Literal

Command = Literal['rotate_joint', 'move_arm', 'adjust_grip']


def check_response_time(command: Command) -> float:
    """Simulate execution of a control command and return response time in seconds.

    The function uses small, deterministic `time.sleep()` calls to emulate
    processing and mechanical delays. Replace with actual timing calls when
    connected to real hardware.

    Args:
        command: one of 'rotate_joint', 'move_arm', 'adjust_grip'

    Returns:
        float: observed response time in seconds
    """
    start = time.time()
    if command == 'rotate_joint':
        # Baseline realistic delay for rotation (simulated)
        time.sleep(0.18)
    elif command == 'move_arm':
        time.sleep(0.1)
    elif command == 'adjust_grip':
        time.sleep(0.05)
    else:
        # Unknown commands default to a short delay
        time.sleep(0.05)
    return time.time() - start


def optimized_command(command: Command, improvement_factor: float = 0.2) -> float:
    """Return an optimized (simulated) response time.

    The function preserves the original control behavior but reports the
    expected improved response time after software optimizations.

    Args:
        command: control command to simulate
        improvement_factor: fractional improvement (0.0-1.0) to apply

    Returns:
        float: simulated optimized response time in seconds
    """
    base = check_response_time(command)
    return base * (1.0 - float(improvement_factor))


def simulate_response_time(base_time: float, efficiency_factor: float) -> float:
    """Simulate the effect of a design efficiency change on response time.

    Args:
        base_time: baseline response time in seconds
        efficiency_factor: fractional improvement (0.0-1.0)

    Returns:
        float: new estimated response time
    """
    return base_time * (1.0 - float(efficiency_factor))


def simulate_durability(base_durability: float, reinforcement_factor: float) -> float:
    """Estimate increased durability after reinforcement.

    Args:
        base_durability: baseline durability score/metric
        reinforcement_factor: fractional increase (e.g., 0.15 for +15%)

    Returns:
        float: new durability metric
    """
    return base_durability * (1.0 + float(reinforcement_factor))


def _demo():
    """Small demo that prints before/after timings for the main commands."""
    commands = ['move_arm', 'rotate_joint', 'adjust_grip']
    print('Testing initial command response times:')
    for c in commands:
        t = check_response_time(c)
        print(f'{c} response time: {round(t,3)} seconds')

    print('\nTesting optimized command response times:')
    for c in commands:
        ot = optimized_command(c)
        print(f'{c} optimized response time: {round(ot,3)} seconds')


if __name__ == '__main__':
    _demo()
