import numpy
from sklearn.decomposition import PCA
import plotly.express as px

# Do we need a class for only class methods ? file will be enough. One line command <=> no class definition ?
class PrincipalComponentAnalysis:
    @classmethod
    def compute_basis(cls, data):
        pca = PCA()
        return pca.fit(data).components_

    @classmethod
    def report(cls, data):
        data = numpy.array(data)
        fig = px.scatter(x=data[:,0], y=data[:,1])
        fig.show()