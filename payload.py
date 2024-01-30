'''
payload.py
This file contains all software to handle whatever payload the intended satellite contains
Yearling-2 contains simply a bno085 9 DOF sensor that is being implemented in this software
Author: Nicole Maggard
'''
import time
import board
import busio
import traceback
from debugcolor import co
import adafruit_bno055

class PAYLOAD:
    def debug_print(self,statement):
        """
        Print a debug statement if debugging is enabled.

        Parameters:
        - statement (str): The debug statement to be printed.
        """
        if self.debug:
            print(co("[Payload]" + statement, 'gray', 'bold'))
    
    def Enable(self, data):
        # print debug statement
        self.debug_print("Enabling the following: " + str(data))
        if "acceleration" in data:
            """
            Check if the string "acceleration" is present in the data.

            If the condition is true, enable the accelerometer feature for the BNO sensor
            and initialize the self.acceleration attribute to (0, 0, 0).

            Parameters:
            - data (str): The variable containing data to be checked.

            Note: This assumes that the 'data' variable holds information about sensor features.

            Example Usage:
            if "acceleration" in sensor_data:
            your_instance.enable_accelerometer()
            """

            from adafruit_bno08x import BNO_REPORT_ACCELEROMETER
            # Enable the accelerometer feature for the BNO sensor
            self.bno.enable_feature(BNO_REPORT_ACCELEROMETER)
            # Initialize the self.acceleration attribute to (0, 0, 0)
            self.acceleration=(0,0,0)
        if "gyroscope" in data:
            """
            Check if the string "gyroscope" is present in the data.

            If the condition is true, enable the gyroscope feature for the BNO sensor
            and initialize the self.gyroscope attribute to (0, 0, 0).

            Parameters:
            - data (str): The variable containing data to be checked.

            Note: This assumes that the 'data' variable holds information about sensor features.

            Example Usage:
            if "gyroscope" in sensor_data:
                your_instance.enable_gyroscope()
            """
            from adafruit_bno08x import BNO_REPORT_GYROSCOPE
            # Enable the gyroscope feature for the BNO sensor
            self.bno.enable_feature(BNO_REPORT_GYROSCOPE)
            # Initialize the self.gyroscope attribute to (0, 0, 0)
            self.gyroscope=(0,0,0)
        if "magnetometer" in data:
            """
            Check if the string "magnetometer" is present in the data.

            If the condition is true, enable the magnetometer feature for the BNO sensor
            and initialize the self.magnetometer attribute to (0, 0, 0).

            Parameters:
            - data (str): The variable containing data to be checked.

            Note: This assumes that the 'data' variable holds information about sensor features.

            Example Usage:
            if "magnetometer" in sensor_data:
                your_instance.enable_magnetometer()
            """
            from adafruit_bno08x import BNO_REPORT_MAGNETOMETER
            # Enable the magnetometer feature for the BNO sensor
            self.bno.enable_feature(BNO_REPORT_MAGNETOMETER)
            # Initialize the self.magnetometer attribute to (0, 0, 0)
            self.magnetometer=(0,0,0)
        if "linear acceleration" in data:
            """
            Check if the string "linear acceleration" is present in the data.

            If the condition is true, enable the linear acceleration feature for the BNO sensor
            and initialize the self.linear_acceleration attribute to (0, 0, 0).

            Parameters:
            - data (str): The variable containing data to be checked.

            Note: This assumes that the 'data' variable holds information about sensor features.

            Example Usage:
            if "linear acceleration" in sensor_data:
                your_instance.enable_linear_acceleration()
            """
            from adafruit_bno08x import BNO_REPORT_LINEAR_ACCELERATION
            # Enable the linear acceleration feature for the BNO sensor
            self.bno.enable_feature(BNO_REPORT_LINEAR_ACCELERATION)
            # Initialize the self.linear_acceleration attribute to (0, 0, 0)
            self.linear_acceleration=(0,0,0)
        if "rotation vector" in data:
            """
            Check if the string "rotation vector" is present in the data.

            If the condition is true, enable the rotation feature for the BNO sensor
            and initialize the self.rotation attribute to (0, 0, 0).

            Parameters:
            - data (str): The variable containing data to be checked.

            Note: This assumes that the 'data' variable holds information about sensor features.

            Example Usage:
            if "rotation" in sensor_data:
                your_instance.enable_rotation()
            """
            from adafruit_bno08x import BNO_REPORT_ROTATION_VECTOR
            # Enable the rotation feature for the BNO sensor
            self.bno.enable_feature(BNO_REPORT_ROTATION_VECTOR)
            # Initialize the self.rotation attribute to (0, 0, 0)
            self.rotation=(0,0,0)
        if "geomagnetic rotation vector" in data:
            """
            Check if the string "geomagnetic rotation vector" is present in the data.

            If the condition is true, enable the geomagnetic rotation feature for the BNO sensor
            and initialize the self.geomagnetic_rotation attribute to (0, 0, 0).

            Parameters:
            - data (str): The variable containing data to be checked.

            Note: This assumes that the 'data' variable holds information about sensor features.

            Example Usage:
            if "geomagnetic rotation vector" in sensor_data:
                your_instance.enable_geomagnetic_rotation()
            """
            from adafruit_bno08x import BNO_REPORT_GEOMAGNETIC_ROTATION_VECTOR
            # Enable the geomegnetic feature for the BNO sensor
            self.bno.enable_feature(BNO_REPORT_GEOMAGNETIC_ROTATION_VECTOR)
            # Initialize the self.geomagnetic_rotation attribute to (0, 0, 0)
            self.geomagnetic_rotation=(0,0,0)
        if "game rotation vector" in data:
            """
            Check if the string "game rotation vector" is present in the data.

            If the condition is true, enable the game rotation feature for the BNO sensor
            and initialize the self.game_rotation attribute to (0, 0, 0).

            Parameters:
            - data (str): The variable containing data to be checked.

            Note: This assumes that the 'data' variable holds information about sensor features.

            Example Usage:
            if "game rotation vector" in sensor_data:
                your_instance.enable_game_rotation()
            """
            from adafruit_bno08x import BNO_REPORT_GAME_ROTATION_VECTOR
            # Enable the game rotation feature for the BNO sensor
            self.bno.enable_feature(BNO_REPORT_GAME_ROTATION_VECTOR)
            # Initialize the self.game_rotation attribute to (0, 0, 0)
            self.game_rotation=(0,0,0)
        if "raw acceleration" in data:
            """
            Check if the string "raw acceleration" is present in the data.

            If the condition is true, enable the raw acceleration feature for the BNO sensor
            and initialize the self.raw_acceleration attribute to (0, 0, 0).

            Parameters:
            - data (str): The variable containing data to be checked.

            Note: This assumes that the 'data' variable holds information about sensor features.

            Example Usage:
            if "raw_acceleration" in sensor_data:
                your_instance.enable_raw_acceleration()
            """
            from adafruit_bno08x import BNO_REPORT_RAW_ACCELEROMETER
            # Enable the raw acceleration feature for the BNO sensor
            self.bno.enable_feature(BNO_REPORT_RAW_ACCELEROMETER)
            # Initialize the self.raw_acceleration attribute to (0, 0, 0)
            self.raw_acceleration=(0,0,0)
        if "raw gyroscope" in data:
            """
            Check if the string "raw gyroscope" is present in the data.

            If the condition is true, enable the raw gyroscope feature for the BNO sensor
            and initialize the self.raw_gyroscope attribute to (0, 0, 0).

            Parameters:
            - data (str): The variable containing data to be checked.

            Note: This assumes that the 'data' variable holds information about sensor features.

            Example Usage:
            if "raw gyroscope" in sensor_data:
                your_instance.enable_raw_gyroscope()
            """
            from adafruit_bno08x import BNO_REPORT_RAW_GYROSCOPE
            # Enable the raw gyroscope feature for the BNO sensor
            self.bno.enable_feature(BNO_REPORT_RAW_GYROSCOPE)
            # Initialize the self.raw_gyroscope attribute to (0, 0, 0)
            self.raw_gyroscope=(0,0,0)
        if "raw magnetometer" in data:
            """
            Check if the string "raw magnetometer" is present in the data.

            If the condition is true, enable the raw magnetometer feature for the BNO sensor
            and initialize the self.raw_magnetometer attribute to (0, 0, 0).

            Parameters:
            - data (str): The variable containing data to be checked.

            Note: This assumes that the 'data' variable holds information about sensor features.

            Example Usage:
            if "raw magnetometer" in sensor_data:
                your_instance.enable_raw_magnetometer()
            """
            from adafruit_bno08x import BNO_REPORT_RAW_MAGNETOMETER
            # Enable the raw magnetometer feature for the BNO sensor
            self.bno.enable_feature(BNO_REPORT_RAW_MAGNETOMETER)
            # Initialize the self.raw_magnetometer attribute to (0, 0, 0)
            self.raw_magnetometer=(0,0,0)

    def __init__(self, debug, i2c, data=[]):
        """
        Initialize an instance of PAYLOAD with the specified parameters.

        Parameters:
        - debug (bool): Set to True to enable debugging, which will print debug statements.
        - i2c: The I2C bus object used to communicate with the BNO055 sensor.
        - data (list): Optional parameter to provide initial data for the instance.
        """
        self.debug=debug
        self.data=data
        self.debug_print("Initializing BNO055...")
        try:
            # Attempt to initialize the BNO055 sensor using the provided I2C bus
            self.bno = adafruit_bno055.BNO055_I2C(i2c)
            self.debug_print("Initialization of BNO complete without error!")
        except Exception as e:
            # Handle any exceptions that may occur during BNO055 initialization
            self.debug_print("ERROR Initializing BNO sensor: " + ''.join(traceback.format_exception(e)))
    
    def reinit(self,data=[]):
        """
        Reinitialize the BNO08x sensor.

        This method attempts to reinitialize the BNO08x sensor using the specified data.

        Parameters:
        - data (list): Optional parameter to provide data for the reinitialization.
        """
        try:
            # Print a debug statement indicating the start of the reinitialization process
            self.debug_print("Reinitializing BNO08x...")
            # Call the Enable method with the provided data for reinitialization
            self.Enable(self.data)
            # Print a success debug statement if reinitialization is complete without error
            self.debug("Reinitialization of BNO complete without error!")
        except Exception as e:
            # Handle any exceptions that may occur during BNO08x reinitialization
            self.debug_print("ERROR Initializing BNO sensor: " + ''.join(traceback.format_exception(e)))

    @property
    def Data(self):
        # This property allows external code to retrieve the current value of the 'data' attribute.
        return self.data
    
    def UpdateData(self, data, option="append"):
        if option == "replace":
            # Replace the current 'data' attribute with the specified data
            self.data=data
        if option == "append":
            # Append the specified data to the current 'data' attribute
            self.data.append(data)
        else:
            # Raise an error for an incorrect option argument input
            raise TypeError("Incorrect option argument input. Please use either \"append\" or \"replace\"")
        # Reinitialize the BNO08x sensor after updating the 'data' attribute
        self.reinit()  

    @property
    def Acceleration(self):
        if "acceleration" in self. data:
            # If "acceleration" feature is enabled, retrieve acceleration data from the BNO sensor
            self.acceleration=self.bno.acceleration
        return self.acceleration
    
    @property
    def Gyroscope(self):
        if "gyroscope" in self. data:
            # If "gyroscope" feature is enabled, retrieve gyroscope data from the BNO sensor
            self.gyroscope=self.bno.gyro
        return self.gyroscope
    
    @property
    def Magnetometer(self):
        if "magnetometer" in self. data:
            # If "magnetometer" feature is enabled, retrieve magnetometer data from the BNO sensor
            self.magnetometer=self.bno.magnetic
        return self.magnetometer
    
    @property
    def Linear_Acceleration(self):
        if "linear acceleration" in self. data:
            # If "linear acceleration" feature is enabled, retrieve linear acceleration data from the BNO sensor
            self.linear_acceleration=self.bno.linear_acceleration
        return self.linear_acceleration
    
    @property
    def Rotation(self):
        if "rotation vector" in self. data:
            # If "rotation vector" feature is enabled, retrieve rotation vector data from the BNO sensor
            self.rotation=self.bno.quaternion
        return self.rotation
    
    @property
    def Geomagnetic_Rotation(self):
        if "geomagnetic rotation vector" in self. data:
            # If "geomagnetic rotation vector" feature is enabled, retrieve geomagnetic rotation vector data from the BNO sensor
            self.geomagnetic_rotation=self.bno.geomagnetic_quaternion
        return self.geomagnetic_rotation
    
    @property
    def Game_Rotation(self):
        if "game rotation vector" in self. data:
            # If "game rotation vector" feature is enabled, retrieve game rotation vector data from the BNO sensor
            self.game_rotation=self.bno.game_quaternion
        return self.game_rotation
    
    @property
    def Raw_Acceleration(self):
        if "raw acceleration" in self. data:
            # If "raw acceleration" feature is enabled, retrieve raw acceleration data from the BNO sensor
            self.raw_acceleration=self.bno.raw_acceleration
        return self.raw_acceleration
    
    @property
    def Raw_Gyroscope(self):
        if "raw gyroscope" in self. data:
            # If "raw gyroscope" feature is enabled, retrieve raw gyroscope data from the BNO sensor
            self.raw_gyroscope=self.bno.raw_gyro
        return self.raw_gyroscope
    
    @property
    def Raw_Magnetometer(self):
        if "raw magnetometer" in self. data:
            # If "raw magnetometer" feature is enabled, retrieve raw magnetometer data from the BNO sensor
            self.raw_magnetometer=self.bno.raw_magnetic
        return self.raw_magnetometer