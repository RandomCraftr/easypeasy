import numpy
from easypeasy.data_utils import sequence, compute_pca_basis

def test_sequence():
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

    # easypeasy call
    final_sequence = sequence(objects_list_shuffled)

    check_sequence = objects_true_indices[final_sequence]
    if check_sequence[0] < check_sequence[-1]:
        numpy.testing.assert_array_equal(numpy.arange(20), objects_true_indices[final_sequence])
    else:
        numpy.testing.assert_array_equal(numpy.arange(20), objects_true_indices[final_sequence[::-1]])

# row wise
def test_compute_pca_basis():
    # Generate canonical vectors to test PCA
    data = numpy.array([[0,0,0],[1,0,0]])
    # Call PCA
    transformed_data = compute_pca_basis(data)
    print(data)
    print(transformed_data)