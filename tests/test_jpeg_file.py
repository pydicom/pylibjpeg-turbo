
import pytest
from pathlib import Path

from pylibjpeg_turbo import decode


HERE = Path(__file__).parent

def test_jpeg_file():
    """Decode a simple jpg file"""
    decode(HERE / "_pydicom-logo.jpg")    
