import numpy
from sklearn.decomposition import PCA
import plotly.express as px
from jinja2 import Environment, PackageLoader, select_autoescape

from PIL import Image


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
        fig = px.scatter(x=data[:, 0], y=data[:, 1],
                         title="Data distribution",
                         labels={'x':"Dimension 1", 'y':"Dimension 2"},
                         )
        # Customize appearance: fonte, layout, logo
        PrincipalComponentAnalysis.customize_plot(fig)
        # Customize various option before export: toolbar, scroll zoom
        config = dict({'scrollZoom': True,
                       'displaylogo': False,
                       # List of buttons at: https://plotly.com/javascript/configuration-options/#remove-modebar-buttons
                       "modeBarButtonsToRemove" : ("select2d", "lasso2d","resetScale2d")})
        # Export figure to embed in HTML template
        fig_html = fig.to_html(full_html = False, include_plotlyjs = False, config = config)
        # Fill out template
        env = Environment(
            loader=PackageLoader("easypeasy"),
        )
        template = env.get_template("PrincipalComponentAnalysis.html")
        report_string = template.render(figure = fig_html)
        report = open("out/report.html","w")
        report.write(report_string)
        report.close()

    @classmethod
    def customize_plot(self, fig):
        # Add plotly template
        fig.update_layout(template = "none")
        # Add easypeasy logo
        easypeasy_logo = Image.open('./easypeasy/templates/media/logo_RGB_47_153_89.png')
        fig.update_layout(images=[dict(
                              source=easypeasy_logo,
                              xref="paper", yref="paper",
                              x=1, y=0  ,
                              sizex=0.1, sizey=0.1,
                              xanchor="right", yanchor="bottom")])
        # Format title and center
        fig.update_layout(title={'text': "<b>"+fig.layout.title.text+"</b>",'x': 0.5,'xanchor': 'center'})
        fig.update_layout(title={'text': "<b>" + fig.layout.title.text + "</b>", 'x': 0.5, 'xanchor': 'center'})
        # Format axis labels
        fig.update_layout(xaxis_title="<i>"+fig.layout.xaxis.title.text+"</i>")
        fig.update_layout(yaxis_title="<i>" + fig.layout.yaxis.title.text + "</i>")
        # Dragmode is pan by default (instead of zoom)
        fig.update_layout(dragmode="pan")
        # Figure size
        fig.update_layout(
            width=800,
            height=600)
