import numpy
import easypeasy


def test_compute_basis():
    print(dir(easypeasy.PrincipalComponentAnalysis))
    # Generate canonical vectors to test PCA
    data = numpy.array([[0, 0, 0], [1, 0, 0]])
    # Call PCA
    transformed_data = easypeasy.PrincipalComponentAnalysis.compute_basis(data)
    print(data)
    print(transformed_data)


def test_report():
    data = numpy.random.randn(1000, 2)
    data[:, 1] = data[:, 0]*2+2+0.4*data[:, 1]
    easypeasy.PrincipalComponentAnalysis.report(data)
