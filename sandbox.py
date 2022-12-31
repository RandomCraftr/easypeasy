import numpy

import easypeasy

data = numpy.random.randn(1000,4)
data[:, 1] = data[:, 0] * 2 + 2 + 0.4 * data[:, 1]
data[:, 2] = -data[:, 1] * 2 + 2 + 0.4 * data[:, 2]

easypeasy.PrincipalComponentAnalysis.report(data)