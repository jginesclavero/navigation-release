Name:           ros-indigo-robot-pose-ekf
Version:        1.12.7
Release:        0%{?dist}
Summary:        ROS robot_pose_ekf package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/robot_pose_ekf
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-bfl
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-nav-msgs
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-rostest
Requires:       ros-indigo-sensor-msgs
Requires:       ros-indigo-std-msgs
Requires:       ros-indigo-tf
BuildRequires:  ros-indigo-bfl
BuildRequires:  ros-indigo-catkin >= 0.5.68
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-nav-msgs
BuildRequires:  ros-indigo-rosbag
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-rostest
BuildRequires:  ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-std-msgs
BuildRequires:  ros-indigo-tf

%description
The Robot Pose EKF package is used to estimate the 3D pose of a robot, based on
(partial) pose measurements coming from different sources. It uses an extended
Kalman filter with a 6D model (3D position and 3D orientation) to combine
measurements from wheel odometry, IMU sensor and visual odometry. The basic idea
is to offer loosely coupled integration with different sensors, where sensor
signals are received as ROS messages.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Sat Feb 06 2016 David V. Lu!! <davidvlu@gmail.com> - 1.12.7-0
- Autogenerated by Bloom

* Sat Jan 02 2016 David V. Lu!! <davidvlu@gmail.com> - 1.12.6-0
- Autogenerated by Bloom

* Fri Oct 30 2015 David V. Lu!! <davidvlu@gmail.com> - 1.12.5-0
- Autogenerated by Bloom

* Wed Jun 03 2015 David V. Lu!! <davidvlu@gmail.com> - 1.12.4-0
- Autogenerated by Bloom

* Thu Apr 30 2015 David V. Lu!! <davidvlu@gmail.com> - 1.12.3-0
- Autogenerated by Bloom

* Tue Mar 31 2015 David V. Lu!! <davidvlu@gmail.com> - 1.12.2-0
- Autogenerated by Bloom

* Sat Mar 14 2015 David V. Lu!! <davidvlu@gmail.com> - 1.12.1-0
- Autogenerated by Bloom

* Wed Feb 04 2015 David V. Lu!! <davidvlu@gmail.com> - 1.12.0-0
- Autogenerated by Bloom

