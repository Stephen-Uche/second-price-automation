from abc import ABCMeta, abstractmethod


class IFileHandler(metaclass=ABCMeta):
	@abstractmethod
	def write(self, content: str, path: str) -> None:
		pass

	def read(self, path: str) -> None:
		pass	