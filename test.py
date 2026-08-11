from tools.tavily_tool import tavily_search
from tools.flight_tool import search_flights
from backend import run_travel_agent

# res = tavily_search("Best hotels in Penang for a 2-day trip")
# print(res)


# res = search_flights("Plan a 7 days Cairo trip from Kuala Lumpur, Malaysia, departing on 2024-07-15 and returning on 2024-07-22. I prefer direct flights and would like to know the best options for economy class.")
# print(res)

user_input = input("Enter travel request: ")

response = run_travel_agent(
    user_input=user_input,
    thread_id="test_user"
)

print("\nFINAL RESPONSE:\n")
print(response["answer"])