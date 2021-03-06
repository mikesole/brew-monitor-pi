
import datetime

import requests

"""
    REST API communications wrapper for sensor data
"""
class SensorWebComms(object):

    def __init__(self, username, password, target_api_url, _login_decl, post_data_decl):

        self._username = username
        self._password = password
        
        self._target_api_url = target_api_url
        self._login_decl = _login_decl
        self._post_data_decl = post_data_decl

    """
        Get api auth token
    """
    def getAuthToken(self):

        post_url = "".join([self._target_api_url, self._login_decl])

        auth = {'email':self._username, 'password':self._password}

        r = requests.post(post_url, data = auth)

        print(" get token status code: ", r.status_code)

        return r.json()["id"]

    """
        Post sensor reading
    """
    def postSensorReading(self, temp_readings):

        token = self.getAuthToken()
    
        for temp_reading in temp_readings:

            timestamp = str(datetime.datetime.now().isoformat())

            id = str(temp_reading[0])
            value = str(temp_reading[1])
            
            payload = {"sensor-id": id, "value": value, "timestamp": timestamp, "id": timestamp}

            post_url = "".join([self._target_api_url, self._post_data_decl, "?access_token=", token])

            r = requests.post(post_url, json=payload)

            print(" status code: ", r.status_code)
            print(r.json())
            print("\n")
