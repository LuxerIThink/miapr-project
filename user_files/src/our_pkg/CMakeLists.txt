cmake_minimum_required(VERSION 3.5)
project(our_pkg)

find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)
find_package(rclpy REQUIRED)
find_package(nav2_common REQUIRED)
find_package(navigation2 REQUIRED)

nav2_package()

install(DIRECTORY launch DESTINATION share/${PROJECT_NAME})
install(DIRECTORY params DESTINATION share/${PROJECT_NAME})
install(DIRECTORY map DESTINATION share/${PROJECT_NAME})
install(PROGRAMS scripts/dist.py DESTINATION lib/${PROJECT_NAME})

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
