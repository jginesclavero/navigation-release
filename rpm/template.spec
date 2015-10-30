Name:           ros-jade-robot-pose-ekf
Version:        1.13.1
Release:        0%{?dist}
Summary:        ROS robot_pose_ekf package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/robot_pose_ekf
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jade-bfl
Requires:       ros-jade-geometry-msgs
Requires:       ros-jade-nav-msgs
Requires:       ros-jade-roscpp
Requires:       ros-jade-rostest
Requires:       ros-jade-sensor-msgs
Requires:       ros-jade-std-msgs
Requires:       ros-jade-tf
BuildRequires:  ros-jade-bfl
BuildRequires:  ros-jade-catkin >= 0.5.68
BuildRequires:  ros-jade-geometry-msgs
BuildRequires:  ros-jade-nav-msgs
BuildRequires:  ros-jade-rosbag
BuildRequires:  ros-jade-roscpp
BuildRequires:  ros-jade-rostest
BuildRequires:  ros-jade-sensor-msgs
BuildRequires:  ros-jade-std-msgs
BuildRequires:  ros-jade-tf

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
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Fri Oct 30 2015 David V. Lu!! <davidvlu@gmail.com> - 1.13.1-0
- Autogenerated by Bloom

* Tue Mar 17 2015 David V. Lu!! <davidvlu@gmail.com> - 1.13.0-0
- Autogenerated by Bloom

