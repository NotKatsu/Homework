class main: 
    def fetch_input() -> dict[str]:
        first_name = str(input("Enter your first name: "))
        second_name = str(input("Enter your second name: "))
        
        return {"first_name": first_name, "second_name": second_name}
        
    def calculate_staff_code(first_name: str, second_name: str) -> str:
        return first_name[0] + second_name[0:2]
    
if __name__ == "__main__":
    input: dict[str] = main.fetch_input()
    print("Staff Code: " + main.calculate_staff_code(input["first_name"], input["second_name"]).upper())