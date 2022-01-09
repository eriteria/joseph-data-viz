import statistics, math
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


def bar_plots(df1):
    for i in range(2010, 2020, 1):
        df_plot = df1[(df1["TimeDim"] == i)]
        df_plot = df_plot.plot(x="Country", y="NumericValue", figsize=(20, 10), style=['o', 'rx'], kind='bar',
                               title=f"HIV/AIDS data for African Countries in the year {i}",
                               ylabel="No. Of Cases")
        
        df_plot.figure.savefig(f'./static/images/hbars3_{i}.png')

def dispersion_plots(df):
    plt.figure(figsize=(10,10))

    def interquartile_range(sample):
        q3, q1 = np.percentile(sample, [75 ,25])
        return q3 - q1

    def quartile_range(sample):
        q3, q1 = np.percentile(sample, [75 ,25])
        return (q3 - q1)/2

    def _range(sample):
        return sample.max() - sample.min()

    def create_plot(fn, label):
        ls = []
        for year in range(2010,2020):
            ls.append(fn(df[df['TimeDim'] == year]['NumericValue']))
                
        plt.plot(range(2000,2015), ls, label=label)
        plt.title('Measures of Dispersion of African Countries against Year.')
        plt.ylabel('Observation Value')
        plt.xlabel('Year')


        if label == 'Range':
            plt.savefig('./static/images/dispersion_plots.png')
        
    create_plot(statistics.mean, 'Mean')
    create_plot(statistics.variance, 'Variance')
    create_plot(statistics.stdev, 'Standard Deviation')
    create_plot(interquartile_range, 'Interquartile Range')
    create_plot(quartile_range, 'Quartile Range')
    create_plot(_range, 'Range')

    plt.legend(loc='best')

def box_plots(df):
    fig, axes  = plt.subplots(1,15, figsize=(10,10), sharey=True)
    fig.suptitle('Boxplots from 2000 to 2014')
    axes[0].set_ylabel('Observation Value')

    for idx, year in enumerate(range(2010,2020)):
        sns.boxplot(ax = axes[idx], y = df[df['TimeValue'] == year]['NumericValue'])
        axes[idx].set_title(year)
        if idx > 0: axes[idx].set_ylabel('')

    fig.savefig('./static/images/boxplots.png')