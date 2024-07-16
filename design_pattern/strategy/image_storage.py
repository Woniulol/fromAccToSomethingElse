class ImageStorage:
    def __init__(self, compressor, filter):
        self.compressor = compressor
        self.filter = filter

    def store(self, file_name):
        compressed_file = self.compressor.compress(file_name)
        filtered_file = self.filter.filter(compressed_file)
        return


