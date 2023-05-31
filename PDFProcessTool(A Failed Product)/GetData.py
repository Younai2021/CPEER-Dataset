import numpy as np
import pandas as pd
import pdfplumber
import sqlite3
import shutil
import os
import re
from copy import deepcopy

class ToolBox:
    def __init__(self, Data: pd.DataFrame):
        self.data = self.clean_data(Data)
        self.cp_data = Data
        pass

    def clean_data(self, data):
        for col in data.columns:
            if data[col].dtype == "O":
                data[col] = data[col].apply(lambda x: x.replace("\n",""))
        return data

    def SelectColumns(self, ToSaveColumns: list):
        for _Save in ToSaveColumns:
            if _Save not in self.data.columns:
                return

        self.cp_data = deepcopy(self.data)
        self.data = self.data.loc[:, ToSaveColumns]
        pass

    def AddColumns(self, AddColumnsName: str, AddColumnsValue):
        self.cp_data = deepcopy(self.data)
        self.data[AddColumnsName] = np.full(self.data.shape[0], AddColumnsValue)
        pass

    def RenameColumns(self, RenameList: list):
        self.cp_data = deepcopy(self.data)
        if self.data.shape[1] != len(RenameList):
            print("RenameList size isn't match table shape")
        else:
            self.data.columns = RenameList
        pass

    def DelLine(self, ToDeleteList: list):
        self.cp_data = deepcopy(self.data)
        self.data.drop(index=ToDeleteList, inplace=True)
        pass

    def Withdraw(self):
        self.data = deepcopy(self.cp_data)
        pass

    def Drop(self):
        pass

    def Save(self):
        pass

    def __Show(self):
        print(self.data)
        pass



