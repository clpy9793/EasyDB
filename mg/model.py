#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-31 17:33:10
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
import pymongo


class MongoHelper(object):
    pass

    def __init__(self, host='localhost', port=6379):
        client = pymongo.MongoClient(host, port)
        self._client = client
        self._db = None

    def use_db(self, db_name):
        self._db = self._client[db_name]

    def use_cl(self, cl):
        """
        :param cl_name: cellection name
        :return:
        """
        self._cl = self.self._db[cl]

    def insert_one(self, data, *args, db=None, cl=None, **kwargs):
        if len(args) != 0:
            raise ValueError('param error.')
        if db:
            self.use_db(db)
        if cl:
            self.use_cl(cl)
        return self._cl.insert_one(data, **kwargs)

    def insert_many(self, data, *args, db=None, cl=None, **kwargs):
        if len(args) != 0:
            raise ValueError('param error.')
        if db:
            self.use_db(db)
        if cl:
            self.use_cl(cl)
        if not isinstance(data, (list, tuple)):
            raise ValueError('param must be list or tuple')
        return self._cl.insert_many(data, **kwargs)

    def find_one(self, cl, *args, db=None, **kwargs):
        if len(args) != 0:
            raise ValueError('param error.')
        if db:
            self.use_db(db)
        if not cl:
            raise ValueError('param error...')
        self.use_cl(cl)
        self._cl.find_one(**kwargs)


if __name__ == '__main__':
    pass
