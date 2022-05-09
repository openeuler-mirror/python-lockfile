%global _empty_manifest_terminate_build 0
Name:		python-lockfile
Version:	0.12.2
Release:	2
Summary:	Platform-independent file locking module
License:	MIT License
URL:		http://launchpad.net/pylockfile
Source0:	https://files.pythonhosted.org/packages/17/47/72cb04a58a35ec495f96984dddb48232b551aafb95bde614605b754fe6f7/lockfile-0.12.2.tar.gz
Patch0000:      convert-to-unittest.patch
BuildArch:	noarch
BuildRequires:  python3-pbr python3-pytest

%description
The lockfile module exports a FileLock class which provides a simple API for
locking files. Unlike the Windows msvcrt.locking function, the Unix
fcntl.flock, fcntl.lockf and the deprecated posixfile module, the API is
identical across both Unix (including Linux and Mac) and Windows platforms. The
lock mechanism relies on the atomic nature of the link (on Unix) and mkdir (on
Windows) system calls.

%package -n python3-lockfile
Summary:	Platform-independent file locking module
Provides:	python-lockfile
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
%description -n python3-lockfile
The lockfile module exports a FileLock class which provides a simple API for
locking files. Unlike the Windows msvcrt.locking function, the Unix
fcntl.flock, fcntl.lockf and the deprecated posixfile module, the API is
identical across both Unix (including Linux and Mac) and Windows platforms. The
lock mechanism relies on the atomic nature of the link (on Unix) and mkdir (on
Windows) system calls.

%package help
Summary:	Development documents and examples for lockfile
Provides:	python3-lockfile-doc
%description help
Development documents and examples for lockfile

%prep
%autosetup -n lockfile-%{version} -p1
cp -r lockfile test/

%build
%py3_build

%install
%py3_install
install -d -m755 %{buildroot}/%{_pkgdocdir}
if [ -d doc ]; then cp -arf doc %{buildroot}/%{_pkgdocdir}; fi
if [ -d docs ]; then cp -arf docs %{buildroot}/%{_pkgdocdir}; fi
if [ -d example ]; then cp -arf example %{buildroot}/%{_pkgdocdir}; fi
if [ -d examples ]; then cp -arf examples %{buildroot}/%{_pkgdocdir}; fi
pushd %{buildroot}
if [ -d usr/lib ]; then
	find usr/lib -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/lib64 ]; then
	find usr/lib64 -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/bin ]; then
	find usr/bin -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/sbin ]; then
	find usr/sbin -type f -printf "/%h/%f\n" >> filelist.lst
fi
touch doclist.lst
if [ -d usr/share/man ]; then
	find usr/share/man -type f -printf "/%h/%f.gz\n" >> doclist.lst
fi
popd
mv %{buildroot}/filelist.lst .
mv %{buildroot}/doclist.lst .

%check
/usr/bin/pytest

%files -n python3-lockfile -f filelist.lst
%dir %{python3_sitelib}/*

%files help -f doclist.lst
%{_pkgdocdir}

%changelog
* Sat May 7 2022 caodongxia <caodongxia@h-partners.com> - 0.12.2-2
- Remove test dependency on python-nose during build

* Wed Aug 25 2021 Python_Bot <Python_Bot@openeuler.org>
- Package Spec generated
