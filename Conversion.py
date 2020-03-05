# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 13:00:31 2020

@author: kbootsri
"""

class TempChange():
    def CelsiusToKelvin(celsius):
        kelvin = celsius + 273.15
        return kelvin
    
    def CelsiusToFahrenheit(celsius):
        multipler = 9/5
        farenheit = (celsius * multipler) + 32
        return farenheit
    
    def FarenheitToCelsius(farenheit):
        multipler = 5/9
        celsius = (farenheit - 32) * multipler
        return celsius
    
    def FarenheitToKelvin(farenheit):
        multipler = 5/9
        kelvin = (farenheit + 459.67) * multipler
        return kelvin
    
    def KelvinToCelsius(kelvin):
        celsius = kelvin - 273.15
        return celsius
    
    def KelvinToFarenheit(kelvin):
        multipler = 9/5
        farenheit = (kelvin * multipler) - 459.67
        return farenheit
    

import unittest

class KnownValues(unittest.TestCase):
    known_values_cel_to_kel = ((0, 273.15), (25, 298.15), (75.8, 348.95), (100.5, 373.65), (54, 327.15))
    
    known_values_cel_to_far = ((0, 32), (5.23, 41.414), (14.5, 58.1), (25, 77), (75.8, 168.44))
    
    known_values_far_to_kel = ((132, 328.706), (85.4, 302.8167), (23.4, 268.3722), (-14, 247.594), (0, 255.372))
    
    
    def testconvertCelsiusToKelvin(self):
        '''CelsiusToKelvin should give known result with known input'''
        for cel, kel in self.known_values_cel_to_kel:
            result = TempChange.CelsiusToKelvin(cel)
            self.assertEqual(round(kel,2), round(result,2))
            
    def testconvertKelvinToCelsius(self):
        '''KelvinToCelsius should give known result with known input'''
        for cel, kel in self.known_values_cel_to_kel:
            result = TempChange.KelvinToCelsius(kel)
            self.assertEqual(round(cel,2), round(result,2))    
        
    def testconvertCelsiusToFahrenheit(self):
        '''CelsiusToFahrenheit should give known result with known input'''
        for cel, far in self.known_values_cel_to_far:
            result = TempChange.CelsiusToFahrenheit(cel)
            self.assertEqual(round(far,2), round(result,2))
            
    def testconvertFahrenheitToCelsius(self):
        '''FahrenheitToCelsius should give known result with known input'''
        for cel, far in self.known_values_cel_to_far:
            result = TempChange.FarenheitToCelsius(far)
            self.assertEqual(round(cel,2), round(result,2))

    def testconvertFarenheitToKelvin(self):
        '''FarenheitToKelvin should give known result with known input'''
        for far, kel in self.known_values_far_to_kel:
            result = TempChange.FarenheitToKelvin(far)
            self.assertEqual(round(kel,2), round(result,2))
 
    def testconvertKelvinToFarenheit(self):
        '''FarenheitToKelvin should give known result with known input'''
        for far, kel in self.known_values_far_to_kel:
            result = TempChange.KelvinToFarenheit(kel)
            self.assertEqual(round(far,2), round(result,2))

           
if __name__ == '__main__':
    unittest.main(verbosity=2)
        
    
