import os
import yaml


# Loads data from config file
def load_config(path):
    with open(path, 'r') as open_file:
        return yaml.safe_load(open_file)


# Locates config file in directory
def find_config(path):
    if os.path.exists(path):
        print("\nConfig file found.\n")  # Debug output
        config_data = load_config(path)
        return config_data
    print("\nConfig file not found, entering manual mode\n")  # Debug output
    return None


# Gets information in manual mode
def manual():
    while True:
        try:
            pid = int(input("Please enter the PilotId: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    while True:
        cert_input = input("\nPlease enter if you have any certifications (True/False): ").strip().lower()
        if cert_input in ('true', 'false'):
            cert = cert_input == 'true'
            break
        else:
            print("Invalid input. Please enter either 'True' or 'False'.")
    while True:
        try:
            flight_hrs = int(input("Please enter the amount of flight hours: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    while True:
        try:
            sim_hrs = int(input("Please enter the amount of simulation hours: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    return pid, cert, flight_hrs, sim_hrs


# Writes the argument file
def write_argument_file(pid, cert, f_hours, sim_hours):
    argument_filename = f"Pilot{pid}.argument"
    argument_file = os.path.join(script_dir, argument_filename)
    print(argument_filename + " created")
    flight_hours_bool = False
    sim_hours_bool = False
    n = 10

    # Sets booleans based on relation to N
    if f_hours is not None and f_hours >= n:
        flight_hours_bool = True
    if sim_hours is not None and sim_hours >= n:
        sim_hours_bool = True

    with open(argument_file, "w") as file:

        # Writes starting nodes and arrows
        file.write(argument_filename + "\n\n")
        file.write("Goal G1 {\n     description \"Safe flight in controlled airspace\"\n}\n")
        file.write("Strategy S1 {\n     description ")
        file.write("\"Argue the pilot is trusted enough to safely complete the flight\"\n}\n")
        file.write("Context C1 {\n     description \"Pilot description\"\n}\n")
        file.write("Context C2 {\n     description ")
        file.write("\"If pilot is certified or has enough flight/simulation time we will allow the flight\"\n}\n")

        file.write("IsSupportedBy ISB1 {\n     to S1 from G1\"\n}\n")
        file.write("InContextOf ICO1 {\n     to C1 from S1\"\n}\n")
        file.write("InContextOf ICO2 {\n     to C2 from S1\"\n}\n")

        # If there's a certification
        if cert:
            file.write("Goal G2 {\n     description \"The pilot is certified to fly their UAS\"\n}\n")
            file.write("Solution E1 {\n     description ")
            file.write('"Check confirms the pilot is certified. [Certification] == \\n\\"Part 107\\""\n}\n')
            file.write("IsSupportedBy ISB2 {\n     to G2 from S1\"\n}\n")
            file.write("IsSupportedBy ISB3 {\n     to E1 from G2\"\n}\n")

            # Certification, flight and simulation are true
            if flight_hours_bool and sim_hours_bool:
                file.write("Goal G3 {\n     description ")
                file.write("\"The pilot has sufficient flight hours to complete the flight\"\n}\n")
                file.write("Solution E2 {\n     description ")
                file.write("\"Check confirms the pilot has enough flight time. ")
                file.write("[Flight_Hours] is [Greater_Than_or_Equal_to_N]\"\n}\n")

                file.write("IsSupportedBy ISB4 {\n     to G3 from S1\"\n}\n")
                file.write("IsSupportedBy ISB5 {\n     to E2 from G3\"\n}\n")

                file.write("Goal G4 {\n     description ")
                file.write("\"The pilot has sufficient simulation hours to complete the flight\"\n}\n")
                file.write("Solution E3 {\n     description ")
                file.write("\"Check confirms the pilot has enough simulation flight time. ")
                file.write("[Simulation_Hours] is [Greater_Than_or_Equal_to_N]\"\n}\n")

                file.write("IsSupportedBy ISB6 {\n     to G4 from S1\"\n}\n")
                file.write("IsSupportedBy ISB7 {\n     to E3 from G4\"\n}\n")

            # Certification and flight are true
            elif flight_hours_bool:
                file.write("Goal G3 {\n     description ")
                file.write("\"The pilot has sufficient flight hours to complete the flight\"\n}\n")
                file.write("Solution E2 {\n     description ")
                file.write("\"Check confirms the pilot has enough flight time. ")
                file.write("[Flight_Hours] is [Greater_Than_or_Equal_to_N]\"\n}\n")

                file.write("IsSupportedBy ISB4 {\n     to G3 from S1\"\n}\n")
                file.write("IsSupportedBy ISB5 {\n     to E2 from G3\"\n}\n")

            # Certification and simulation are true
            elif sim_hours_bool:
                file.write("Goal G3 {\n     description ")
                file.write("\"The pilot has sufficient simulation hours to complete the flight\"\n}\n")
                file.write("Solution E2 {\n     description ")
                file.write("\"Check confirms the pilot has enough simulation flight time. ")
                file.write("[Simulation_Hours] is [Greater_Than_or_Equal_to_N]\"\n}\n")

                file.write("IsSupportedBy ISB4 {\n     to G3 from S1\"\n}\n")
                file.write("IsSupportedBy ISB5 {\n     to E2 from G3\"\n}\n")

        else:
            # Flight and simulation are true
            if flight_hours_bool and sim_hours_bool:
                file.write("Goal G2 {\n     description ")
                file.write("\"The pilot has sufficient flight hours to complete the flight\"\n}\n")
                file.write("Solution E1 {\n     description ")
                file.write("\"Check confirms the pilot has enough flight time. ")
                file.write("[Flight_Hours] is [Greater_Than_or_Equal_to_N]\"\n}\n")

                file.write("IsSupportedBy ISB2 {\n     to G2 from S1\"\n}\n")
                file.write("IsSupportedBy ISB3 {\n     to E1 from G2\"\n}\n")

                file.write("Goal G3 {\n     description ")
                file.write("\"The pilot has sufficient simulation hours to complete the flight\"\n}\n")
                file.write("Solution E2 {\n     description ")
                file.write("\"Check confirms the pilot has enough simulation flight time. ")
                file.write("[Simulation_Hours] is [Greater_Than_or_Equal_to_N]\"\n}\n")

                file.write("IsSupportedBy ISB4 {\n     to G3 from S1\"\n}\n")
                file.write("IsSupportedBy ISB5 {\n     to E2 from G3\"\n}\n")

            # Flight is true
            elif flight_hours_bool:
                file.write("Goal G2 {\n     description ")
                file.write("\"The pilot has sufficient flight hours to complete the flight\"\n}\n")
                file.write("Solution E1 {\n     description ")
                file.write("\"Check confirms the pilot has enough flight time. ")
                file.write("[Flight_Hours] is [Greater_Than_or_Equal_to_N]\"\n}\n")

                file.write("IsSupportedBy ISB2 {\n     to G2 from S1\"\n}\n")
                file.write("IsSupportedBy ISB3 {\n     to E1 from G2\"\n}\n")

            # Simulation is true
            elif sim_hours_bool:
                file.write("Goal G2 {\n     description ")
                file.write("\"The pilot has sufficient simulation hours to complete the flight\"\n}\n")
                file.write("Solution E1 {\n     description ")
                file.write("\"Check confirms the pilot has enough simulation flight time. ")
                file.write("[Simulation_Hours] is [Greater_Than_or_Equal_to_N]\"\n}\n")

                file.write("IsSupportedBy ISB2 {\n     to G2 from S1\"\n}\n")
                file.write("IsSupportedBy ISB3 {\n     to E1 from G2\"\n}\n")

            # None are true
            else:
                file.write("Goal G2 {\n     description \"The pilot is certified to fly their UAS\"\n}\n")
                file.write("Solution E1 {\n     description ")
                file.write('FAILED: "Check confirms the pilot is certified. [Certification] == \\n\\"Part 107\\""\n}\n')
                file.write("Goal G3 {\n     description ")
                file.write("\"The pilot has sufficient flight hours to complete the flight\"\n}\n")
                file.write("Solution E2 {\n     description ")
                file.write("FAILED: \"Check confirms the pilot has enough flight time. ")
                file.write("[Flight_Hours] is [Greater_Than_or_Equal_to_N]\"\n}\n")
                file.write("Goal G4 {\n     description ")
                file.write("\"The pilot has sufficient simulation hours to complete the flight\"\n}\n")
                file.write("Solution E3 {\n     description ")
                file.write("FAILED: \"Check confirms the pilot has enough simulation flight time. ")
                file.write("[Simulation_Hours] is [Greater_Than_or_Equal_to_N]\"\n}\n")

                file.write("IsSupportedBy ISB2 {\n     to G2 from S1\"\n}\n")
                file.write("IsSupportedBy ISB3 {\n     to E1 from G2\"\n}\n")
                file.write("IsSupportedBy ISB4 {\n     to G3 from S1\"\n}\n")
                file.write("IsSupportedBy ISB5 {\n     to E2 from G3\"\n}\n")
                file.write("IsSupportedBy ISB6 {\n     to G4 from S1\"\n}\n")
                file.write("IsSupportedBy ISB7 {\n     to E3 from G4\"\n}\n")


if __name__ == "__main__":
    # Gets directory and filepath if it exists
    script_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(script_dir, 'pilotConfig.YAML')
    config_file = find_config(config_path)

    # Get number of pilots from manual mode if config file doesn't exist
    if config_file is None:
        while True:
            try:
                num_of_pilots = int(input("Please enter the amount of pilots: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
    else:
        num_of_pilots = config_file.get('NumOfPilots')

    # Current pilot
    count = 1

    while True:
        if count <= num_of_pilots:
            if config_file:
                pilots = config_file.get('Pilots', [])
                for pilot in pilots:
                    if pilot.get('PilotId') is not None:
                        p_id = pilot.get('PilotId')
                        certification = pilot.get('Certification')
                        flight_hours = pilot.get('FlightHours')
                        simulation_hours = pilot.get('SimHours')

                        write_argument_file(p_id, certification, flight_hours, simulation_hours)
                        count += 1
                    else:
                        break
            else:
                p_id, certification, flight_hours, simulation_hours = manual()
                write_argument_file(count, certification, flight_hours, simulation_hours)
                count += 1
        else:
            break

