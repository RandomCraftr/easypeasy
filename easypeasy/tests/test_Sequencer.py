import numpy
import easypeasy
from PIL import Image
from numpy import asarray

def test_report():
    # Prepare data
    #image = Image.open('templates/media/kool - blinking.jpg').convert("L") # Load image, convert to greyscale
    image = Image.open('tests/bear.jpg').convert("L")  # Load image, convert to greyscale
    data = numpy.array(asarray(image)) # Convert to numpy array
    numpy.random.shuffle(data) # Shuffle all lines
    # Do the magic !
    easypeasy.Sequencer.report(data)
