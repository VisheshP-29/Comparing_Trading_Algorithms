# Step 1: Set the minimum required version of CMake
cmake_minimum_required(VERSION 3.14)

# Step 2: Create a project named Tutorial
project(Trading_Strategies_Profit_Comparison
        VERSION 1.0
        LANGUAGES CXX)

# Step 4: Set the variable CMAKE_CXX_STANDARD to 17
#         and the variable CMAKE_CXX_STANDARD_REQUIRED to True
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# Step 3: Add an executable
# Hint: Be sure to specify the source file(s)
set(src_dir ${CMAKE_SOURCE_DIR}/src)

add_executable(main ${src_dir}/main.cpp)