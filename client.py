import socket
from prettytable import PrettyTable

# Information that will be used by the client to connect to the server, such as the server's IP address and port
PORT = 49999
SERVER = "127.0.0.1"
# TCP-based socket creation for the client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# We can determine if we have any problems using try and expect that.
try:
    client.connect((SERVER, PORT))
except:
    print("There is a Problem, Cant Find Server Restart Client or Server")
    exit(0)

# Here is the header of the table of usernames connected to the server right now.
table_list_client = PrettyTable(["User Name"])
# Obtaining the user name allows us to include it in the table of active users.
user = input("Enter Your Username : ")
# Obtain the username entered, then encode it in a variable.
user_encode = user.encode('utf-8')
client.sendall(user_encode)
# A list of the users who are currently connected is sent to the client.
list_client = client.recv(2085).decode()
print("\n Hi ", user)
print("\n•┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈•")


def print_list(input_):
    # prints the info that was decoded from the server's sent data.
    input_decoded = input_.decode('utf-8')
    print(input_decoded)


while True:
    #  Request it from the server the user wants to utilize.
    # There are several restrictions here, therefore the user must enter the correct information to commit.
    try:
        print("1. Display All arrived flights")
        print("2. Display All delayed flights")
        print("3. Display All flights from a specific city")
        print("4. Display Details of a particular flight")
        print("5. Quit(exit)")
        option = input("\nEnter the Option (Should From 1 to 5): \n")
        print("•┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈•")
        
        # Option 1 will be encoded and sent to the server if the user selects it.
        # Once the operation is complete, obtain the data from the server and print the data.
        if option == "1":
            client.sendall(option.encode())
            data = client.recv(8192)
            print_list(data)

        # In the event that the user selects Option 2, we shall encrypt and send that selection to the server.
        # Once the operation is complete, obtain the data from the server and print the data.
        elif option == "2":
            client.sendall(option.encode())
            data = client.recv(16384)
            print_list(data)

        # Option 3 will be encoded and sent to the server if the user selects it.
        # Additionally, request the city IATA and provide it to the server encoded.
        # Once the operation is complete, obtain the data from the server and print the data.
        elif option == "3":
            client.sendall(option.encode())
            city_iata = input("Please Enter City IATA: ")
            client.sendall(city_iata.encode())
            data = client.recv(8192)
            print_list(data)

        # Option 4 will be encoded and sent to the server if the user selects it
        # Additionally, request the flight IATA and transmit it to the server encoded.
        # Once the operation is complete, obtain the data from the server and print the data.
        elif option == "4":
            client.sendall(option.encode())
            flight_iata = input("Please Enter Flight IATA: ")
            client.sendall(flight_iata.encode())
            data = client.recv(8192)
            print_list(data)

        #Option 5 will be encoded and sent to the server if the user selects it.
        # print "goodbye" to the user before closing the application.
        elif option == "5":
            client.sendall(option.encode())
            print("Good Bye, see you soon :)")
            client.close()
            break
        
        # When a user selects a false option
        else:
            print("\n Invalid Option , Please Enter Number From 1 to 5:")
        print("•┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈•")
    except:
        print("There is a Problem, We Cant Find Server")
        break
