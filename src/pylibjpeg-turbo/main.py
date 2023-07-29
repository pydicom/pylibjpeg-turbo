from pathlib import Path
from io import BytesIO
import warnings
from turbojpeg import TurboJPEG


def decode(buff, transform=0, reshape=True):
    """Return the decoded JPEG data from `buff` as a :class:`numpy.ndarray`.

    Parameters
    ----------
    buff : str | pathlib.Path | bytes
        The path to a JPEG file or the `bytes` representing encoded JPEG data.

    Returns
    -------
    numpy.ndarray
        A 1D array of ``numpy.uint8`` containing the decoded image data.

    Raises
    ------
    RuntimeError
        If the decoding failed.
    """
    
    if transform != 0 or reshape is False:
        raise NotImplementedError("Currently only handle transform 0 and reshape True")
    
    jpeg = TurboJPEG()
    if isinstance(buff, (str, Path)):
        buff = open(buff, "rb").read()
    width, height, jpeg_subsample, jpeg_colorspace = jpeg.decode_header(buff)
    print(width, height, jpeg_subsample, jpeg_colorspace)
    return jpeg.decode(buff)


def decode_pixel_data(arr, ds=None, **kwargs):
    """Return the decoded JPEG data from `arr` as a :class:`numpy.ndarray`.

    Intended for use with *pydicom* ``Dataset`` objects.

    Parameters
    ----------
    arr : numpy.ndarray | bytes
        The encoded JPEG image as a ``np.uint8`` 1D array or :class:`bytes`.
    ds : pydicom.dataset.Dataset | None
        A :class:`~pydicom.dataset.Dataset` containing the group ``0x0028``
        elements corresponding to the *Pixel Data*. Must have
        *Photometric Interpretation* (``'MONOCHROME1'``, ``'MONOCHROME2'``,
        ``'RGB'``, ``'YBR_FULL'``, or ``'YBR_FULL_422'``).
    **kwargs: Dict[str, Any]
        Additional keyword arguments.

    Returns
    -------
    numpy.ndarray
        The decoded image data as a 1D ``numpy.uint8`` array.

    """
    colors = ["MONOCHROME1", "MONOCHROME2", "RGB", "YBR_FULL", "YBR_FULL_422"]

    photometric = ds.get("PhotometricInterpretation") or kwargs.get(
        "photometric_interpretation"
    )
    if not photometric:
        raise ValueError(
            "Photometric Interpretation element is not in the Dataset, "
            "nor is it supplied as keyword argument `photometric_interpretation`."
        )

    if photometric not in colors:
        warnings.warn(
            f"Unsupported Photometric Interpretation '{photometric}'. No "
            "color transformation will be applied"
        )

    transform = 1 if photometric == "RGB" else 0

    return decode(arr, transform, reshape=False)
