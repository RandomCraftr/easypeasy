from sklearn.decomposition import PCA

class PrincipalComponentAnalysis:
    @classmethod
    def compute_basis(cls, data):
        pca = PCA()
        return pca.fit(data).components_

    @classmethod
    def report(cls, data):
        #Compute PCA
        #Compute checks
        #Fill out template and export report
        pass