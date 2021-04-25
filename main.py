from sklearn import tree

# //Apple: 0 and Orange: 1
features = [[140, 1], [130, 1], [150, 0], [170, 0]]
labels = [0,0,1,1]

# // Using Decision Modal tree
clf = tree.DecisionTreeClassifier()
# // categoring the content i.e feature and labels
clf = clf.fit(features,labels)