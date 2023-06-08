cmake_minimum_required(VERSION 3.8)
project(miapr_project)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
# uncomment the following section in order to fill in
# further dependencies manually.
# find_package(<dependency> REQUIRED)

install(DIRECTORY ./src/launch ./src/param ./src/map ./src/rviz ./src/dist_meas DESTINATION ../install)

ament_package()
