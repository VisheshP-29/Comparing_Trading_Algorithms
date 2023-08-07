#Set the minimum required version of CMake to be 3.10
cmake_minimum_required(VERSION 3.10)

#Create a project named Tutorial
project(Trading_Strategies_Profit_Comparison
        VERSION 1.0
        LANGUAGES CXX)

# TODO 7: Set the project version number as 1.0 in the above project command

# TODO 6: Set the variable CMAKE_CXX_STANDARD to 11
#         and the variable CMAKE_CXX_STANDARD_REQUIRED to True

# TODO 8: Use configure_file to configure and copy TutorialConfig.h.in to
#         TutorialConfig.h

# Add an executable called Tutorial to the project
# Hint: Be sure to specify the source file as tutorial.cxx
#file(GLOB_RECURSE src CONFIGURE_DEPENDS ${src}/*.cpp)
#add_executable()

# TODO 9: Use target_include_directories to include ${PROJECT_BINARY_DIR}
