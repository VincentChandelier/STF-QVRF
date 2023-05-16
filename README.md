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

# Available data
| Method | Lambda | Link                                                                                              |
| ---- |--------|---------------------------------------------------------------------------------------------------|
| Fixed-rate model | 0.0483 | [stf_0483](https://drive.google.com/file/d/1cH5cR-0VdsQqCchyN3DO62Sx0WGjv1h8/view?usp=share_link)    |
| Variable-rate mode|0.0018, 0.0035, 0.0067, 0.0130, 0.025, 0.0483, 0.0932, 0.18, 0.36, 0.72, 1.44    |  [stf_0483](https://drive.google.com/file/d/1cH5cR-0VdsQqCchyN3DO62Sx0WGjv1h8/view?usp=share_link)  |

## Installation


```bash
conda create -n compress python=3.7
conda activate compress
pip install compressai=1.1.5
pip install pybind11
pip install timm
```
## Usage
### Training
Load the [fixed-rate model](https://drive.google.com/file/d/1cH5cR-0VdsQqCchyN3DO62Sx0WGjv1h8/view?usp=share_link) from [STF](https://github.com/Googolxx/STF) as the pretrained model and finetune into a variable-rate model.
The trained set is same to [QRAF](https://github.com/VincentChandelier/QRAF）
```
stage 3
```
python3 train.py  -d ./dataset  -e 500 -lr 1e-6 -n 8 --batch-size 8 --test-batch-size 64 --aux-learning-rate 1e-3 --patch-size 256 256 --cuda --save --seed 1926 --clip_max_norm 1.0  --stage 3 --ste 1 --refresh 1 --loadFromPretrainedSinglemodel 0 --checkpoint stf_0483.pth.tar
```
### Fixed the entropy model
```
python3 update.py checkpoint.pth.tar  -n STFVR
```
###Inference
For  discrete bitrate results at a assign Index: Index belongs in {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
```
    python3 Inference.py --dataset ./dataset/Kodak --s 11 --output_path AttentionVRSTE -p ./STFVR.pth.tar --patch 64 --factormode 0 --factor 0
```
### Continuous bitrate results
For example continuous bitrate  results:
```
    python3 Inference.py --dataset ./dataset/Kodak --s 2 --output_path AttentionVRSTE -p ./STFVR.pth.tar --patch 64 --factormode 1 --factor 0.1
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
