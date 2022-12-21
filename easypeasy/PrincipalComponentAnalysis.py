import numpy
from sklearn.decomposition import PCA
import plotly.express as px
from jinja2 import Environment, PackageLoader, select_autoescape


# Do we need a class for only class methods ? file will be enough. One line command <=> no class definition ?
class PrincipalComponentAnalysis:
    @classmethod
    def compute_basis(cls, data):
        pca = PCA()
        return pca.fit(data).components_

    @classmethod
    def report(cls, data):
        # Generate figures
        data = numpy.array(data)
        fig = px.scatter(x=data[:, 0], y=data[:, 1])
        fig_html = fig.to_html(full_html = False, include_plotlyjs = False)
        # Fill out template
        env = Environment(
            loader=PackageLoader("easypeasy"),
        )
        template = env.get_template("PrincipalComponentAnalysis.html")
        report_string = template.render(figure = fig_html)
        report = open("out/report.html","w")
        report.write(report_string)
        report.close()