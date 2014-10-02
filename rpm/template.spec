Name:           ros-hydro-nav-core
Version:        1.11.13
Release:        0%{?dist}
Summary:        ROS nav_core package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/nav_core
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-costmap-2d
Requires:       ros-hydro-geometry-msgs
Requires:       ros-hydro-std-msgs
Requires:       ros-hydro-tf
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-costmap-2d
BuildRequires:  ros-hydro-geometry-msgs
BuildRequires:  ros-hydro-std-msgs
BuildRequires:  ros-hydro-tf

%description
This package provides common interfaces for navigation specific robot actions.
Currently, this package provides the BaseGlobalPlanner, BaseLocalPlanner, and
RecoveryBehavior interfaces, which can be used to build actions that can easily
swap their planner, local controller, or recovery behavior for new versions
adhering to the same interface.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Thu Oct 02 2014 David V. Lu!! <davidvlu@gmail.com> - 1.11.13-0
- Autogenerated by Bloom

* Wed Oct 01 2014 David V. Lu!! <davidvlu@gmail.com> - 1.11.12-0
- Autogenerated by Bloom

