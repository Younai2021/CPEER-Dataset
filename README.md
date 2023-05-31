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

院校|年份|院系|专业|__初试成绩*__|复试成绩|复试满分|总成绩|是否录取
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

已包含的数据条数：**14594**

已经统计好的院校：  20所

| 北京大学 | 华东师范大学 | 北京师范大学 |同济大学 |电子科技大学|
| :------: | :----------: | :----------: |:----------: |:----------: 
     **西安电子科技大学**       |  **北京邮电大学** | **新疆大学**   |  **北京科技大学**     |
|    **北京航天航空大学**  |  **上海财经大学** | **武汉大学** |  **西南财经大学** | **上海大学** | 
**南京理工大学** | **南京航天航空大学** | **北京理工大学** | **华中师范大学** |**华中科技大学**
 |**中南财经政法大学** |哈尔滨工业大学|东北师范大学|北京化工大学|中央音乐学院|

|江南大学|华中农业大学|大连海事大学|南昌大学|海南大学|
中国地质大学（北京）|



# Archives
Version|rows|#University
:-:|:-:|:-:
v1.0|7349|10
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
Contributers:{黄青林，玉晨甫，张诚，杨名宇，李淑芳，张梓莹，梁思思，缪秉辰 still adding...}  

**Please cite us as: CPEER dataset.**

# Notations
1，放弃/少数民族/夏历营等特殊的数据不添加  

![image](https://github.com/Younai2021/CPEER-Dataset/blob/main/imgs/%E6%94%BE%E5%BC%83.png)  

2，不同院校复试满分不一样的现象  

![image](https://github.com/Younai2021/CPEER-Dataset/blob/main/imgs/%E6%A0%87%E5%87%86.jpg)

# Digression

前文提及半自动方法比较吃力也不是空穴来风，我们使用过的辅助提取软件中，效果比较理想为：[Adobe Acrobat(付费/免费试用)](https://www.adobe.com/acrobat.html)

之后我们尝试做的一份基于pdfplumber的半自动py程序，但是效果同样不太理想（不规则表格是个硬伤），程序描述如下：

这是一个半自动抓取PDF表格的程序，虽然它还是有非常多的缺陷，但是拿来凑合还是可以的，一切输出和交互都在控制台实现 ：)

（先在GetData.py旁创建 /Data 文件夹并将所需要运行的PDF放进去，然后运行py）

- 初始化：扫描文件夹中所有PDF做出统计，创建三个文件夹：/FinishPDF、/ProblemPDF、/SaveData
- 接下来逐个PDF读取：
  - 先抓取所有页面的文字呈现，查看PDF是否保留（按下0丢弃/1继续，并回车），如果选择0则PDF将转移至 /ProblemPDF
  - 选择继续则，自动抓取所有表格并自动拼接，生成DataFrame，查看PDF是否保留（按下0丢弃/1继续，并回车）
  - 选择继续则，进入工具箱ToolBox，提供了几个便捷操作：
    - 0： 选择你需要保留的columns， 输入中文，以及逗号隔开（中/英），回车即可
    - 1： 加入一列相同的数据（常用于加入学校名称），用法为：先输入表头名，再输入填入数据
    - 2： 重命名所有columns，输入同等栏数量的标签（逗号隔开，中英文都可），若是数量不匹配不会更新
    - 3： 删除某行（不太好用，因为控制台对DataFrame的输出会压缩行，显示不完全），输入数字，或数字-数字都可以删除，eg：7  或  2-19
    - 4： 可以支持一次撤回，以防错误操作
    - 5： 丢弃，放回 /ProblemPDF
    - 6： 保存
  - 输入院校名称，即可保留为XXXX.csv

*如果有任何问题可以随时终止程序*

当然这个半自动程序真的有许多bug，如果执意使用本程序但遇到bug请找一下作者..



... 当然，想过半自动当然也想过全自动，曾经有方案是：爬取所有表格后，通过词分类模型将不同字但同语义的聚类，实现标签归一后提取数据。但是表格不规则样式与院校对PDF做特殊处理（图片化）还是造成很大影响。方案二是走OCR文本扫描的老路，同时看了一篇图神经解构不规则表格信息提取的文章：[GFTE: Graph-based Financial Table Extraction](https://arxiv.org/abs/2003.07560)，但还是被不规则处理绊住脚，最终还是决定发起共筑数据集的号召...



