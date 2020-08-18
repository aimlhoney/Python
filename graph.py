# Graph Plotting
from matplotlib import pyplot as plt
%matplotlib inline
import seaborn as sns

class Graph:
            
    def __init__(self,data):
        self.data = data

    def plotPairGraph(self, ax = None):
        sns.pairplot(self.data)

    def plotBarGraph(self,x,y,hue=None):
        sns.barplot(x=x, y=y, data=self.data, hue = hue)
            
    def plotPieChart(self,data):
        data.plot.pie()

    def plotCorelationMatrix(self):
        sns.heatmap(self.data.corr(), annot=True)
        
    def plotBoxplotGraph(self, x = None, y = None, hue = None, palette="Set3"):
        sns.boxplot(data=self.data, x=x, y=y, hue=hue, palette=palette)

    def plotJointMap(self, x = None, y = None, kind = None):
        sns.jointplot(data = self.data, x=x, y=y, kind = kind)
        
    def plotlmplotGraph(self,x=None,y=None,hue=None,palette=None):
        sns.lmplot(x=x, y=y, hue=hue, data=self.data,palette=palette)
        
    def plotViolinGraph(self,x=None,y=None,hue=None,palette=None,split=True):
        sns.violinplot(x, y, hue, self.data, palette, split)
        
    def plotSwarmPlotGraph(x=None, y=None, hue=None, data=None, order=None, hue_order=None, dodge=False, orient=None, color=None, palette=None, size=5, edgecolor='gray', linewidth=0, ax=None, **kwargs):
        sns.swarmplot(x,y,hue,self.data,order,hue_order,dodge,orient,color,palette,size,edgecolor,linewidth,ax, kwargs)

    def setSize(self,width,height):
        plt.figure(figsize=(width,height))
    
    def show(self):
        plt.show()
    
