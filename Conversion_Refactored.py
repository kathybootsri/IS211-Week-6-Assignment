# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 09:35:53 2019

@author: kbootsri
"""
class Conversions():
    def __init__(self, fromUnit, toUnit, orig_value):
        self.fromUnit = fromUnit
        self.toUnit = toUnit
        self.orig_value = orig_value  
        
    def conversion(fromUnit, toUnit, orig_value):
        
        if fromUnit == 'celsius' and toUnit == 'kelvin':        
            kelvin = orig_value + 273.15
            return kelvin

        if fromUnit == 'celsius' and toUnit == 'farenheit':
            multipler = 9/5
            farenheit = (orig_value * multipler) + 32
            return farenheit
    
        if fromUnit == 'farenheit' and toUnit == 'celsius':  
            multipler = 5/9
            celsius = (orig_value - 32) * multipler
            return celsius

        if fromUnit == 'farenheit' and toUnit == 'kelvin':      
            multipler = 5/9
            kelvin = (orig_value + 459.67) * multipler
            return kelvin

        if fromUnit == 'kelvin' and toUnit == 'celsius':      
            celsius = orig_value - 273.15
            return celsius

        if fromUnit == 'kelvin' and toUnit == 'farenheit':      
            multipler = 9/5
            farenheit = (orig_value * multipler) - 459.67
            return farenheit
        
        if fromUnit == 'mile' and toUnit == 'yard':      
            yard = orig_value * 1760.0
            return yard

        if fromUnit == 'yard' and toUnit == 'mile':      
            mile = orig_value/1760.0
            return mile
        
        if fromUnit == 'yard' and toUnit == 'meter':      
            meter = orig_value/1.0936
            return meter
        
        if fromUnit == 'meter' and toUnit == 'yard':      
            yard = orig_value * 1.0936
            return yard
        
        if fromUnit == 'mile' and toUnit == 'meter':      
            meter = orig_value/0.00062137
            return meter    
        
        if fromUnit == 'meter' and toUnit == 'mile':      
            meter = orig_value * 0.00062137
            return meter 
        

import unittest

class KnownValues(unittest.TestCase):
    known_values_cel_to_kel = ((0, 273.15), (25, 298.15), (75.8, 348.95), (100.5, 373.65), (54, 327.15))
    
    known_values_cel_to_far = ((0, 32), (5.23, 41.414), (14.5, 58.1), (25, 77), (75.8, 168.44))
    
    known_values_far_to_kel = ((132, 328.706), (85.4, 302.8167), (23.4, 268.3722), (-14, 247.594), (0, 255.372))
    
    known_values_mile_to_yard = ((1, 1760), (55.4, 97504), (400, 704000), (15, 26400), (90.5, 159280))
    
    known_values_yard_to_meter = ((1, 0.9144), (55.4, 50.65776), (400, 365.76), (15, 13.716), (90.5, 82.7532))
    
    known_values_mile_to_meter = ((1, 1609.35), (55.4, 89157.83), (58, 93342.13), (15.4, 24783.95), (90.5, 145645.91))
    
    def testconvertCelsiusToKelvin(self):
        '''CelsiusToKelvin should give known result with known input'''
        for cel, kel in self.known_values_cel_to_kel:
            result = Conversions.conversion('celsius', 'kelvin' , cel)
            self.assertEqual(round(kel,2), round(result,2))
            
    def testconvertKelvinToCelsius(self):
        '''KelvinToCelsius should give known result with known input'''
        for cel, kel in self.known_values_cel_to_kel:
            result = Conversions.conversion('kelvin', 'celsius', kel)
            self.assertEqual(round(cel,2), round(result,2))    
        
    def testconvertCelsiusToFarenheit(self):
        '''CelsiusToFarenheit should give known result with known input'''
        for cel, far in self.known_values_cel_to_far:
            result = Conversions.conversion('celsius', 'farenheit', cel)
            self.assertEqual(far, result)
            
    def testconvertFarenheitToCelsius(self):
        '''FarenheitToCelsius should give known result with known input'''
        for cel, far in self.known_values_cel_to_far:
            result = Conversions.conversion('farenheit', 'celsius', far)
            self.assertEqual(round(cel,2), round(result,2))

    def testconvertFarenheitToKelvin(self):
        '''FarenheitToKelvin should give known result with known input'''
        for far, kel in self.known_values_far_to_kel:
            result = Conversions.conversion('farenheit', 'kelvin', far)
            self.assertEqual(round(kel,2), round(result,2))
 
    def testconvertKelvinToFarenheit(self):
        '''FarenheitToKelvin should give known result with known input'''
        for far, kel in self.known_values_far_to_kel:
            result = Conversions.conversion('kelvin', 'farenheit', kel)
            self.assertEqual(round(far,2), round(result,2))
            


    def testconvertMileToYard(self):
        '''MileToYard should give known result with known input'''
        for mile, yard in self.known_values_mile_to_yard:
            result = Conversions.conversion('mile', 'yard', mile)
            self.assertEqual(round(yard,2), round(result,2))
            
    def testconvertYardToMile(self):
        '''YardToMile should give known result with known input'''
        for mile, yard in self.known_values_mile_to_yard:
            result = Conversions.conversion('yard', 'mile', yard)
            self.assertEqual(round(mile,2), round(result,2))    
        
    def testconvertYardToMeter(self):
        '''YardToMeter should give known result with known input'''
        for yard, meter in self.known_values_yard_to_meter:
            result = Conversions.conversion('yard', 'meter', yard)
            self.assertEqual(round(meter,2), round(result,2))
            
    def testconvertMeterToYard(self):
        '''MeterToYard should give known result with known input'''
        for yard, meter in self.known_values_yard_to_meter:
            result = Conversions.conversion('meter','yard', meter)
            self.assertEqual(round(yard,2), round(result,2))

    def testconvertMileToMeter(self):
        '''MileToMeter should give known result with known input'''
        for mile, meter in self.known_values_mile_to_meter:
            result = Conversions.conversion('mile', 'meter', mile)
            self.assertEqual(round(meter,2), round(result,2))
 
    def testconvertMeterToMile(self):
        '''MeterToMile should give known result with known input'''
        for mile, meter in self.known_values_mile_to_meter:
            result = Conversions.conversion('meter', 'mile', meter)
            self.assertEqual(round(mile,2), round(result,2))            
            
            
            
if __name__ == '__main__':
    unittest.main(verbosity=2)
        