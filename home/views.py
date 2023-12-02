from django.shortcuts import render
from django.http import HttpResponse                                                     
import mysql.connector
# Create your views here.

def main(request):
    return render(request, 'main.html')
    # return HttpResponse("Hello world")

def about(request):
    return render(request, 'about.html')
                
def gallary(request):
    return render(request, 'gallary.html')     

def adminlogin(request):
    return render(request, 'adminlogin.html')                                                             

def createEvent(request):
    
    # Replace these values with your MySQL database information
    print("hai")
    host = 'localhost'
    user = 'root'
    password = 'Jacob@960598'
    database = 'history_timeline'

    inputJson = {
        "event_name": "Hello Event Name Here",
        "event_link": "link here",
        "desc": "event description",
        "event_date": "2023-11-24",
        "likes": 5,
        "event_tag": 1,
        "event_image": "image link here"
    }

    print("hai")
    # Create a connection to the MySQL database
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        if connection.is_connected():
            print("Connected to the MySQL database")

            # Prepare the INSERT query with parameters
            query = """
                INSERT INTO home_event(event_name, link, description, eve_date, likes, eve_tag, eve_image)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            values = (
                inputJson['event_name'],
                inputJson['event_link'],
                inputJson["desc"],
                inputJson["event_date"],
                inputJson["likes"],
                inputJson['event_tag'],
                inputJson['event_image']
            )

            # Execute the query with the data to be inserted
            cursor = connection.cursor()
            cursor.execute(query, values )

            # Commit the changes to the database
            connection.commit()

            print("Data inserted successfully")
            return HttpResponse("Success")

    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL: {e}")
        return HttpResponse("Error")

    except Exception as e:
        print(f"Error: {e}")
        return HttpResponse("Error")

    finally:
        # Close the connection when done
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Connection closed")
    return HttpResponse("hai")


