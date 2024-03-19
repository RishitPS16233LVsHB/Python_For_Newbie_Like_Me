class HeritageSite:
    def __init__(self, name, location, district, state, built_year, builder, purpose, website=None):
        self.name = name
        self.location = location
        self.district = district
        self.state = state
        self.built_year = built_year
        self.builder = builder
        self.purpose = purpose
        self.website = website

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Location: {self.location}")
        print(f"District: {self.district}")
        print(f"State: {self.state}")
        print(f"Built Year: {self.built_year}")
        print(f"Builder: {self.builder}")
        print(f"Purpose: {self.purpose}")
        if self.website:
            print(f"Website: {self.website}")
        print()

def add_heritage_site(heritage_sites):
    name = input("Enter the name of the heritage site: ")
    location = input("Enter the location of the heritage site: ")
    district = input("Enter the district of the heritage site: ")
    state = input("Enter the state of the heritage site: ")
    built_year = input("Enter the year the heritage site was built: ")
    builder = input("Enter the name of the builder: ")
    purpose = input("Enter the purpose of the heritage site: ")
    website = input("Enter the website link (if any): ")
    heritage_site = HeritageSite(name, location, district, state, built_year, builder, purpose, website)
    heritage_sites.append(heritage_site)

def display_all_sites(heritage_sites):
    for site in heritage_sites:
        site.display_info()

def search_site_by_state(heritage_sites, state):
    found_sites = []
    for site in heritage_sites:
        if site.state.lower() == state.lower():
            found_sites.append(site)
    if found_sites:
        print(f"Heritage sites in {state}:")
        for found_site in found_sites:
            found_site.display_info()
    else:
        print(f"No heritage sites found in {state}")

def main():
    heritage_sites = []

    # Add some initial heritage sites for demonstration
    heritage_sites.append(HeritageSite("Taj Mahal", "Agra", "Agra", "Uttar Pradesh", 1632, "Shah Jahan", "Mausoleum", "https://www.tajmahal.gov.in/"))
    heritage_sites.append(HeritageSite("Red Fort", "Delhi", "Central Delhi", "Delhi", 1639, "Shah Jahan", "Fort", "https://whc.unesco.org/en/list/231/"))
    heritage_sites.append(HeritageSite("Qutub Minar", "Mehrauli", "South Delhi", "Delhi", 1193, "Qutb al-Din Aibak", "Minaret", "https://whc.unesco.org/en/list/233/"))

    while True:
        print("\n1. Add a new heritage site")
        print("2. Display all heritage sites")
        print("3. Search for heritage sites by state")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_heritage_site(heritage_sites)
        elif choice == '2':
            display_all_sites(heritage_sites)
        elif choice == '3':
            state = input("Enter the state to search for heritage sites: ")
            search_site_by_state(heritage_sites, state)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
