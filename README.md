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
$$Usage
### Training
stage 1
```
python train.py -d ./dataset  -e 2000 -lr 1e-4 -n 8 --batch-size 8 --test-batch-size 64 --aux-learning-rate 1e-3 --patch-size 256 256 --cuda --save --seed 1926 --clip_max_norm 1.0  --stage 1 --ste 0  --loadFromPretrainedSinglemodel 0
```
stage 2
```
python3 train.py  -d ./dataset  -e 500 -lr 1e-4 -n 8 --batch-size 8 --test-batch-size 64 --aux-learning-rate 1e-3 --patch-size 256 256 --cuda --save --seed 1926 --clip_max_norm 1.0  --stage 2 --ste 0  --refresh 1 --loadFromPretrainedSinglemodel 0 --checkpoint checkpoint_best_loss.pth.tar
```
stage 3
```
python3 train.py  -d ./dataset  -e 500 -lr 1e-4 -n 8 --batch-size 8 --test-batch-size 64 --aux-learning-rate 1e-3 --patch-size 256 256 --cuda --save --seed 1926 --clip_max_norm 1.0  --stage 3 --ste 1 --refresh 1 --loadFromPretrainedSinglemodel 0 --checkpoint checkpoint_best_loss.pth.tar
```

###Inference
```
python3 Inference.py --dataset ./dataset/Kodak --s 8 --output_path STFVR -p ./checkpoint_best_loss.pth.tar --patch 64 --factormode 0 --factor 0
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
