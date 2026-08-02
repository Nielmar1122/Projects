from display import display_menu, display_header, display_visitors

def main():
    display_header()
    
    visitors = []  # List to store visitor tuples: (name, purpose)
    
    while True:
        display_menu()
        choice = input("\nPumili ng opsyon (1-4): ")
        
        if choice == "1":
            name = input("Pangalan ng bisita: ")
            purpose = input("Layunin ng pagbisita: ")
            visitors.append((name, purpose))
            print(f"\n✓ Si {name} ay naitala na sa logbook.")
            
        elif choice == "2":
            display_visitors(visitors)
            
        elif choice == "3":
            name = input("Pangalan ng hahanapin: ")
            found = False
            for visitor in visitors:
                if visitor[0].lower() == name.lower():
                    print(f"\n✓ Natagpuan ang bisita!")
                    print(f"   Name: {visitor[0]}")
                    print(f"   Purpose: {visitor[1]}")
                    found = True
                    break
            if not found:
                print("\n✗ Walang bisita na may ganyang pangalan.")
            
        elif choice == "4":
            print("\nSalamat sa paggamit ng Barangay Active Log System!")
            print("Mag-ingat at mabuhay!")
            break
            
        else:
            print("\n✗ Hindi wasto ang iyong pinili. Pumili ng 1-4.")

if __name__ == "__main__":
    main()