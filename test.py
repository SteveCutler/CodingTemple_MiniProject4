
# from data_connectDatabase import connect_database
# from mysql.connector import Error


# # conn = connect_database()

# # if conn is not None:
# #     try:
# #         cursor = conn.cursor()
# #         vars = ('*', 'books', '1984')
# #         Fantasy = "Fantasy"
# #         genres = "genres"
# #         #print(vars)

# #         try:
# #             if type == "books":
# #                 #print("type is books")
# #                 query = "SELECT %s FROM %s WHERE title = %s"
                
# #             else:
# #                 #print("type is anything else")
# #                 query = f"SELECT * FROM {genres} WHERE name = '{Fantasy}'"
            
            

# #             cursor.execute(query)
            
# #             response = cursor.fetchall()
            
# #             #print(f"Found '{label}' in '{type}'")
# #             print(response)
# #         except Error as e:
# #             print(f"Error: '{e}")
# #             print(f"\nChecking... ___ is not already in our system.\n")
# #             print("None")

# #     except Error as e:
# #         print(f"Error: {e}")

# #     finally:
# #     #       print("Closing cursor and connection...")
# #         cursor.close()
# #         conn.close()

# # vars = ["3423432", 2, "test"]
# # varsString = ",".join(vars)
# # print(varsString)


# conn = connect_database()

# if conn is not None:
#     try:
#         cursor = conn.cursor()
        

#         try:
#             if type == "books":
#                 print("type is books")
#                 query = f"SELECT * FROM {type} WHERE title = {label}"
                
#             else:
#                 print("type is anything else")
#                 query = "SELECT id FROM authors WHERE name = 'JRR Tolkien'"

#             cursor.execute(query)
#             response = cursor.fetchall()
#             if 
#             print(response)
#             print(str(response))
#             #return str(response)
        
#         except Error as e:
#             #print(f"Error: '{e}")
#             print(f"\nChecking... '{label}' is not already in our system.\n")
#             print("None")
            

#     except Error as e:
#         print(f"Error: {e}")
#         print("None")

#     finally:
#     #   print("Closing cursor and connection...")
#         cursor.close()
#         conn.close()

# from datetime import datetime

# from datetime import timedelta
# today = datetime.today()
# todaystr = today.strftime('%Y-%m-%d')
# duedate = today + timedelta(weeks = 2)
# duedatestr = duedate.strftime('%Y-%m-%d')
# print(duedatestr)

from data_retrieveData import retrieve_data as rd
response = rd("borrowed_books",2)
print(response)