# -*- coding: utf-8 -*-
__author__ = 'forest'

import random


class Perceptron:

    def _init_weight(self):
        """
        초기 웨이트값 랜덤으로 초기화
        :return:
        """
        print "key: %d" % len(self.train_set.keys()[0])

        for n in xrange(0, len(self.train_set.keys()[0])):
            self.weight.append(random.random())
            temp = random.randrange(0, 2)

            if temp is 0:
                self.weight[n] = -self.weight[n]

        print "init weight: %s" % str(tuple(self.weight))

    def _inner_product(self, inp):
        return sum([i*w for i, w in zip(inp, self.weight)])

    def _active_function(self, result):
        if result >= 0:
            return 1
        else:
            return -1

    def training(self):
        inputs = self.train_set.keys()
        test_count = 0
        break_count = 0

        # 트레이닝 시작
        while True:

            # print "-----------------------------------------------"
            # print "test count: %d" % test_count
            test_count += 1
            err_count = 0
            no_err = True

            for inp in inputs:
                # 내적 후 활성함수
                result = self._active_function(self._inner_product(inp))

                if self.train_set.get(inp) is not result:
                    err_count += 1
                    no_err = False

                    # 결과가 다를 경우 웨이트 업데이트
                    for n in xrange(0, len(self.weight)):
                        self.weight[n] += self.l_rate * (self.train_set.get(inp) - result) * inp[n]

            # print 'error count: %d' % err_count

            break_count += 1

            if err_count < self.min_err:
                print "find min"
                self.min_err = err_count
                self.min_weight = self.weight
                break_count = 0

            elif break_count > 10000:
                break

            if no_err:
                break

        self.weight = self.min_weight
        print "-----------------------------------------------"
        print "train input: %d" % len(inputs)
        print "min err: %d" % self.min_err
        print "err rate: %f" % (self.min_err/float(len(inputs)))
        print "min weight: %s" % self.min_weight.__str__()

    def testing(self):
        inputs = self.test_set.keys()
        err_count = 0

        print "-----------------------------------------------"
        print "test input: %d" % len(inputs)

        for inp in inputs:
            # 내적 후 활성함수
            result = self._active_function(self._inner_product(inp))

            if self.test_set.get(inp) is not result:
                err_count += 1

        print "correct answer: %d" % (len(inputs)-err_count)
        print "wrong answer: %d" % err_count
        print "err rate: %f" % (err_count/float(len(inputs)))

    def _input_read(self):
        workclass = {
            'Private': 1, 'Self-emp-not-inc':2, 'Self-emp-inc':3, 'Federal-gov':4, 'Local-gov':5, 'State-gov':6,
            'Without-pay':7, 'Never-worked':8
        }

        education = {
            'Bachelors':1, 'Some-college':2, '11th':3, 'HS-grad':4, 'Prof-school':5, 'Assoc-acdm':6, 'Assoc-voc':7,
            '9th':8, '7th-8th':9, '12th':10, 'Masters':11, '1st-4th':12, '10th':13, 'Doctorate':14, '5th-6th':15, 'Preschool':16
        }

        marital_status = {
            'Married-civ-spouse':1, 'Divorced':2, 'Never-married':3, 'Separated':4, 'Widowed':5,
            'Married-spouse-absent':6, 'Married-AF-spouse':7
        }

        occupation = {
            'Tech-support':1, 'Craft-repair':2, 'Other-service':3, 'Sales':4, 'Exec-managerial':5, 'Prof-specialty':6,
            'Handlers-cleaners':7, 'Machine-op-inspct':8, 'Adm-clerical':9, 'Farming-fishing':10, 'Transport-moving':11,
            'Priv-house-serv':12, 'Protective-serv':13, 'Armed-Forces':14
        }

        relationship = {
            'Wife':1, 'Own-child':2, 'Husband':3, 'Not-in-family':4, 'Other-relative':5, 'Unmarried':6
        }

        race = {
            'White':1, 'Asian-Pac-Islander':2, 'Amer-Indian-Eskimo':3, 'Other':4, 'Black':5
        }

        sex = {
            'Female':1, 'Male':2
        }

        native_country = {
            'United-States':1, 'Cambodia':2, 'England':3, 'Puerto-Rico':4, 'Canada':5, 'Germany':6, 'Outlying-US(Guam-USVI-etc)':7,
            'India':8, 'Japan':9, 'Greece':10, 'South':11, 'China':12, 'Cuba':13,
            'Iran':14, 'Honduras':15, 'Philippines':16, 'Italy':17, 'Poland':18, 'Jamaica':19, 'Vietnam':20,
            'Mexico':21, 'Portugal':22, 'Ireland':23, 'France':24, 'Dominican-Republic':25, 'Laos':26, 'Ecuador':27, 'Taiwan':28,
            'Haiti':29, 'Columbia':30, 'Hungary':31, 'Guatemala':32, 'Nicaragua':33, 'Scotland':34, 'Thailand':35, 'Yugoslavia':36, 'El-Salvador':37,
            'Trinadad&Tobago':38, 'Peru':39, 'Hong':40, 'Holand-Netherlands':41
        }

        answer = {
            '>50K': 1,
            '<=50K': -1
        }

        f = open('adult.inp')
        data = f.readlines()
        self.min_err = len(data)
        test = int(len(data) * (30/100.0))
        print "test: %d" % test

        test_count = 0

        for line in data:
            line = line.replace(' ', '')
            line = line.replace('\n', '')
            temp_list = line.split(',')
            vector = [1]
            n = 0

            # 입력파일 인풋 벡터로 변환
            for temp in temp_list:

                if temp != '?':
                    if n is 0 and n in self.features:
                        vector.append(int(temp))
                    elif n is 1 and n in self.features:
                        vector.append(workclass[temp])
                    elif n is 2 and n in self.features:
                        vector.append(int(temp))
                    elif n is 3 and n in self.features:
                        vector.append(education[temp])
                    elif n is 4 and n in self.features:
                        vector.append(int(temp))
                    elif n is 5 and n in self.features:
                        vector.append(marital_status[temp])
                    elif n is 6 and n in self.features:
                        vector.append(occupation[temp])
                    elif n is 7 and n in self.features:
                        vector.append(relationship[temp])
                    elif n is 8 and n in self.features:
                        vector.append(race[temp])
                    elif n is 9 and n in self.features:
                        vector.append(sex[temp])
                    elif n is 10 and n in self.features:
                        vector.append(int(temp))
                    elif n is 11 and n in self.features:
                        vector.append(int(temp))
                    elif n is 12 and n in self.features:
                        vector.append(int(temp))
                    elif n is 13 and n in self.features:
                        vector.append(native_country[temp])
                    elif n is 14:
                        vector.append(answer[temp])
                else:
                    if n in self.features:
                        vector.append(0)

                n += 1

            if test > test_count:
                self.test_set[tuple(vector[:-1])] = vector[-1]
            else:
                self.train_set[tuple(vector[:-1])] = vector[-1]

            test_count += 1

    def __init__(self, features, learning_rate=0.5):
        self.min_err = 0
        self.min_weight = []
        self.weight = []
        self.train_set = {}
        self.test_set = {}
        self.features = features
        self._input_read()
        self._init_weight()
        self.l_rate = learning_rate

        print "learning rate: %f" % self.l_rate

if __name__ == "__main__":
    p = Perceptron((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13), 1)
    p.training()
    p.testing()
