from abc import ABC, abstractmethod

class Compressor:
    @abstractmethod
    def compress(self, data):
        ...

class GzipCompressor(Compressor):
    def compress(self, data):
        print("compressed data using gzip")

class Bzip2Compressor(Compressor):
    def compress(self, data):
        print("compressed data using bzip2")