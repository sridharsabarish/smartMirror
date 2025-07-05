
import sys
import os

# Add the parent directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/')))
from HandleClothing import HandleClothing

import pytest

@pytest.mark.parametrize("temperature, expected", [
    (10, 2),
    (15, 1),
    (20, 0),
    (30, 0),
])
def test_Check_layers(temperature, expected):
    handleClothing = HandleClothing()
    assert handleClothing.find_layers(temperature=temperature) == expected

    