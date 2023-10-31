#!/usr/bin/env python3
import ipdb

from classes.many_to_many import NationalPark
from classes.many_to_many import Visitor
from classes.many_to_many import Trip

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    v1 = Visitor('kass')
    v2 = Visitor('shi')

    n1 = NationalPark('Zion National Park')
    n2 = NationalPark('Bryce National Park')

    t1 = Trip(v1,n1,"Semptember 1st","September 4th" )
    t2 = Trip(v1,n2,"Semptember 1st","September 4th" )
    t4 = Trip(v1,n1,"July 1st","July 4th" )

    t3 = Trip(v2,n1,"Semptember 1st","September 4th" )


    ipdb.set_trace()
