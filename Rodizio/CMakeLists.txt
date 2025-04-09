cmake_minimum_required(VERSION 3.26)
project(rodizio_veiculos C)

set(CMAKE_C_STANDARD 11)

# Adicione esta linha para incluir todos os arquivos fonte
add_executable(rodizio_veiculos main.c rodizio.c)
