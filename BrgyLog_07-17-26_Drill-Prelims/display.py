def display_menu():
    """Display the main menu options"""
    print("\n" + "-" * 50)
    print("   MAIN MENU")
    print("-" * 50)
    print("   [1] Magdagdag ng Bisita")
    print("   [2] Tingnan ang Lahat ng Bisita")
    print("   [3] Maghanap ng Bisita")
    print("   [4] Lumabas")
    print("-" * 50)

def display_header():
    """Display the system header"""
    print("=" * 60)
    print("   BARANGAY ACTIVE LOG SYSTEM")
    print("   BrgyActiveLog_07-17-26_drill_Prelims")
    print("=" * 60)

def display_visitors(visitors):
    """Display all visitors in the log"""
    print("\n=== BARANGAY VISITOR LOG ===")
    
    if not visitors:
        print("Walang bisita sa logbook.")
    else:
        # Assuming visitors is a list of tuples: (name, purpose)
        for i, visitor in enumerate(visitors, start=1):
            print(f"{i}. Name: {visitor[0]} | Purpose: {visitor[1]}")
    
    print(f"\nTotal number of visitors: {len(visitors)}")
    print("=" * 30)