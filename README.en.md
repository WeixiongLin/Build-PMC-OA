# BuildPubmed

Collect data from Pubmed.

- [BuildPubmed](#buildpubmed)
  - [Build up ENV](#build-up-env)
    - [Conda](#conda)
    - [Dependency](#dependency)
  - [Others](#others)
      - [Description](#description)
      - [Installation](#installation)
      - [Instructions](#instructions)
      - [Contribution](#contribution)
      - [PMC Open Access Subset](#pmc-open-access-subset)

## Build up ENV

### Conda
```bash
conda create -n pubmed python=3.8  # 不支持更低版本, 编码存在问题
conda activate pubmed

python setup.py develop
```

### Dependency
```bash
pip install -r requirements.txt
```
- pandas >= 1.1.3
- beautifulsoup4
- lxml
- tqdm
- jsonlines

## Others

#### Description
Collect data from Pubmed.


#### Installation

1.  Built up ENV
2.  Install dependencies
3.  xxxx

#### Instructions

1.  xxxx
2.  xxxx
3.  xxxx

#### Contribution

1.  Fork the repository
2.  Create Feat_xxx branch
3.  Commit your code
4.  Create Pull Request

#### PMC Open Access Subset
PMC is not available for bulk download due to licence restrictions. Only a subset of PMC is open to public.

[Download Page](https://www.ncbi.nlm.nih.gov/pmc/tools/ftp/)

```bash
# ROCO API
# https://www.ncbi.nlm.nih.gov/pmc/utils/oa/oa.fcgi?tool=roco-fetch&email=johannes.rueckert@fh-dortmund.de&id=PMC4608653
# wget -Uri ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_package/8d/34/PMC4608653.tar.gz -OutFile E:\Dataset

wget https://www.ncbi.nlm.nih.gov/pmc/articles/PMC555952/bin/1468-6708-6-4-2.jpg -OutFile E:\Dataset
```