class FuckPDF:

    def __init__(self, WorkPath='./'):
        """
            ToProcess PDFs put into -> WorkPath + '/Data'
        """
        print("Init...")
        assert os.path.exists(WorkPath + 'Data/'), 'No Data Path'
        if os.path.exists(WorkPath + 'ProblemPDF/') is False:  os.makedirs(WorkPath + 'ProblemPDF/')
        if os.path.exists(WorkPath + 'FinishPDF/') is False:  os.makedirs(WorkPath + 'FinishPDF/')
        if os.path.exists(WorkPath + 'SaveData/') is False:  os.makedirs(WorkPath + 'SaveData/')
        assert os.path.exists(WorkPath + 'ProblemPDF/') is True, 'Create ProblemPDF Path Error'
        assert os.path.exists(WorkPath + 'FinishPDF/') is True, 'Create FinishPDF Path Error'
        assert os.path.exists(WorkPath + 'SaveData/') is True, 'Create SaveData Path Error'

        self.PDFName_List = []
        print(f"Found {self.__CountFile(WorkPath + 'Data/')} PDF files")

        self.WorkPath = WorkPath
        self.ProblemPath = WorkPath + 'ProblemPDF/'
        self.FinishPath = WorkPath + 'FinishPDF/'
        self.SavePath = WorkPath + 'SaveData/'

        input('>>> Press any to Work...')
        self.Run()
        pass

    def __CountFile(self, FilePath):
        _CountPdfs = 0
        files = os.listdir(FilePath)
        for file in files:
            file_d = os.path.join(FilePath, file)
            if os.path.isdir(file_d):
                _CountPdfs += self.__CountFile(FilePath=file_d)
            else:
                ext = os.path.splitext(file)[1]
                if ext == '.pdf':
                    _CountPdfs += 1
                    self.PDFName_List.append(file_d)
        return _CountPdfs
        pass

    def __SomeThing_Crash(self, FilePath):
        '''
            put into -> ProblemTable Fold
            del from -> TD Fold
        '''
        shutil.move(FilePath, self.ProblemPath)
        pass

    def __SaveTable(self, FilePath, data:pd.DataFrame):
        '''
            Design Save Method
        '''



    def Run(self):
        for PDFName in self.PDFName_List:
            _pdf = pdfplumber.open(PDFName)
            _PageCount = len(_pdf.pages)
            # -------------- step1: View PDF Text -------------- #
            print("-----------------------------------------------------")
            print("GET PDF path: ", PDFName)
            input('>>> Press any to continue')

            for page in _pdf.pages:
                print(page.extract_text())

            _switch1 = input("Is well ? 0/1 : 0->bad  1->good")
            if _switch1 == '0':
                _pdf.close()
                self.__SomeThing_Crash(PDFName)
                continue

            # -------------- step2: Extract PDF Table -------------- #
            tables = []
            for _page in _pdf.pages:
                tables += _page.extract_tables()

            if len(tables) == 0:
                print("Table not captured, the PDF will throw it into the ProblemPath")
                continue

            col = [c.replace("\n", "") for c in tables[0][0]]
            print(f'columns: {col}')
            data_df = pd.DataFrame()
            for table in tables:
                _table = pd.DataFrame(table)
                if col in _table.values:
                    _table.drop(index=[0], inplace=True)
                data_df = pd.concat([data_df, _table])

            data_df.columns = col
            data_df.reset_index(inplace=True)

            print(data_df)

            _switch2 = input("Is well ? 0/1 : 0->bad  1->good")
            if _switch2 == '0':
                _pdf.close()
                self.__SomeThing_Crash(PDFName)
                continue

            # -------------- step3: Cropping Data with Tool Box -------------- #
            # funtion:
            # SelectColumns/AddColumns/RenameColumns/DelLine/Withdraw/DropTable/SaveTable

            fl_for_crash = False
            tb = ToolBox(data_df)

            while True:
                print("----------------")
                print("- ToolBox -")
                print("0. | SelectColumns")
                print("1. | AddColumns")
                print("2. | RenameColumns")
                print("3. | DelLine")
                print("4. | Withdraw")
                print("5. | DropTable")
                print("6. | SaveTable")

                _select = input("To Choose Which One To Use")
                if _select == '0':
                    print(f'columns: {col}')
                    ToSaveColumns = input("input: To Save Columns")
                    SaveColumnsList = re.split(',|，', ToSaveColumns.replace(" ", ""))
                    tb.SelectColumns(SaveColumnsList)
                elif _select == '1':
                    AddColumnName = input("input: Add Column Name")
                    AddColumnValue = input("input: Add Column Value")
                    tb.AddColumns(AddColumnName, AddColumnValue)
                elif _select == '2':
                    Renames = input("input: RE-Name list")
                    RenamesList = re.split(',|，', Renames.replace(" ", ""))
                    tb.RenameColumns(RenamesList)
                elif _select == '3':
                    Del_str = input("input: DelList list     |--warning: input like: 8 or 6-19")
                    DelList = []
                    if '-' in Del_str:
                        DelList = [i for i in range(int(re.split('-', Del_str)[0]), int(re.split('-', Del_str)[1]) + 1)]
                    else:
                        DelList = [int(Del_str)]
                    tb.DelLine(DelList)
                elif _select == '4':
                    tb.Withdraw()
                elif _select == '5':
                    fl_for_crash = True
                    break
                else:
                    break

                print(tb.data)

            if fl_for_crash:
                _pdf.close()
                self.__SomeThing_Crash(PDFName)
                continue

            ### Save good Table ###

            # self.__SaveTable(PDFName, tb.data)
            name = input("请输入保存名称")
            print('Save Table -> ', self.SavePath + f'{name}.csv')
            tb.data.to_csv(self.SavePath + f'{name}.csv', index=False, encoding='utf-8_sig')

            _pdf.close()
            shutil.move(PDFName, self.FinishPath)

        pass

    def ViewText(self):
        '''
            attention: one page / many pages
        '''
        pass

    def Extract_Table(self):
        '''
            attention: connect many pages
        '''
        pass

    def ViewTable(self):
        '''

        '''
        pass

    def SaveTabel(self):
        pass

