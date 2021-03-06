%{!?python2_sitelib: %define python2_sitelib %(python2 -c "from distutils.sysconfig import get_python_lib;print(get_python_lib())")}
%{!?python3_sitelib: %define python3_sitelib %(python3 -c "from distutils.sysconfig import get_python_lib;print(get_python_lib())")}

Summary:        Code coverage measurement for Python.
Name:           python-coverage
Version:        4.3.4
Release:        1%{?dist}
License:        Apache 2.0
Group:          Development/Languages/Python
Vendor:         VMware, Inc.
Distribution:   Photon
Url:            https://pypi.python.org/pypi/coverage
Source0:        https://files.pythonhosted.org/packages/source/c/coverage/coverage-%{version}.tar.gz
%define         sha1 coverage=8ffe985cb6efd4b747fd8ee75a9a41e4f319cc71

BuildRequires:  python2
BuildRequires:  python2-libs
BuildRequires:  python2-devel
BuildRequires:  python-setuptools

Requires:       python2
Requires:       python2-libs

%description
Code coverage measurement for Python.
Coverage.py measures code coverage, typically during test execution. It uses the code analysis tools and tracing hooks provided in the Python standard library to determine which lines are executable, and which have been executed.

%package -n     python3-coverage
Summary:        python-coverage
BuildRequires:  python3-devel
BuildRequires:  python3-libs

Requires:       python3
Requires:       python3-libs

%description -n python3-coverage
Python 3 version.

%prep
%setup -q -n coverage-%{version}
rm -rf ../p3dir
cp -a . ../p3dir

%build
python2 setup.py build
pushd ../p3dir
python3 setup.py build
popd

%install
python2 setup.py install --prefix=%{_prefix} --root=%{buildroot}
pushd ../p3dir
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}
popd

%check
python2 setup.py test
pushd ../p3dir
python3 setup.py test
popd

%files
%defattr(-,root,root)
%{python2_sitelib}/*

%files -n python3-coverage
%defattr(-,root,root)
%{python3_sitelib}/*
%{_bindir}/*

%changelog
*   Wed Apr 05 2017 Xiaolin Li <xiaolinl@vmware.com> 4.3.4-1
-   Initial packaging for Photon
