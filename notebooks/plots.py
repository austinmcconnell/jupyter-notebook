import seaborn as sns

CATPLOT_KINDS = {'strip', 'swarm', 'box', 'violin', 'boxen', 'point', 'bar', 'count'}

def get_title_str(text, x, y):
    if text:
        title_str = text
    else:
        title_str = ''
        if y:
            title_str += f'{y.title().replace("_", " ")}'
        if x:
            title_str += f' vs {x.title().replace("_", " ")}'
    return title_str

def add_labels(g):
    # iterate through axes
    for ax in g.axes.ravel():

        # add annotations
        for c in ax.containers:
            labels = [f'{(v.get_height()):.0f}' for v in c]
            ax.bar_label(c, labels=labels, label_type='edge')

        ax.margins(y=0.2)

def generate_catplot(data, title: str=None, label_values=False, **kwargs):

    kind = kwargs.pop('kind', 'strip')
    if kind and kind not in CATPLOT_KINDS:
        raise Exception(f'Kind param must be one of: {CATPLOT_KINDS}')

    estimator = kwargs.pop('estimator', 'mean')
    x = kwargs.pop('x', None)
    y = kwargs.pop('y', None)

    g = sns.catplot(data=data, x=x, y=y, estimator=estimator, kind=kind, height=5, aspect=2, legend_out=False, errorbar=None, **kwargs)
    g.fig.subplots_adjust(top=0.9)
    g.fig.suptitle(get_title_str(text=title, x=x, y=y), fontsize=30)

    if label_values:
        add_labels(g)

    return g
