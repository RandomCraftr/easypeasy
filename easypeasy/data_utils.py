import numpy
import tempfile
import easypeasy.thirdparties.sequencer as sequencer
from sklearn.decomposition import PCA

def sequence(data):
    """
    easy peasy wrapper of sequencer work from https://github.com/dalya/Sequencer
    """
    # Define default grid
    grid = numpy.arange(data.shape[1])
    # Define the list of distance metrics to consider.
    estimator_list = ['EMD', 'energy', 'L2']
    # Define Sequencer object
    seq = sequencer.Sequencer(grid, data, estimator_list)
    # Define output dir as tempdir
    output_path = tempfile.gettempdir()
    final_elongation, final_sequence = seq.execute(output_path)
    return final_sequence

#Row wise
def compute_pca_basis(data):
    pca = PCA()
    return pca.fit(data).components_

