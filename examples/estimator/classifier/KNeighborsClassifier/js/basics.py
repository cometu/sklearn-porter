# -*- coding: utf-8 -*-

from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
from sklearn_porter import Porter


iris_data = load_iris()
X = iris_data.data
y = iris_data.target

clf = KNeighborsClassifier(algorithm='brute',
                           n_neighbors=3,
                           weights='uniform')
clf.fit(X, y)

porter = Porter(clf, language='js')
output = porter.export()
print(output)

"""
var KNeighborsClassifier = function(nNeighbors, nClasses, power, X, y) {

    this.nNeighbors = nNeighbors;
    this.nTemplates = y.length;
    this.nClasses = nClasses;
    this.power = power;
    this.X = X;
    this.y = y;

    var Neighbor = function(clazz, dist) {
        this.clazz = clazz;
        this.dist = dist;
    };

    var compute = function(temp, cand, q) {
        var dist = 0.,
            diff;
        for (var i = 0, l = temp.length; i < l; i++) {
    	    diff = Math.abs(temp[i] - cand[i]);
    	    if (q==1) {
    	        dist += diff;
    	    } else if (q==2) {
    	        dist += diff*diff;
    	    } else if (q==Number.POSITIVE_INFINITY) {
    	        if (diff > dist) {
    	            dist = diff;
    	        }
    	    } else {
    	        dist += Math.pow(diff, q);
    		}
        }
        if (q==1 || q==Number.POSITIVE_INFINITY) {
            return dist;
        } else if (q==2) {
            return Math.sqrt(dist);
        } else {
            return Math.pow(dist, 1. / q);
        }
    };
    
    this.predict = function(features) {
        var classIdx = 0, i;
        if (this.nNeighbors == 1) {
            var minDist = Number.POSITIVE_INFINITY,
                curDist;
            for (i = 0; i < this.nTemplates; i++) {
                curDist = compute(this.X[i], features, this.power);
                if (curDist <= minDist) {
                    minDist = curDist;
                    classIdx = this.y[i];
                }
            }
        } else {
            var classes = new Array(this.nClasses).fill(0);
            var dists = [];
            for (i = 0; i < this.nTemplates; i++) {
                dists.push(new Neighbor(this.y[i], compute(this.X[i], features, this.power)));
            }
            dists.sort(function compare(n1, n2) {
                return (n1.dist < n2.dist) ? -1 : 1;
            });
            for (i = 0; i < this.nNeighbors; i++) {
                classes[dists[i].clazz]++;
            }
            for (i = 0; i < this.nClasses; i++) {
                classIdx = classes[i] > classes[classIdx] ? i : classIdx;
            }
        }
        return classIdx;
    };

};

if (typeof process !== 'undefined' && typeof process.argv !== 'undefined') {
    if (process.argv.length - 2 === 4) {

        // Features:
        var features = process.argv.slice(2);

        // Parameters:
        var X = [[5.0999999999999996, 3.5, 1.3999999999999999, 0.20000000000000001], [4.9000000000000004, 3.0, 1.3999999999999999, 0.20000000000000001], [4.7000000000000002, 3.2000000000000002, 1.3, 0.20000000000000001], [4.5999999999999996, 3.1000000000000001, 1.5, 0.20000000000000001], [5.0, 3.6000000000000001, 1.3999999999999999, 0.20000000000000001], [5.4000000000000004, 3.8999999999999999, 1.7, 0.40000000000000002], [4.5999999999999996, 3.3999999999999999, 1.3999999999999999, 0.29999999999999999], [5.0, 3.3999999999999999, 1.5, 0.20000000000000001], [4.4000000000000004, 2.8999999999999999, 1.3999999999999999, 0.20000000000000001], [4.9000000000000004, 3.1000000000000001, 1.5, 0.10000000000000001], [5.4000000000000004, 3.7000000000000002, 1.5, 0.20000000000000001], [4.7999999999999998, 3.3999999999999999, 1.6000000000000001, 0.20000000000000001], [4.7999999999999998, 3.0, 1.3999999999999999, 0.10000000000000001], [4.2999999999999998, 3.0, 1.1000000000000001, 0.10000000000000001], [5.7999999999999998, 4.0, 1.2, 0.20000000000000001], [5.7000000000000002, 4.4000000000000004, 1.5, 0.40000000000000002], [5.4000000000000004, 3.8999999999999999, 1.3, 0.40000000000000002], [5.0999999999999996, 3.5, 1.3999999999999999, 0.29999999999999999], [5.7000000000000002, 3.7999999999999998, 1.7, 0.29999999999999999], [5.0999999999999996, 3.7999999999999998, 1.5, 0.29999999999999999], [5.4000000000000004, 3.3999999999999999, 1.7, 0.20000000000000001], [5.0999999999999996, 3.7000000000000002, 1.5, 0.40000000000000002], [4.5999999999999996, 3.6000000000000001, 1.0, 0.20000000000000001], [5.0999999999999996, 3.2999999999999998, 1.7, 0.5], [4.7999999999999998, 3.3999999999999999, 1.8999999999999999, 0.20000000000000001], [5.0, 3.0, 1.6000000000000001, 0.20000000000000001], [5.0, 3.3999999999999999, 1.6000000000000001, 0.40000000000000002], [5.2000000000000002, 3.5, 1.5, 0.20000000000000001], [5.2000000000000002, 3.3999999999999999, 1.3999999999999999, 0.20000000000000001], [4.7000000000000002, 3.2000000000000002, 1.6000000000000001, 0.20000000000000001], [4.7999999999999998, 3.1000000000000001, 1.6000000000000001, 0.20000000000000001], [5.4000000000000004, 3.3999999999999999, 1.5, 0.40000000000000002], [5.2000000000000002, 4.0999999999999996, 1.5, 0.10000000000000001], [5.5, 4.2000000000000002, 1.3999999999999999, 0.20000000000000001], [4.9000000000000004, 3.1000000000000001, 1.5, 0.10000000000000001], [5.0, 3.2000000000000002, 1.2, 0.20000000000000001], [5.5, 3.5, 1.3, 0.20000000000000001], [4.9000000000000004, 3.1000000000000001, 1.5, 0.10000000000000001], [4.4000000000000004, 3.0, 1.3, 0.20000000000000001], [5.0999999999999996, 3.3999999999999999, 1.5, 0.20000000000000001], [5.0, 3.5, 1.3, 0.29999999999999999], [4.5, 2.2999999999999998, 1.3, 0.29999999999999999], [4.4000000000000004, 3.2000000000000002, 1.3, 0.20000000000000001], [5.0, 3.5, 1.6000000000000001, 0.59999999999999998], [5.0999999999999996, 3.7999999999999998, 1.8999999999999999, 0.40000000000000002], [4.7999999999999998, 3.0, 1.3999999999999999, 0.29999999999999999], [5.0999999999999996, 3.7999999999999998, 1.6000000000000001, 0.20000000000000001], [4.5999999999999996, 3.2000000000000002, 1.3999999999999999, 0.20000000000000001], [5.2999999999999998, 3.7000000000000002, 1.5, 0.20000000000000001], [5.0, 3.2999999999999998, 1.3999999999999999, 0.20000000000000001], [7.0, 3.2000000000000002, 4.7000000000000002, 1.3999999999999999], [6.4000000000000004, 3.2000000000000002, 4.5, 1.5], [6.9000000000000004, 3.1000000000000001, 4.9000000000000004, 1.5], [5.5, 2.2999999999999998, 4.0, 1.3], [6.5, 2.7999999999999998, 4.5999999999999996, 1.5], [5.7000000000000002, 2.7999999999999998, 4.5, 1.3], [6.2999999999999998, 3.2999999999999998, 4.7000000000000002, 1.6000000000000001], [4.9000000000000004, 2.3999999999999999, 3.2999999999999998, 1.0], [6.5999999999999996, 2.8999999999999999, 4.5999999999999996, 1.3], [5.2000000000000002, 2.7000000000000002, 3.8999999999999999, 1.3999999999999999], [5.0, 2.0, 3.5, 1.0], [5.9000000000000004, 3.0, 4.2000000000000002, 1.5], [6.0, 2.2000000000000002, 4.0, 1.0], [6.0999999999999996, 2.8999999999999999, 4.7000000000000002, 1.3999999999999999], [5.5999999999999996, 2.8999999999999999, 3.6000000000000001, 1.3], [6.7000000000000002, 3.1000000000000001, 4.4000000000000004, 1.3999999999999999], [5.5999999999999996, 3.0, 4.5, 1.5], [5.7999999999999998, 2.7000000000000002, 4.0999999999999996, 1.0], [6.2000000000000002, 2.2000000000000002, 4.5, 1.5], [5.5999999999999996, 2.5, 3.8999999999999999, 1.1000000000000001], [5.9000000000000004, 3.2000000000000002, 4.7999999999999998, 1.8], [6.0999999999999996, 2.7999999999999998, 4.0, 1.3], [6.2999999999999998, 2.5, 4.9000000000000004, 1.5], [6.0999999999999996, 2.7999999999999998, 4.7000000000000002, 1.2], [6.4000000000000004, 2.8999999999999999, 4.2999999999999998, 1.3], [6.5999999999999996, 3.0, 4.4000000000000004, 1.3999999999999999], [6.7999999999999998, 2.7999999999999998, 4.7999999999999998, 1.3999999999999999], [6.7000000000000002, 3.0, 5.0, 1.7], [6.0, 2.8999999999999999, 4.5, 1.5], [5.7000000000000002, 2.6000000000000001, 3.5, 1.0], [5.5, 2.3999999999999999, 3.7999999999999998, 1.1000000000000001], [5.5, 2.3999999999999999, 3.7000000000000002, 1.0], [5.7999999999999998, 2.7000000000000002, 3.8999999999999999, 1.2], [6.0, 2.7000000000000002, 5.0999999999999996, 1.6000000000000001], [5.4000000000000004, 3.0, 4.5, 1.5], [6.0, 3.3999999999999999, 4.5, 1.6000000000000001], [6.7000000000000002, 3.1000000000000001, 4.7000000000000002, 1.5], [6.2999999999999998, 2.2999999999999998, 4.4000000000000004, 1.3], [5.5999999999999996, 3.0, 4.0999999999999996, 1.3], [5.5, 2.5, 4.0, 1.3], [5.5, 2.6000000000000001, 4.4000000000000004, 1.2], [6.0999999999999996, 3.0, 4.5999999999999996, 1.3999999999999999], [5.7999999999999998, 2.6000000000000001, 4.0, 1.2], [5.0, 2.2999999999999998, 3.2999999999999998, 1.0], [5.5999999999999996, 2.7000000000000002, 4.2000000000000002, 1.3], [5.7000000000000002, 3.0, 4.2000000000000002, 1.2], [5.7000000000000002, 2.8999999999999999, 4.2000000000000002, 1.3], [6.2000000000000002, 2.8999999999999999, 4.2999999999999998, 1.3], [5.0999999999999996, 2.5, 3.0, 1.1000000000000001], [5.7000000000000002, 2.7999999999999998, 4.0999999999999996, 1.3], [6.2999999999999998, 3.2999999999999998, 6.0, 2.5], [5.7999999999999998, 2.7000000000000002, 5.0999999999999996, 1.8999999999999999], [7.0999999999999996, 3.0, 5.9000000000000004, 2.1000000000000001], [6.2999999999999998, 2.8999999999999999, 5.5999999999999996, 1.8], [6.5, 3.0, 5.7999999999999998, 2.2000000000000002], [7.5999999999999996, 3.0, 6.5999999999999996, 2.1000000000000001], [4.9000000000000004, 2.5, 4.5, 1.7], [7.2999999999999998, 2.8999999999999999, 6.2999999999999998, 1.8], [6.7000000000000002, 2.5, 5.7999999999999998, 1.8], [7.2000000000000002, 3.6000000000000001, 6.0999999999999996, 2.5], [6.5, 3.2000000000000002, 5.0999999999999996, 2.0], [6.4000000000000004, 2.7000000000000002, 5.2999999999999998, 1.8999999999999999], [6.7999999999999998, 3.0, 5.5, 2.1000000000000001], [5.7000000000000002, 2.5, 5.0, 2.0], [5.7999999999999998, 2.7999999999999998, 5.0999999999999996, 2.3999999999999999], [6.4000000000000004, 3.2000000000000002, 5.2999999999999998, 2.2999999999999998], [6.5, 3.0, 5.5, 1.8], [7.7000000000000002, 3.7999999999999998, 6.7000000000000002, 2.2000000000000002], [7.7000000000000002, 2.6000000000000001, 6.9000000000000004, 2.2999999999999998], [6.0, 2.2000000000000002, 5.0, 1.5], [6.9000000000000004, 3.2000000000000002, 5.7000000000000002, 2.2999999999999998], [5.5999999999999996, 2.7999999999999998, 4.9000000000000004, 2.0], [7.7000000000000002, 2.7999999999999998, 6.7000000000000002, 2.0], [6.2999999999999998, 2.7000000000000002, 4.9000000000000004, 1.8], [6.7000000000000002, 3.2999999999999998, 5.7000000000000002, 2.1000000000000001], [7.2000000000000002, 3.2000000000000002, 6.0, 1.8], [6.2000000000000002, 2.7999999999999998, 4.7999999999999998, 1.8], [6.0999999999999996, 3.0, 4.9000000000000004, 1.8], [6.4000000000000004, 2.7999999999999998, 5.5999999999999996, 2.1000000000000001], [7.2000000000000002, 3.0, 5.7999999999999998, 1.6000000000000001], [7.4000000000000004, 2.7999999999999998, 6.0999999999999996, 1.8999999999999999], [7.9000000000000004, 3.7999999999999998, 6.4000000000000004, 2.0], [6.4000000000000004, 2.7999999999999998, 5.5999999999999996, 2.2000000000000002], [6.2999999999999998, 2.7999999999999998, 5.0999999999999996, 1.5], [6.0999999999999996, 2.6000000000000001, 5.5999999999999996, 1.3999999999999999], [7.7000000000000002, 3.0, 6.0999999999999996, 2.2999999999999998], [6.2999999999999998, 3.3999999999999999, 5.5999999999999996, 2.3999999999999999], [6.4000000000000004, 3.1000000000000001, 5.5, 1.8], [6.0, 3.0, 4.7999999999999998, 1.8], [6.9000000000000004, 3.1000000000000001, 5.4000000000000004, 2.1000000000000001], [6.7000000000000002, 3.1000000000000001, 5.5999999999999996, 2.3999999999999999], [6.9000000000000004, 3.1000000000000001, 5.0999999999999996, 2.2999999999999998], [5.7999999999999998, 2.7000000000000002, 5.0999999999999996, 1.8999999999999999], [6.7999999999999998, 3.2000000000000002, 5.9000000000000004, 2.2999999999999998], [6.7000000000000002, 3.2999999999999998, 5.7000000000000002, 2.5], [6.7000000000000002, 3.0, 5.2000000000000002, 2.2999999999999998], [6.2999999999999998, 2.5, 5.0, 1.8999999999999999], [6.5, 3.0, 5.2000000000000002, 2.0], [6.2000000000000002, 3.3999999999999999, 5.4000000000000004, 2.2999999999999998], [5.9000000000000004, 3.0, 5.0999999999999996, 1.8]];
        var y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2];

        // Estimator:
        var clf = new KNeighborsClassifier(3, 3, 2, X, y);
        var prediction = clf.predict(features);
        console.log(prediction);

    }
}
"""
