# Build PMC-OA

[English Version](./README.md)

这是我们建立 PMC-OA 数据集的流程, 您需要对其进行修改以适应个性化的需求。

- [TMP](#tmp)
  - [人工智能的数学基础](#人工智能的数学基础)
  - [BiomedBERT](#biomedbert)
  - [PMC Private](#pmc-private)
  - [Low Rank](#low-rank)
  - [KG](#kg)
  - [数据整理](#数据整理)
  - [代码重构](#代码重构)
  - [表格解析](#表格解析)
- [Build PMC-OA](#build-pmc-oa)
  - [安装教程](#安装教程)
  - [关于 PMC-OA 数据集](#关于-pmc-oa-数据集)
  - [项目结构](#项目结构)
  - [参与贡献](#参与贡献)
  - [局限性](#局限性)
  - [引用](#引用)


## 安装教程

1. 创建环境
```bash
conda create -n pubmed python=3.8  # 其他版本可能存在编码问题
conda activate pubmed

pip install -r requirements.txt  # 安装依赖

git clone https://gitee.com/lin_wei_hung/build-pmcoa.git
python setup.py develop  # 安装本项目(开发者模式)
```

2. 执行脚本

```bash
python src/fetch_oa.py --volumes 0 1 2 3 4 5 6 7 8 9  # PMC OA 有 [0-9] 十个分卷可以选
python src/fetch_oa.py --volumes 0 1 2  # 选择 [0,1,2] 三个分卷
```

## 关于 PMC-OA 数据集

PMC 中的部分论文受限于许可不能公开, PMC Open Access ( **PMC OA** ) 是 PMC 的子集, 可以通过 https://www.ncbi.nlm.nih.gov/pmc/tools/ftp/ 下载.
保险起见我们没有使用许可类型为 Non Commercial Use 以及没有明确许可的论文.

PMC OA 提供的文件结构:
```bash
PMC_OA/
  |--PMC000xxxxxx/:
  | |--oa_comm_xml.PMC000xxxxxx.baseline.2022-09-03.filelist.csv
  | |--PMC000xxxxxx/:
  | | |---PMC176545.xml
  | | |--- ...
  |xxx.jsonl  # (img, caption) info extracted
```

## 项目结构
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

## 参与贡献

1.  Fork 本仓库
2.  新建 Feat_xxx 分支
3.  提交代码
4.  新建 Pull Request


## 局限性
1. Pubmed 上的部分 paper 只提供 pdf 格式, 图片无法获取
2. 各种类型的媒体都会被下载, 包括 .mp4, .avi 等格式的音视频文件。

<!-- 2. url 中指定页面的显示格式: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC176545/?report=classic -->


## 引用

```bash
@article{lin2023pmc,
  title={PMC-CLIP: Contrastive Language-Image Pre-training using Biomedical Documents},
  author={Lin, Weixiong and Zhao, Ziheng and Zhang, Xiaoman and Wu, Chaoyi and Zhang, Ya and Wang, Yanfeng and Xie, Weidi},
  journal={arXiv preprint arXiv:2303.07240},
  year={2023}
}
```
