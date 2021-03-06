#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy


class Prototype:
    value = 'default'

    def clone(self, **attrs):
        """Clone a prototype and update inner attributes dictionary"""
        obj = copy.deepcopy(self)
        obj.__dict__.update(attrs)
        return obj


class PrototypeDispatcher:

    def __init__(self):
        self._objects = {}

    def get_objects(self):
        """Get all objects"""
        return self._objects

    def register_object(self, name, obj):
        """Register an object"""
        self._objects[name] = obj

    def unregister_object(self, name):
        """Unregister an object"""
        del self._objects[name]


def main():

    dispatcher = PrototypeDispatcher()
    prototype = Prototype()

    d = prototype.clone()
    a = prototype.clone(value='a-value', category='a')
    b = prototype.clone(value='b-value', is_checked=True)

    dispatcher.register_object('objecta', a)
    dispatcher.register_object('objectb', b)
    dispatcher.register_object('default', d)
    # 遍历dispatcher 的所有键值对, 值为一个实例化对象, 打印其value 实例属性
    print([{n: p.value} for n, p in dispatcher.get_objects().items()])


if __name__ == '__main__':
    main()

### OUTPUT ###
# [{'objectb': 'b-value'}, {'default': 'default'}, {'objecta': 'a-value'}]
#
# Q&A
# 1. 为何最后生成的dispatcher 没有category 等等键
# 答:
