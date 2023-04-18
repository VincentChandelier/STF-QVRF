# STF-QVRF

# The Devil Is in the Details: Window-based Attention for Image Compression + QVRF: A Quantization-error-aware Variable Rate Framework for Learned Image Compression
Pytorch implementation of the paper "The Devil Is in the Details: Window-based Attention for Image Compression" + “QVRF: A Quantization-error-aware Variable Rate Framework for Learned Image Compression”

We make the STF into variable rate model
This repository is based on [STF](https://github.com/Googolxx/STF). We kept network scripts, and removed other components. The major changes are provided in `stf.py`. For the official code release, see the [STF](https://github.com/Googolxx/STF/blob/main/compressai/models/stf.py).

## About
This repo defines Transformer-based models in varibale rate model for learned image compression in "The Devil Is in the Details: Window-based Attention for Image Compression" + “QVRF: A Quantization-error-aware Variable Rate Framework for Learned Image Compression”.

## Related links
 * CompressAI: https://github.com/InterDigitalInc/CompressAI
 * STF：https://github.com/Googolxx/STF
 * QVRF：https://github.com/bytedance/QRAF
 
## Installation


```bash
conda create -n compress python=3.7
conda activate compress
pip install compressai=1.1.5
pip install pybind11
pip install timm
```


## Citation
```
@inproceedings{zou2022the,
  title={The Devil Is in the Details: Window-based Attention for Image Compression},
  author={Zou, Renjie and Song, Chunfeng and Zhang, Zhaoxiang},
  booktitle={CVPR},
  year={2022}
}

@article{tong2023qvrf,
  title={QVRF: A Quantization-error-aware Variable Rate Framework for Learned Image Compression},
  author={Tong, Kedeng and Wu, Yaojun and Li, Yue and Zhang, Kai and Zhang, Li and Jin, Xin},
  journal={arXiv preprint arXiv:2303.05744},
  year={2023}
}
```
