# -*- coding: utf-8 -*-
__author__ = 'forest'

import random


class Perceptron:

    def _init_weight(self):
        """
        초기 웨이트, b값 -1~1 사이로 랜덤값 생성
        :return:
        """
        self.weight = []

        for n in xrange(0, 3):
            self.weight.append(random.random())
            temp = random.randrange(0, 2)

            if temp is 0:
                self.weight[n] = -self.weight[n]

        print u"초기 weight: %f %f %f" % (tuple(self.weight))

    def _inner_product(self, inp):
        """
        인풋벡터, 웨이트벡터 내적
        :param inp: 인풋 벡터
        :return: 내적 결과값
        """
        return sum([i*w for i, w in zip(inp, self.weight)])

    def _active_function(self, result):
        """
        활성화 함수, 인풋<->웨이트 벡터 내적 결과 표준화
        :param result:
        :return:
        """
        if result >= 1:
            return 1
        else:
            return 0

    def train(self, input_name):
        """
        and, or 에 따라 테스트 셋 해당하는걸로 변경

        1. 입력*가중치 내적
        2. 내적 결과값 활성 함수로 정규화
        3. 활성 함수 결과값과 실제 정답과 비교후 다르면 가중치 변경
        :param input_name: and || or
        :return:
        """

        # and, or 선택
        if input_name is 'and':
            train_set = self.train_set_and
            print "Perceptron for and"
        else:
            train_set = self.train_set_or
            print "Perceptron for or"

        inputs = train_set.keys()
        test_count = 0

        # 트레이닝 시작
        while True:
            print "-----------------------------------------------"
            print "test count: %d" % test_count
            test_count += 1

            no_err = True
            for inp in inputs:
                print u"가중치: %f %f %f" % tuple(self.weight)

                # 내적 후 활성함수
                result = self._active_function(self._inner_product(inp))

                print u"입력: %d %d %d" % tuple(inp)
                print u"결과: %d" % result
                print u"실제정답: %d\n" % train_set.get(inp)

                if train_set.get(inp) is not result:
                    no_err = False

                    # 결과가 틀릴경우 웨이트 업데이트
                    for n in xrange(0, 3):
                        self.weight[n] += self.l_rate * (train_set.get(inp) - result) * inp[n]

            if no_err:
                break

    def __init__(self, learning_rate=0.5):
        self._init_weight()
        self.l_rate = learning_rate

        self.train_set_and = {      # and train set
            (1, 0, 0): 0,
            (1, 0, 1): 0,
            (1, 1, 0): 0,
            (1, 1, 1): 1,
        }

        self.train_set_or = {      # or train set
            (1, 0, 0): 0,
            (1, 0, 1): 1,
            (1, 1, 0): 1,
            (1, 1, 1): 1,
        }

        print u"러닝레이트: %f" % self.l_rate
        print u"==================================================="

p = Perceptron(0.1)
p.train('or')
p.train('and')