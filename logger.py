from prettytable import PrettyTable
import datetime
import json
from enum import Enum

LogFile = 'logs/logging.json'
Format = '%H:%M:%S %a %d/%m/%y'


class LogType(Enum):
	LOG = 1
	ERROR = 2


class Logging():

	def GetLogsOfType(type, table=False):
		with open(LogFile, 'r') as f:
			data: dict = json.load(f)

		if not table: return data

		LogTable = PrettyTable()
		LogTable.title = 'GetLogsOfType'
		LogTable.field_names = ['ID', 'Message', 'Type', 'Time']

		for i, v in data.items():
			if v['type'] == type.value:
				LogTable.add_row([i, v['msg'], v['type'], v['time']])
		return LogTable.get_string(sortby='ID',
		                           sort_key=lambda row: int(row[0]),
		                           reversesort=True)

	def GetLogFromID(ID, table=False):
		with open(LogFile, 'r') as f:
			data: dict = json.load(f)

		data = data[str(ID)]
		if not table: return data

		LogTable = PrettyTable()
		LogTable.title = 'GetLogFromID'
		LogTable.field_names = ['ID', 'Message', 'Type', 'Time']
		LogTable.add_row([ID, data['msg'], data['type'], data['time']])
		return str(LogTable)

	def GetAllLogs(table=False):
		with open(LogFile, 'r') as f:
			data: dict = json.load(f)

		if not table: return data

		LogTable = PrettyTable()
		LogTable.title = 'GetAllLogs'
		LogTable.field_names = ['ID', 'Message', 'Type', 'Time']

		for i, v in data.items():
			LogTable.add_row([i, v['msg'], v['type'], v['time']])

		return LogTable.get_string(sortby='ID',
		                           sort_key=lambda row: int(row[0]),
		                           reversesort=True)


class LogInfo():

	def __init__(self, msg, type, save):
		self.Msg = msg
		self.Type = type
		self.Id = self._FindID()
		self.CreateTime = datetime.datetime.today().strftime(Format)

		if save: self.SaveLog()

	def __str__(self):
		LogTable = PrettyTable()
		LogTable.title = 'LogInfo'
		LogTable.field_names = ['ID', 'Message', 'Type', 'Time']
		LogTable.add_row([self.Id, self.Msg, self.Type, self.CreateTime])

		return str(LogTable)

	def _FindID(self):
		with open(LogFile, 'r') as f:
			data = json.load(f)

			if len(data) < 1:
				return "0"
			elif len(data) >= 1:
				return str(len(data))

	def SaveLog(self):
		with open(LogFile, 'r') as f:
			data = json.load(f)

		with open(LogFile, 'w') as f:
			NewData = {}
			NewData['msg'] = self.Msg
			NewData['type'] = self.Type.value
			NewData['time'] = self.CreateTime

			data[self.Id] = NewData
			json.dump(data, f)
			
			print(NewData)
