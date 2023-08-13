# Step 1: Set the minimum required version of CMake
cmake_minimum_required(VERSION 3.14)

# Step 2: Create a project named Tutorial
project(Comparing_Trading_Algorithms
        VERSION 1.0
        LANGUAGES CXX)

# Step 4: Set the variable CMAKE_CXX_STANDARD to 17
#         and the variable CMAKE_CXX_STANDARD_REQUIRED to True
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

#find_package(PythonLibs REQUIRED)
#include_directories(${PYTHON_INCLUDE_DIRS})
#add_library(test /opt/homebrew/opt/python@3.11/Frameworks/Python.framework/Versions/3.11/include/python3.11)
#target_include_directories(test PRIVATE /opt/homebrew/opt/python@3.11/Frameworks/Python.framework/Versions/3.11/include/python3.11)
# /opt/homebrew/opt/python@3.11/Frameworks/Python.framework/Versions/3.11/include/python3.11

# Step 3: Add an executable
# Hint: Be sure to specify the source file(s)
set(src_dir ${CMAKE_SOURCE_DIR}/src)

#set(SOURCES)

#add_executable(main ${src_dir}/main.cpp ${test})
add_executable(main ${src_dir}/main.cpp)

target_include_directories(main PRIVATE /opt/homebrew/opt/python@3.11/Frameworks/Python.framework/Versions/3.11/include/python3.11)
target_link_libraries(main /opt/homebrew/opt/python@3.11/Frameworks/Python.framework/Versions/3.11/lib/python3.11/config-3.11-darwin/libpython3.11.a)