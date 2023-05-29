# CPEER-Dataset
We create an open dataset of **C**hina **P**ostgraduate **E**ntrance **E**xam **R**ecord (CPEER) for data analysis.  
由张诚，黄青林，玉晨甫共同提出的制作考研数据集的邀请。
# Motivation
* 要收集的院校过多  
* 多数院校的信息格式不同，存储形式不同，难以获取结构化数据  
* 很多同学说python数据处理的课程设计在收集数据这块很困难，主要是python在pdf爬取有bug以及栏目名字不统一，实现全自动与半自动获取数据比较困难，如果每个同学都一个一个pdf搞会很棘手以及每个人都重复一件事效率低下  
* __我们希望我们的数据集能在未来被重复使用__  
* 本着从简与搭建基础的原则，我们提供最基础的数据集列的信息，并鼓励大家基于我们的数据集添加更多信息（例如985/211,QS排名等）用于数据分析  

# Dataset Structure
经过我们的讨论，我们暂定数据集的列名如下：  

院校|年份|院系|专业|初试成绩|复试成绩|复试满分|总成绩|是否录取
:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:
华中师范大学|2022|人工智能教育学部|人工智能|400|384|400|92|是
华中科技大学|2023|计算学部|计算机科学与技术|421|91|100|96|是  

__说明__：每一行代表一个考生，出于保护考生信息的隐私，以及考虑到考生信息对数据分析的作用不大，我们不记录考生信息，每一行就代表一名考生  

每一列的信息如下：
列名|是否必填*|描述
:-:|:-:|:-:
院校|是|院校的名称
年份|是|考生考研的年份，格式（2021/2022/2023...)
学院|是|考生所在的学院
专业|可选|考生所在的专业，由于专业可能会存在大方向专业与细分专业的问题，我们暂定这一列自由填写
初试成绩|是|考生研究生考试初试的成绩
复试成绩|是|这一列的情况比较复杂，因为有的学校会给出复试的细分，但是有的学校不给出，因此我们选择只记录复试的综合成绩（从简原则），如需分析复试的细分成绩请自行扩充数据
复试满分|__强烈建议__|该专业复试的满分。由于不同学校的复试满分不同，我们添加这一列使得不同学校之间的复试成绩具有可比性
总成绩|是|学校给出的文档中考生的总成绩（可能存在不同学校加权不同的情况，仅作参考）
是否录取|是|考生是否被录取，格式（是/否）

\* : 如不填写该列，请保留该列名并将该列数据置为空，或者在上传的文档中包含表头

# Update Requirement
请**严格按照**数据集的结构上传您的文件（支持.csv/.xlsx格式)   
可以包含表头，也可以不包含

# Maintainment and Update
从2023年5月30日起至2023年6月17日，我们将会每天根据同学上传数据的负责维护和更新数据集。

# Citation
Updating
