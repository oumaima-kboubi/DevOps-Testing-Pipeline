from unittest import TestCase
from app import routes

class LabelCountTest(TestCase):
    def test_low_label(self):
        #Given
        number = 55
        expected_result= {"message":"Let's get more active! Keep the hight spirit"}

        # When
        result = routes.countTaskMessage(number)

        # Then
        assert expected_result == result 

    def test_medium_label(self):
        #Given
        number = 4
        expected_result= {"message":"You seem to be active today! Well done"}
        # When
        result = routes.countTaskMessage(number)

        # Then
        assert expected_result == result 
    
    def test_hight_label(self):
        #Given
        number = 7
        expected_result= {"message":"Excellent job! You deserve a good treat"}

        # When
        result = routes.countTaskMessage(number)

        # Then
        assert expected_result == result 

    
class UserTest(TestCase):
    def test_get_first_task(self):
        #Given
        expected_task=  {
            "taskname":"Do DevOps project",
            "task_id":1,
            "status":"Todo"
        }

        #When
        result = routes.get_first_task(1)

        #Then
        assert expected_task == result