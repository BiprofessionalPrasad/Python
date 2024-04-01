# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 08:58:44 2024

@author: 9387758
"""

# Import seaborn
import seaborn as sns
import pandas as pd

# Apply the default theme
sns.set_theme()

# Load an example dataset
tips = sns.load_dataset("tips")

# Create a visualization
sns.relplot(
    data=tips,
    x="total_bill", y="tip", col="time",
    hue="smoker", style="smoker", size="size",
)
#---------------------------------------------------------------------------------------
dots = sns.load_dataset("dots")
sns.relplot(
    data=dots, kind="line",
    x="time", y="firing_rate", col="align",
    hue="choice", size="coherence", style="choice",
    #facet_kws=dict(sharex=False),
)
#---------------------------------------------------------------------------------------
fmri = sns.load_dataset("fmri")
sns.relplot(
    data=fmri, kind="line",
    x="timepoint", y="signal", col="region",
    hue="event", style="event",
)
#----------------------------------------------------------------------
# average value of one variable as a function of other variables. 
sns.lmplot(data=tips, x="total_bill", y="tip", 
           col="time", hue="smoker")
#----------------------------------------------------------------------
#Distributional representations
sns.displot(data=tips, x="total_bill", color='magenta',
            col="time", kind="hist",kde=True)

sns.displot(data=tips, kind="ecdf", 
            x="total_bill", col="time", 
            hue="smoker", rug=True)
#----------------------------------------------------------------------
# categorical data
sns.catplot(data=tips, 
            kind="swarm", 
            x="day", y="total_bill", hue="smoker")

sns.catplot(data=tips, 
            kind="boxen", 
            x="day", y="total_bill", hue="smoker")

sns.catplot(data=tips, 
            kind="violin", 
            x="day", y="total_bill", 
            hue="smoker", split=True)

sns.catplot(data=tips, kind="bar", x="day", y="total_bill", hue="smoker")
#----------------------------------------------------------------------
# Multivariate views on complex datasets

penguins = sns.load_dataset("penguins")

sns.jointplot(data=penguins, 
              x="flipper_length_mm", y="bill_length_mm", 
              hue="species")

sns.pairplot(data=penguins, hue="species")
#----------------------------------------------------------------------

g = sns.PairGrid(penguins, hue="species", corner=True)
g.map_lower(sns.kdeplot, hue=None, levels=5, color=".2")
g.map_lower(sns.scatterplot, marker="+")
g.map_diag(sns.histplot, element="step", linewidth=0, kde=True)
g.add_legend(frameon=True)
g.legend.set_bbox_to_anchor((.61, .6))

#----------------------------------------------------------------------
sns.relplot(
    data=penguins,
    x="bill_length_mm", y="bill_depth_mm", hue="body_mass_g"
)
#---------------------------------------------------------------------
sns.set_theme(style="ticks", font_scale=1.25)
g = sns.relplot(
    data=penguins,
    x="bill_length_mm", y="bill_depth_mm", hue="body_mass_g",
    palette="crest", marker="x", s=100,
)
g.set_axis_labels("Bill length (mm)", "Bill depth (mm)", labelpad=10)
g.legend.set_title("Body mass (g)")
g.figure.set_size_inches(6.5, 4.5)
g.ax.margins(.15)
g.despine(trim=True)
#-------------------------------------------------------------------
titanic=pd.read_csv(r'C:\Users\9387758\OneDrive - MyFedEx\Documents\Python\titanic.csv')
sns.boxplot(x=titanic["age"])
titanic["age"].median()

titanic["age"].min()

titanic["age"].max()

titanic.age.quantile([0.25,0.5,0.75])
