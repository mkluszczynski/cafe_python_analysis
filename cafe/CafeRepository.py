from io import TextIOWrapper

import csv


class CafeRepository:

    _csvFileReader: csv.reader
    _columns: list
    _data: list = []

    def __init__(self, data_file: TextIOWrapper) -> None:
        self._csvFileReader = csv.reader(data_file)
        self._getColumns()
        self._mapData()

    # select: name, where 
    def find(self, find_options = {}):
        res = []
        whereRes = []

        if find_options.get("where"):
            res = self._processWhere(find_options["where"]) 

        else:
            res = self._data
            

        if find_options.get('select'):
            res = self._processSelect(res , find_options["select"]) 
        
        return res 


    def findBy(self, findby_options):
        return self.find({"where": findby_options}) 

    def _processWhere(self, where_options) -> list:
        resWhereItem = []
        for row in self._data:
                for where in where_options:
                    for key in where.keys():
                        if where[key] == row[key]:
                            resWhereItem.append(row)
        
        return resWhereItem

    def _processSelect(self, list_to_select, select_options) -> list:
        resSelectList = []
        for row in list_to_select:
                resItemDist = {}
                for select in select_options:
                    resItemDist[select] = row[select]
                
                resSelectList.append(resItemDist)
        
        return resSelectList

    def _getColumns(self) -> list:
        self._columns = self._csvFileReader.__next__()

    def _mapData(self) -> None:
        for index, row in enumerate(self._csvFileReader):
            if index == 0:
                continue
            
            dataRowDict = {}
            for i, column in enumerate(self._columns):
                dataRowDict[column] = row[i]

            self._data.append(dataRowDict)