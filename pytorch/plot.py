# coding: utf-8
from visdom import Visdom
import numpy as np


class VisdomLinePlotter(object):
    """Plots to Visdom"""
    def __init__(self, env_name='main'):
        self.viz = Visdom(server='http://localhost', port=10086)
        self.env = env_name
        self.plots = {}
        
    def plot(self, x_name, y_name, title_name, split_name, x, y):
        if title_name not in self.plots:
            self.plots[title_name] = self.viz.line(X=np.array([x,x]), Y=np.array([y,y]), env=self.env, opts=dict(
                legend=[split_name],
                title=title_name,
                xlabel=x_name,
                ylabel=y_name
            ))
        else:
            self.viz.line(X=np.array([x]), Y=np.array([y]), env=self.env, win=self.plots[title_name], name=split_name, update = 'append')

    def plot_bunch(self, x_name, y_name, title_name, split_names,  x, ys):
        assert len(split_names) == len(ys)
        for idx in range(len(split_names)):
            split_name = split_names[idx]
            y = ys[idx]
            self.plot(x_name, y_name, title_name, split_name, x, y)
