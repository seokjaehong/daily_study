def main():
    ### Edit Here ###
    # % matplotlib    inline
    import matplotlib.pyplot as plt
    import numpy as np

    import pandas as pd
    wine = pd.read_csv('wine-clustering.csv')
    wine.head()

    # clustering with KMeans algorithm
    features = ['Malic_Acid', 'Ash', 'Ash_Alcanity', 'Magnesium', 'Total_Phenols', 'Flavanoids', 'Nonflavanoid_Phenols',
                'Proanthocyanins', 'Color_Intensity', 'Hue', 'OD280', 'Proline']
    from sklearn.preprocessing import StandardScaler
    x = wine.loc[:, features].values
    y = wine.loc[:, ['Alcohol']].values
    x = StandardScaler().fit_transform(x)
    from sklearn.cluster import KMeans
    model = KMeans(n_clusters=3, random_state=10)
    model.fit(x)
    wine['cluster'] = model.fit_predict(y)
    # feature dimension reduction with PCA
    from sklearn.decomposition import PCA
    pca = PCA(n_components=2)
    principalComponents = pca.fit_transform(wine)
    principalDf = pd.DataFrame(data=principalComponents
                               , columns=['principal component 1', 'principal component 2'])
    finalDf = pd.concat([principalDf, wine[['Alcohol']]], axis=1)

    # visualization

    import matplotlib.pyplot as plt
    plot = plt.scatter(finalDf[['principal component 1']], finalDf[['principal component 2']], c=finalDf['Alcohol'])
    plt.legend(handles=plot.legend_elements()[0], labels=list(finalDf['Alcohol']))
    plt.show()

    #################


if __name__ == "__main__":
    main()
