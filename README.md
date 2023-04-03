# Build PMC-OA

[中文版本](./README.zh.md)

This is our pipeline for the development of PMC-OA.
You might need further adaptation to use it for your own purpose.

- [Build PMC-OA](#build-pmc-oa)
  - [Installation](#installation)
  - [About PMC-OA](#about-pmc-oa)
  - [Structure](#structure)
  - [Contribution](#contribution)
  - [Limitation](#limitation)
  - [Cite](#cite)

## Installation

1. Setup ENV
```bash
conda create -n pubmed python=3.8  # not test for other version
conda activate pubmed

pip install -r requirements.txt

git clone https://gitee.com/lin_wei_hung/build-pmcoa.git
python setup.py develop  # choose developer mode for customization
```

2. Run the script

```bash
python src/fetch_oa.py --volumes 0 1 2 3 4 5 6 7 8 9  # 10 volumes for PMC OA in total
python src/fetch_oa.py --volumes 0 1 2  # Choose volumes of 0,1,2 only
```

## About PMC-OA
PMC-OA(Pubmed Open Acess Subset) is built with public papers in Pubmed, which can be downloaded from [pubmed page](https://www.ncbi.nlm.nih.gov/pmc/tools/ftp/).

Due to the issue of copyright, the papers with Non-Commertial-Use liscence and ones with no liscence is not included in PMC-OA.
You might customize the repo for your own purpose.

## Structure
```
setup.py
src/
  |--fetch_oa.py: main script for download PMC-OA
  |--args/
  | |--args_oa.py: Configures for pipeline
  |--parser/
  | |--parse_oa.py: Parse web pages into list of <img, caption> pairs
  |--utils/
  | |--io.py: 
```

## Contribution

1.  Fork the repository
2.  Create Feat_xxx branch
3.  Commit your code
4.  Create Pull Request

## Limitation
1. Some of the paper are only presented in pdf formart, the figures in those would not be obtained by this pipeline
2. Media files other than images might also be downloaded, such as suffix .mp4, .avi.

## Cite

```bash
@article{lin2023pmc,
  title={PMC-CLIP: Contrastive Language-Image Pre-training using Biomedical Documents},
  author={Lin, Weixiong and Zhao, Ziheng and Zhang, Xiaoman and Wu, Chaoyi and Zhang, Ya and Wang, Yanfeng and Xie, Weidi},
  journal={arXiv preprint arXiv:2303.07240},
  year={2023}
}
```
