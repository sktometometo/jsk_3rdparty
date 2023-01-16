cmake_minimum_required(VERSION 2.8.3)
project(openai_api_ros)

find_package(catkin REQUIRED COMPONENTS
    catkin_virtualenv
    message_generation
)

catkin_generate_virtualenv(
    PYTHON_INTERPRETER python3.8
)

catkin_python_setup()

add_service_files(
  FILES
  Completion.srv
)

generate_messages()

catkin_package(
  CATKIN_DEPENDS message_runtime
)

install(FILES requirements.txt
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

catkin_install_python(PROGRAMS
  scripts/openai_api_node.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
