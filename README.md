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
| Variable-rate mode|0.0018, 0.0035, 0.0067, 0.0130, 0.025, 0.0483, 0.0932, 0.18  |  [stf_VR]()  |

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

The training and test dataset are same to [STF](https://github.com/Googolxx/STF)
```
python3 train.py  -d ./dataset  -e 21 -lr 1e-4 -n 8 --batch-size 16 --test-batch-size 64 --aux-learning-rate 1e-3 --patch-size 256 256 --cuda --save --seed 1926 --clip_max_norm 1.0  --stage 2 --ste 0 --refresh 1 --loadFromPretrainedSinglemodel 1 --checkpoint stf_0483.pth.tar
```

```
python3 train.py  -d ./dataset  -e 66 -lr 1e-5 -n 8 --batch-size 16 --test-batch-size 64 --aux-learning-rate 1e-3 --patch-size 256 256 --cuda --save --seed 1926 --clip_max_norm 1.0  --stage 3 --ste 1 --refresh 1 --loadFromPretrainedSinglemodel 0 --checkpoint checkpoint.pth.tar
```
### Fixed the entropy model
```
python3 update.py checkpoint_best_loss.pth.tar  -n STFVRImageNetSTE
```
### Inference
For  discrete bitrate results at a assign Index: Index belongs in {0, 1, 2, 3, 4, 5, 6, 7, 8}
```
python3 Inference.py --dataset ./dataset/Kodak --s 11 --output_path STFVRSTE -p ./STFVRImageNetSTE.pth.tar --patch 64 --factormode 0 --factor 0 --cuda
```
### Continuous bitrate results
For example continuous bitrate  results:
```
python3 Inference.py --dataset ./dataset/Kodak --s 22 --output_path STFVRSTE -p ./STFVRImageNetSTE.pth.tar --patch 64 --factormode 1 --factor 0.1 --cuda
```

# RD results on Kodak
The fixed-rate results are obtained by the provided fixed-rate models from [STF](https://github.com/Googolxx/STF).

![](asserts/STF.png)


## Citation
```
@inproceedings{zou2022the,
  title={The Devil Is in the Details: Window-based Attention for Image Compression},
  author={Zou, Renjie and Song, Chunfeng and Zhang, Zhaoxiang},
  booktitle={CVPR},
  year={2022}
}
```
```
@article{tong2023qvrf,
  title={QVRF: A Quantization-error-aware Variable Rate Framework for Learned Image Compression},
  author={Tong, Kedeng and Wu, Yaojun and Li, Yue and Zhang, Kai and Zhang, Li and Jin, Xin},
  journal={arXiv preprint arXiv:2303.05744},
  year={2023}
}
```
