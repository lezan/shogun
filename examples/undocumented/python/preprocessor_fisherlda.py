#!/usr/bin/env python
from tools.load import LoadMatrix
from shogun import *


lm=LoadMatrix()
data = lm.load_numbers('../data/fm_train_real.dat')
labels = lm.load_numbers('../data/label_train_multiclass.dat')

parameter_list = [[data, labels, CANVAR_FLDA], [data, labels, CLASSIC_FLDA]]
def preprocessor_fisherlda (data, labels, method):

	from shogun import RealFeatures, MulticlassLabels, CANVAR_FLDA
	from shogun import FisherLda
	from shogun import MulticlassLabels

	sg_features = RealFeatures(data)
	sg_labels = MulticlassLabels(labels)

	preprocessor=FisherLda(method)
	preprocessor.fit(sg_features, sg_labels, 1)
	yn=preprocessor.apply_to_feature_matrix(sg_features)

	return yn


if __name__=='__main__':
	print('FisherLda')
	preprocessor_fisherlda(*parameter_list[0])

