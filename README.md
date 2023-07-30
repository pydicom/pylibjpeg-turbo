pylibjpeg-turbo
===============
(** This README is a Work in Progress)


A builder of Python wheels to access the libjpeg-turbo library, mainly intended for use as a plugin for [pydicom](https://github.com/pydicom/pydicom).

The library has no Python bindings, but is meant to be used through Python's [ctypes](https://docs.python.org/3/library/ctypes.html).  The [PyTurboJPEG](https://github.com/lilohuang/PyTurboJPEG) library is included as a dependency, and its `ctypes` access is used by the pydicom plugin.

 




## Development

To install the development version of pylibjpeg-turbo:

    git clone --recursive https://github.com/pydicom/pylibjpeg-turbo
    cd pylibjpeg_turbo
    python -m pip install -e .[dev]

