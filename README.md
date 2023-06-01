# CPEER-Dataset
We create an open dataset of **C**hina **P**ostgraduate **E**ntrance **E**xam **R**ecord (CPEER) for data analysis.  
由张诚，黄青林，玉晨甫共同提出的制作考研数据集的邀请。  
我们公开数据集供所有人使用（请引用我们: CPEER dataset）
# Motivation
* 要收集的院校过多  
* 多数院校的信息格式不同，存储形式不同，难以获取结构化数据  
* 很多同学说python数据处理的课程设计在收集数据这块很困难，主要是python在pdf爬取有bug以及栏目名字不统一，实现全自动与半自动获取数据比较困难，如果每个同学都一个一个pdf搞会很棘手以及每个人都重复一件事效率低下  
* __我们希望我们的数据集能在未来被重复使用__  
* 本着从简与搭建基础的原则，我们提供最基础的数据集列的信息，并鼓励大家基于我们的数据集添加更多信息（例如985/211,QS排名, 是否全日制，是否调剂等）用于数据分析  

# Dataset Structure
收集哪些信息（i.e. 列）是一个重要和基础的问题。我们筛选出了一些最基本的列名在绝大多数情况下都可以满足。空列太多会使得数据质量下降。所以我们希望最好不要出现空列。 
经过我们的讨论，我们暂定数据集的列名如下：  

院校|年份|院系|专业|__初试成绩__|复试成绩|复试满分|总成绩|是否录取
:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:
华中师范大学|2022|人工智能教育学部|人工智能|400|384|400|92|是
华中科技大学|2023|计算学部|计算机科学与技术|421|91|100|96|是  

__说明__：
每一行代表一个考生，出于保护考生信息的隐私，以及考虑到考生信息对数据分析的作用不大，我们不记录考生信息，每一行就代表一名考生  

每一列的信息如下：

列名|描述
:-:|:-
院校|院校的名称
年份|考生考研的年份，格式（2021/2022/2023...)
院系|考生所在的学院
专业|考生所在的专业，由于专业可能会存在大方向专业与细分专业的问题，我们暂定这一列自由填写
__初试成绩__|考生研究生考试初试的成绩<br /> * __关于考试科目__：由于收集每个学校的初试考核内容相当困难，此处**只提供最后的初试成绩**。因为每个学校每个专业的初试考核内容不同，成绩在横向对比时可能存在偏差。因此建议在对比初试分数时结合[`专业`]考虑<br /> * __关于学硕与专硕__：由于绝大部分数据都是学硕，以及想要收集是否是学硕或专硕相当困难。因此在此数据库中**不做区分**  
复试成绩|这一列的情况比较复杂，因为有的学校会给出复试的细分，但是有的学校不给出，因此我们选择只记录复试的综合成绩（从简原则），如需分析复试的细分成绩请自行扩充数据
复试满分|该专业复试的满分。由于不同学校的复试满分不同，我们添加这一列使得不同学校之间的复试成绩具有可比性
总成绩|学校给出的文档中考生的总成绩（可能存在不同学校加权不同的情况，仅作参考）
是否录取|考生是否被录取，格式（是/否）


# Current Progress
![image](https://github.com/Younai2021/CPEER-Dataset/blob/main/imgs/echarts.png)  
已包含的数据条数：**18235**

已经统计好的院校：  37所

|#| 北京大学 | 华东师范大学 | 北京师范大学 |同济大学 |电子科技大学|
|:------: | :------: | :----------: | :----------: |:----------: |:----------: |
|5|西安电子科技大学      | 北京邮电大学| 新疆大学   |  北京科技大学     |中国地质大学（北京）|
|10|    北京航天航空大学  |  上海财经大学 | 武汉大学 |  西南财经大学| 上海大学 | 
|15|南京理工大学 | 南京航天航空大学 | 北京理工大学| 华中师范大学|华中科技大学
|20|中南财经政法大学 |哈尔滨工业大学|东北师范大学|北京化工大学|中央音乐学院|  
|25|江南大学|华中农业大学|大连海事大学|南昌大学|海南大学|
|30|安徽大学|福州大学|河北工业大学|西北大学|宁夏大学|
|35|西藏大学|南开大学




# Archives
Version|rows|#University
:-:|:-:|:-:
v1.0|7349|10
v1.1|14592|30
# Upload Requirements
欢迎大家贡献自己的一份力量，支持共享与互惠  
请**严格按照**数据集的结构上传您的文件（支持.csv/.xlsx格式)，方便我们更新数据集。  
上传要求：
* 将文件上传到课程QQ群文件中
* 以学校为最小单位上传文档（参照文件格式：XXX大学.csv 或 XXX大学.xlsx），请在统计时尽量统计好所有相关专业的信息，提供有效准确的数据，为了保证数据集的质量我们会在审核后增加到数据集
* 请在工作前查看文件夹是否已经有相关院校，注意不要上传重复的学校，避免重复劳动

* **请严格按照如下表头：院校|年份|院系|专业|初试成绩|复试成绩|复试满分|总成绩|是否录取**  

# Maintainment and Update
从2023年5月30日起至2023年6月17日，我们将会定期根据同学上传数据的负责维护和更新数据集。

# Citation
Contributers:{黄青林，玉晨甫，张诚，杨名宇，李淑芳，张梓莹，梁思思，缪秉辰，王镜淇，陈凯旋，何瑛琪，方瑞哲 still adding...}  

**Please cite us as: CPEER dataset.**

# Notations
1，放弃/少数民族/夏历营等特殊的数据不添加  

![image](https://github.com/Younai2021/CPEER-Dataset/blob/main/imgs/%E6%94%BE%E5%BC%83.png)  

2，不同院校复试满分不一样的现象  

![image](https://github.com/Younai2021/CPEER-Dataset/blob/main/imgs/%E6%A0%87%E5%87%86.jpg)

3， 所有成型的version版本是经过如下规范化格式处理，以及人为剔除极个别特殊数据的stable版本，有可能出现因为我们修整后，**造成你的理解产生偏差**

```python
data = pd.read_excel('CPEER.xlsx')
data = data.replace('\t','', regex=True).replace('\n','', regex=True).replace(' ', '', regex=True)
data['院校'] = data['院校'].astype(str)
data['年份'] = data['年份'].astype(int)
data['院系'] = data['院系'].astype(str)
data['专业'] = data['专业'].astype(str)
data['初试成绩'] = data['初试成绩'].astype(float)
data['复试成绩'] = data['复试成绩'].astype(float)
data['复试满分'] = data['复试满分'].astype(float)
data['总成绩'] = data['总成绩'].astype(float)
data['是否录取'] = data['是否录取'].astype(str)
data.to_excel('CPEER.xlsx', sheet_name='data',index=False)
```
4， 请注意 不同院校但相同专业的名字可能存在出入，例如有个院校在电子信息类中直接描述为：'电子信息'，但有些为：'085422-电子信息'，推荐在跨院校筛选信息时使用**模糊搜索**

# Digression

如果你也苦于如何获取PDF内的数据，希望下面能帮助到你 ：）

- 推荐辅助提取软件：[Adobe Acrobat(付费/免费试用)](https://www.adobe.com/acrobat.html)

如果你希望自己搞一套处理PDF的程序，希望下面能帮助到你：）

- 一份自己写的不好用的半自动批处理PDF的py：[PDFProcessTool(A Failed Product)](https://github.com/Younai2021/CPEER-Dataset/tree/main/PDFProcessTool(A%20Failed%20Product))








