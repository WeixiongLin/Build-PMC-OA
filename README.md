# BuildPubmed

- [BuildPubmed](#buildpubmed)
  - [PMC OA](#pmc-oa)
  - [软件架构](#软件架构)
  - [安装教程](#安装教程)
  - [使用说明](#使用说明)
  - [参与贡献](#参与贡献)
  - [TODO](#todo)


## PMC OA

PMC 中的部分论文受限于许可不能公开, PMC Open Access ( **PMC OA** ) 是 PMC 的子集, 可以通过 https://www.ncbi.nlm.nih.gov/pmc/tools/ftp/ 下载.

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

## 软件架构
- 源码在 `src/` 中.
- 如果数据量很大得考虑用数据库做持久化


## 安装教程
创建环境
```bash
conda create -n pubmed python=3.8  # 不支持更低版本, 否则编码存在问题
conda activate pubmed

pip install -r requirements.txt  # 安装依赖
python setup.py develop  # 安装本项目
```


## 使用说明

执行 `src/fetch_oa.py` 提取 (image_url, caption)
```bash
python src/fetch_oa.py --volumes 0 1 2 3 4 5 6 7 8 9  # PMC OA 有 [0-9] 十个分卷可以选
python src/fetch_oa.py --volumes 0 1 2  # 选择 [0,1,2] 三个分卷
```

## 参与贡献

1.  Fork 本仓库
2.  新建 Feat_xxx 分支
3.  提交代码
4.  新建 Pull Request

## TODO
- 扫描 PMID, 统计能够获得的总的 document 数量.
- 统计 PMC OA 中包含的 paper, pairs 数量
- 这个爬虫现在可以处理 PMC OA 的部分, 考虑如何获取所有的 PMC 数据



问题:
- 一些 paper 只提供 pdf 格式, 如何提取
- 同一个 url 有时候请求到的数据会不一样, 有时候会返回 PubReader 的那种文件格式
  - 可以在 url 中指定页面的显示格式: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC176545/?report=classic


