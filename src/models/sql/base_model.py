"""
This class is a base for creating tables models in the future.
Thanks to this class, all subclasses will be mapped automatically to the tables (thanks to heritage)
"""

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()