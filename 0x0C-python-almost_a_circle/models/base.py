#!/usr/bin/python3
import json
import csv

"""
This module defines first class base

"""

class Base:
    """
    This defines Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        This is a class constructor
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            """ __nb_objects is private class attribute and cannot be accessed directly without referencing class name"""
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Converts list of dictionaries to json string repr.
        
        Args:
            list_dictionaries (list): A list of dictionaries
            
        Returns:
            str: The JSON string repr of list_dictionaries
            
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)  
        
    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes json string repr of list_obj to a file.
        
        Args:
            list_objs (list): A list of instances.
            
        Returns:
            None.

        """
        flname = cls.__name__ + ".json"
        jstr = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
        with open(flname, "w") as fl:
            fl.write(jstr)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns list repr by json string repr.

        Args:
            json_string (str): A string repr a list of dictionaries.

        Returns:
            List: The list repr by json_string.

        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create instance of class with attr set using gvn dict.

        Args:
            **dict: a dict containing attr names and their corresponding values.

        Returns:
            An instance of class with attr set according to dictionary.

        Example:

        dummy_inst = cls
        dummy_inst.update(width=0, height=0, size=0, x=0, y=0)
        dummy_inst.update(**dictionary)
        return dummy_inst 
        """

        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)

        dummy.update(**dictionary)

        return dummy

    @classmethod
    def load_from_file(cls):
        """
        loads inst from file.

        Returns:
            list: a list of inst loaded from file.
        """

        flname = cls.__name__ + ".json"
        try:
            with open(flname, "r") as fl:
                jdata = fl.read()
                dt = cls.from_json_string(jdata)
                inst = [cls.create(**item) for item in dt]
                return inst
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        serialises list of inst to CSV file.

        Args:
            list_objs (list): list of instances.

        """
        fln = cls.__name__ + ".csv"
        with open(fln, "w", newline="") as fl:
            writer = csv.writer(fl)
            if cls.__name__ == "Rectangle":
                fdn = ["id", "width", "height" "x", "y"]
            elif cls.__name__ == "Square":
                fdn = ["id", "size", "x", "y"]
            writer.writerow(fdn)
            for obj in list_objs:
                writer.writerow(obj.to_csv_row())

    @classmethod
    def load_from_file_csv(cls):   
        """
        deserialises inst from CSV file.

        Args:
            list: list of instances.

        """
        fln = cls.__name__ + ".csv"
        try:
            with open(fln, "r", newline="") as fl:
                reader = csv.DictReader(fl)
                insts = []
                for row in reader:
                    row = {str(key): value for key, value in row.items()}
                    inst = cls.create(**row)
                    insts.append(inst)
                return insts
        except FileNotFoundError:
            return []
    
    @classmethod
    def to_csv_row(self):
        """
        converts instance into csv row.

        Returns:
            list: list repr the instance attributes

        """
        raise NotImplementedError("to_csv_row method must be implemented in\
                the derived class")
