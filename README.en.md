# CPEER-Dataset
We create an open dataset of **C**hina **P**ostgraduate **E**ntrance **E**xam **R**ecord (CPEER) for data analysis.  
The dataset will be openly available for everyone to use (please cite us as the "CPEER dataset").


[简体中文](README.md) | [English](README.en.md)  



# Motivation
* There is a large number of universities to collect data from.
* Most universities have different information formats and storage methods, making it difficult to obtain structured data.
* Many students have expressed difficulties in collecting data for their Python data processing projects, particularly due to bugs in PDF scraping and inconsistent column names. It is challenging to achieve full automation or semi-automation in data retrieval, and individual efforts to collect data would be cumbersome and inefficient.
* __We hope that our dataset can be reused in the future.__
* In line with the principles of simplicity and building a foundation, we provide the most basic information in the dataset columns. We encourage everyone to add more information based on our dataset (e.g., 985/211 status, QS rankings, full-time or part-time status, transfer options, etc.) for data analysis purposes.

# Dataset Structure
Deciding which information (i.e., columns) to collect is an important and fundamental question. We have selected some essential column names that will be applicable in the vast majority of cases. Having too many empty columns would compromise the quality of the data. Therefore, it is preferable to minimize the presence of empty columns.
Based on our discussions, we have tentatively established the following column names for the dataset:

University | Year | Faculty | Major | __Written Exam Score__ | Interview Score | Maximum Interview Score | Total Score | Admission Status
:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:
Central China Normal University | 2022 | Faculty of Artificial Intelligence in Education | Artificial Intelligence | 400 | 384 | 400 | 92 | Yes
Huazhong University of Science and Technology | 2023 | Faculty of Computing | Computer Science and Technology | 421 | 91 | 100 | 96 | Yes

__Explanation__:
Each row represents a candidate. In order to protect the privacy of candidates' information and considering that the impact of candidate information on data analysis is minimal, we do not record candidate information. Each row represents one candidate.

The information for each column is as follows:

Column Name | Description
:-:|:-
University | Name of the university
Year | Year of the candidate's graduate entrance exam (format: 2021/2022/2023...)
Faculty | Faculty of the candidate
Major | Major of the candidate. As majors may have broad categories and specialized subcategories, this column is left open for free entry.
__Written Exam Score__ | Score of the candidate in the written exam of the graduate entrance exam. <br />* __Regarding the exam subjects__: Collecting the specific content of the written exam for each school is challenging. Therefore, only the final written exam score is provided here. Since the content of the written exam varies across schools and majors, there may be deviations in score comparisons. It is recommended to consider the [`Major`] when comparing written exam scores.<br />* __Regarding academic and professional master's programs__: Due to the difficulty in collecting information on whether a candidate is pursuing an academic or professional master's degree, and considering that the majority of the data pertains to academic master's programs, no distinction is made in this database.  |
|Interview Score | This column is more complex. Some schools provide detailed scores for the interview, while others do not. Therefore, we choose to record only the overall interview score (following the principle of simplicity). If you need to analyze the detailed interview scores, please expand the data accordingly.  
|Maximum Interview Score | The maximum score for the interview in the respective major. This column is added to enable comparability of interview scores across different schools.  |
|Total Score | The total score of the candidate as provided in the document from the university. Please note that different universities may weigh the scores differently, so it should be considered as a reference.  |
|Admission Status | Indicates whether the candidate was admitted (format: Yes/No).  |


# Current Progress
![image](https://github.com/Younai2021/CPEER-Dataset/blob/main/imgs/echarts.png)  


# Archives
Version|rows|#University
:-:|:-:|:-:
v1.0|7349|10
v1.1|14592|30


# Citation

**Please cite us as: CPEER dataset.**

# Notations


1. All finalized versions of the dataset have undergone the following normalization and formatting steps, as well as the manual removal of extremely rare special cases. Please note that these adjustments may lead to deviations in your understanding.

```python
data = pd.read_excel('CPEER.xlsx')
data = data.replace('\t', '', regex=True).replace('\n', '', regex=True).replace(' ', '', regex=True).replace('（', '(', regex=True).replace('）', ')', regex=True)
data['院校'] = data['院校'].astype(str)
data['年份'] = data['年份'].astype(int)
data['院系'] = data['院系'].astype(str)
data['专业'] = data['专业'].astype(str)
data['初试成绩'] = data['初试成绩'].astype(float)
data['复试成绩'] = data['复试成绩'].astype(float)
data['复试满分'] = data['复试满分'].astype(float)
data['总成绩'] = data['总成绩'].astype(float)
data['是否录取'] = data['是否录取'].astype(str)
data.to_excel('CPEER.xlsx', sheet_name='data', index=False)
```

2. Please note that the names of the same majors may vary across different universities. For example, one university may simply list a major as '电子信息' in the electronic information field, while others may use '085422-电子信息'. It is recommended to use **fuzzy search** when filtering information across different universities.









