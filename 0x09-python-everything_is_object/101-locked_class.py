#!/usr/bin/python3
"""A class with a fixed number of slots"""

class LockedClass:
"""Prevents the addition of new attributes if user-defined"""
slots = ['first_name']
