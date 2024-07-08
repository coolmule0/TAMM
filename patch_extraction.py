
"""Import modules required to run the Jupyter notebook."""

# Clear logger to use tiatoolbox.logger
# import logging

# if logging.getLogger().hasHandlers():
#     logging.getLogger().handlers.clear()

from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import requests

from tiatoolbox import logger
from tiatoolbox.tools import patchextraction
from tiatoolbox.utils.misc import imread, read_locations

# mpl.rcParams["figure.dpi"] = 300  # for high resolution figure in notebook
# mpl.rcParams["figure.facecolor"] = "white"  # To make sure text is visible in dark mode

class patch_extractor():
    # wsi_dir: Path
    patch_dir: Path
    wsis: list[Path] = ['/home/john/Data/WSI/sheffield_flat/ACC_3590.svs']
    patch_size = (500,500)
    stride = patch_size
    masker: str = 'otsu'
    mask_ratio: float = 0.7

    def extract_patches(self):
        for wsi in self.wsis:

            fixed_patch_extractor = patchextraction.get_patch_extractor(
                input_img=wsi,  # input image path, numpy array, or WSI object
                method_name="slidingwindow",  # also supports "point" and "slidingwindow"
                patch_size=self.patch_size,  # size of the patch to extract around the centroids from centroids_list
                stride=self.stride,  # stride of extracting patches, default is equal to patch_size
                input_mask=self.masker,
                min_mask_ratio=self.mask_ratio,
            )
    
    # def save_patches(self, patch_extractor):

p = patch_extractor()
p.extract_patches()