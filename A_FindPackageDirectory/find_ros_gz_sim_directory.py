#Launch using
#cd Desktop
#python3 find_ros_gz_sim_directory.py

#ros_gz_example_bringup
#ros_gz_sim
#px4_offboard

from ament_index_python.packages import get_package_share_directory

def print_package_share_directory(package_name):
    try:
        package_share_directory = get_package_share_directory(package_name)
        print(f"The share directory for the '{package_name}' package is: {package_share_directory}")
    except PackageNotFoundError:
        print(f"The package '{package_name}' was not found.")

if __name__ == "__main__":
    print_package_share_directory('px4_offboard')#Change package name here
    

