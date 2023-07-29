cmake_minimum_required(VERSION 3.17)
project(pylibjpeg_turbo)

include(ExternalProject)

set(JPEG_INSTALL_DIR ${PROJECT_BINARY_DIR}/libjpeg-turbo-install)
ExternalProject_Add(libjpeg-turbo
    SOURCE_DIR
        ${PROJECT_SOURCE_DIR}/extern/libjpeg-turbo
    CMAKE_CACHE_ARGS
        -DBUILD_SHARED_LIBS:BOOL=On
        -DENABLE_SHARED:BOOL=On
        -DENABLE_STATIC:BOOL=Off
        -DCMAKE_INSTALL_PREFIX:STRING=${JPEG_INSTALL_DIR}
        -DCMAKE_INSTALL_LIBDIR:STRING=lib
        -DCMAKE_INSTALL_BINDIR:STRING=lib
        -DCMAKE_INSTALL_DOCDIR:STRING=doc
        -DCMAKE_PLATFORM_NO_VERSIONED_SONAME:BOOL=On
)
set(PY_BUILD_CMAKE_MODULE_NAME ${PROJECT_NAME} CACHE STRING "")
install(DIRECTORY ${JPEG_INSTALL_DIR}/lib
        DESTINATION ${PY_BUILD_CMAKE_MODULE_NAME}/libjpeg-turbo
        COMPONENT shlib
        FILES_MATCHING REGEX "(lib)?turbojpeg.(so|dll|dylib)$")
install(FILES ${JPEG_INSTALL_DIR}/doc/LICENSE.md
        DESTINATION ${PY_BUILD_CMAKE_MODULE_NAME}/libjpeg-turbo
        COMPONENT shlib)
