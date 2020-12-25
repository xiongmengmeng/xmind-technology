#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""
    xmind
    ~~~~~

    :copyright:
    :license:

"""


__version__ = "0.1a.0"
__author__ = "aiqi@xmind.net <Woody Ai>"

from xmind.core.loader import WorkbookLoader
from xmind.core.saver import WorkbookSaver
from xmind.core.markerref import MarkerId


def load(path):
    """ Load XMind workbook from given path. If file no
    exist on given path then created new one.

    """
    loader = WorkbookLoader(path)
    return loader.get_workbook()


def save(workbook, path=None):
    """ Save workbook to given path. If path not given, then
    will save to path that set to workbook.

    """
    saver = WorkbookSaver(workbook)
    saver.save(path)


def build(content,r2):
    for key in content:
        t1 = r2.addSubTopic()
        list=key.split(":")
        t1.setTitle(list[0])
        if len(list)>1:
            t1.setPlainNotes(list[1]) 
        # print(content[key])
        for i in content[key]:
            # print(type(i))
            if(type(i).__name__=='dict'):
                for t in i:
                    t2 = t1.addSubTopic()
                    t2.setTitle(t)
                    for j in i[t]:
                        #print(j)
                        if(type(j).__name__=='dict'):
                            for h in j:
                                t3 = t2.addSubTopic()
                                t3.setTitle(h) 
                                for m in j[h]:
                                    if(type(m).__name__=='dict'):
                                        for n in m:
                                            t4 = t3.addSubTopic()
                                            t4.setTitle(n) 
                                            for l in m[n]:
                                                if(type(l).__name__=='dict'):
                                                    for k in l:
                                                        t5 = t4.addSubTopic()       
                                                        t5.setTitle(k)
                                                        for p in l[k]:
                                                            if(type(p).__name__=='dict'):
                                                                for u in p:
                                                                    t6 = t5.addSubTopic()
                                                                    t6.setTitle(u)
                                                                    for y in p[u]:
                                                                        if(type(y).__name__=='dict'):
                                                                            for a in y:
                                                                                t7 = t6.addSubTopic()
                                                                                t7.setTitle(a)
                                                                                for b in y[a]:
                                                                                    t8 = t7.addSubTopic()
                                                                                    t8.setTitle(b)
                                                                        else:
                                                                            t7 = t6.addSubTopic()
                                                                            t7.setTitle(y)              
                                                            else:
                                                                t6 = t5.addSubTopic()
                                                                t6.setTitle(p)                                                        
                                                else:
                                                    t5 = t4.addSubTopic()
                                                    t5.setTitle(l) 
                                    else:
                                        t4 = t3.addSubTopic()
                                        t4.setTitle(m) 
                        else:
                            t3 = t2.addSubTopic()
                            t3.setTitle(j) 
            else:
                t2 = t1.addSubTopic()
                t2.setTitle(i) 

    topics=r2.getSubTopics()
    for topic in topics:
        topic.addMarker(MarkerId.starBlue)


