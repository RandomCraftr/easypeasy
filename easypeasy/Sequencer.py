import datetime
import getpass
import hashlib
import os
import sys

import numpy
from sklearn.decomposition import PCA
import plotly.express as px
from jinja2 import Environment, PackageLoader
from codenamize import codenamize

from PIL import Image
import easypeasy.thirdparties.sequencer as sequencer
import tempfile


# Do we need a class for only class methods ? file will be enough. One line command <=> no class definition ?
# TODO refactor analysis to enable building block reporting
class Sequencer:
    analysis_name = "Sequencer"

    @classmethod
    def report(cls, data):
        # Take data and prepare BEFORE plot
        data = numpy.array(data)
        fig = px.imshow(data, color_continuous_scale="gray")
        fig_before_html = fig.to_html(full_html=False, include_plotlyjs=False)
        # Sequence data and prepare plot
        grid = numpy.arange(data.shape[1])
        # Define the list of distance metrics to consider.
        estimator_list = ['EMD', 'energy', 'L2']
        # Define Sequencer object
        seq = sequencer.Sequencer(grid, data, estimator_list)
        # Define output dir as tempdir
        output_path = tempfile.gettempdir()
        final_elongation, final_sequence = seq.execute(output_path,
                                                       to_average_N_best_estimators=True,
                                                       number_of_best_estimators=3)
        # Prepare AFTER PLOT
        fig = px.imshow(data[final_sequence, :], color_continuous_scale="gray")
        fig_after_html = fig.to_html(full_html=False, include_plotlyjs=False)
        # Fill out template
        env = Environment(
            loader=PackageLoader("easypeasy"),
        )
        template = env.get_template("Sequencer.html")
        report_string = template.render(fig_before_html=fig_before_html,
                                        fig_after_html=fig_after_html)
        os.makedirs("out", exist_ok=True)
        report = open("out/report.html", "w")
        report.write(report_string)
        report.close()
