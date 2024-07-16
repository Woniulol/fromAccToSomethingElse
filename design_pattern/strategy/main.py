# What is the difference between strategy pattern and state pattern?
# We use both pattern to change the behavior of an object

# However, in strategy pattern, the behavior is depends on the strategy object,
# the behavior of different strategy object can be different.

# In state pattern, the behavior is represented by a specific state object

from image_storage import ImageStorage
from compressor import Compressor, GzipCompressor, Bzip2Compressor
from filter import Filter, BlackAndWhiteFilter, GrayScaleFilter

if __name__ == '__main__':
    image_storage = ImageStorage(GzipCompressor(), BlackAndWhiteFilter())
    image_storage.store('image.jpg')

    # You can also make compressor and filter as param of .store method
    # So that you have use the same image_storage object with different compressor and filter