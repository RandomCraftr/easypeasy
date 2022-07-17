import numpy
import easypeasy.thirdparties.sequencer as sequencer


def test_sequencer():
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

    # define the sequencer object with default parameters
    #scale_list = numpy.array([[1], [1], [1]], dtype=numpy.int64)
    #print(scale_list is not None)
    #for scale_value in numpy.array(scale_list).flatten():
    #    print(type(scale_value))
    # Define Sequencer object
    seq = sequencer.Sequencer(grid, objects_list_shuffled, estimator_list)
    # To execute the sequencer, we first need to define the output directory to which the different outputs will be saved
    output_path = "."
    final_elongation, final_sequence = seq.execute(output_path)
    print(final_elongation)
    print(final_sequence)