cmake_minimum_required(VERSION 3.17)
project(HW2)

set(CMAKE_CXX_STANDARD 14)

add_executable(HW_2 main.cpp)
target_link_libraries( HW_2 -lOpenGL32 -lfreeGLUT)