fk = FuckPDF()

# ========================================= test ==========================================#

# Del_str = input()
# print( int(re.split('-', Del_str)[1]) + 1 )
# DelList = [i for i in range(int(re.split('-', Del_str)[0]), int(re.split('-', Del_str)[1]) + 1)]
# print(DelList)
# a = [[1, 2, 3, 4], [2, 3, 4, 5], [5, 6, 7, 8]]
# b = pd.DataFrame(a)
# tb = ToolBox(b)
# print(tb.data)
# tb.SelectColumns([1, 2])
# print(tb.data)

# path = r'C:\Users\HQL\Desktop\python数据处理\CourseDesign\Data\南方科技大学计算机科学与工程系2022年硕士研究生招生拟录取名单公示.pdf'
# path = r'C:\Users\HQL\Desktop\python数据处理\CourseDesign\Data\西藏大学2022年硕士研究生拟录取名单（调剂生）.pdf'
# def test():
#     pdf = pdfplumber.open(path)
#     FirstPage = pdf.pages[0]
#     print(len(pdf.pages))
#     tables = FirstPage.extract_tables()
#     print(tables[0])
#     table_df = pd.DataFrame(tables[0][1:], columns=tables[0][0])
#     print(table_df)
#
#
# def test2():
#     pdf = pdfplumber.open(path)
#     tables = []
#     for _page in pdf.pages:
#         _tables = _page.extract_tables()
#         tables += _tables
#
#     assert len(tables) != 0
#     col = [c.replace("\n", "") for c in tables[0][0]]
#
#     print(col)
#     _A = pd.DataFrame()
#     for table in tables:
#         # table_df = pd.DataFrame(table[1:], columns=table[0])
#
#         _table = pd.DataFrame(table[0:])
#         if col in _table.values:
#             _table.drop(index=[0], inplace=True)
#         _A = pd.concat([_A, _table])
#         # print(table_df)
#     _A.columns = col
#     _A.reset_index(inplace=True)
#     print(_A)
#     tb = ToolBox(_A)
#     print(_A.columns)
#     ToSaveColumns = input("input: To Save Columns")
#     SaveColumnsList = re.split(',|，', ToSaveColumns.replace(" ", ""))
#     # SaveColumnsList = [st.replace("//", "/") if type(st) == str else st for st in SaveColumnsList]
#     print(SaveColumnsList)
#     tb.SelectColumns(SaveColumnsList)
#     print(tb.data)
# # test()
# test2()
#
#
# def __CountFile(FilePath):
#     _CountPdfs = 0
#     files = os.listdir(FilePath)
#     for file in files:
#         file_d = os.path.join(FilePath, file)
#         if os.path.isdir(file_d):
#             _CountPdfs += __CountFile(FilePath=file_d)
#         else:
#             ext = os.path.splitext(file)[1]
#             _CountPdfs += 1 if ext == '.pdf' else 0
#             print(file_d)
#     return _CountPdfs
#     pass


# path = './Data'
# # assert os.path.exists('./' + 'Data/') == False, 'No Data Path'
# # if os.path.exists(path + 'ProblemPDF/') is False:  os.makedirs(path + 'ProblemPDF/')
# print(__CountFile(path))
# # input('>>> press any continue...')
# # os.system('clear')
# pdf = pdfplumber.open('./Data\南方科技大学计算机科学与工程系2022年硕士研究生招生拟录取名单公示.pdf')
# # print(len(pdf.pages))
# for page in pdf.pages:
#     print(page.extract_text())
#     tables = page.extract_table()
#     print(len(tables))
#     for table in tables:
#         print(table)
#         table_df = pd.DataFrame(table)
#         # print(table_df)


# path = './'
# shutil.move(path + 'Data/西藏大学2022年硕士研究生拟录取名单（调剂生）.pdf', path + 'ProblemPDF')