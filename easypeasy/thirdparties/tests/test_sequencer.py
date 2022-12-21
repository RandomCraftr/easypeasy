import numpy
import pandas
import tempfile
import easypeasy.thirdparties.sequencer as sequencer


def test_sequencer():
    """
    Test sequencer overall behaviour. Shuffle a sequence generated and check Sequencer finds out initial ordering.
    """
    # Create test data to sequence
    grid = numpy.arange(20)
    objects_list_simulated = []
    objects_true_indices = numpy.arange(20)  # the ordered indices
    for i in range(20):
        y = numpy.zeros(20)
        y[i] = 1
        objects_list_simulated.append(y)
    objects_list_simulated = numpy.array(objects_list_simulated)
    # Shuffle data to sequence
    numpy.random.shuffle(objects_true_indices)
    objects_list_shuffled = objects_list_simulated[objects_true_indices, :]
    # Define the list of distance metrics to consider.
    estimator_list = ['EMD', 'energy', 'L2']
    # Define Sequencer object
    seq = sequencer.Sequencer(grid, objects_list_shuffled, estimator_list)
    # Define output dir as tempdir
    output_path = tempfile.gettempdir()
    final_elongation, final_sequence = seq.execute(output_path)
    # Assert result against known reference: sequence can be original or reverse: both valid
    check_sequence = objects_true_indices[final_sequence]
    if check_sequence[0]<check_sequence[-1]:
        numpy.testing.assert_array_equal(numpy.arange(20), objects_true_indices[final_sequence])
    else:
        numpy.testing.assert_array_equal(numpy.arange(20), objects_true_indices[final_sequence[::-1]])
