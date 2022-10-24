#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-abydos
Version  : 0.5.0
Release  : 13
URL      : https://files.pythonhosted.org/packages/30/53/4d8dfccbbfe6031a2293941d718dfda7cf2e39883f915b5e3b2c057b518c/abydos-0.5.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/30/53/4d8dfccbbfe6031a2293941d718dfda7cf2e39883f915b5e3b2c057b518c/abydos-0.5.0.tar.gz
Summary  : Abydos NLP/IR library
Group    : Development/Tools
License  : GPL-3.0 GPL-3.0+
Requires: pypi-abydos-license = %{version}-%{release}
Requires: pypi-abydos-python = %{version}-%{release}
Requires: pypi-abydos-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(deprecation)
BuildRequires : pypi(numpy)

%description
======
        
        +------------------+------------------------------------------------------+
        | CI & Test Status | |travis| |circle| |azure| |semaphore| |coveralls|    |
        +------------------+------------------------------------------------------+
        | Code Quality     | |codeclimate| |scrutinizer| |codacy| |codefactor|    |
        +------------------+------------------------------------------------------+
        | Dependencies     | |requires| |snyk| |pyup| |cii|                       |
        +------------------+------------------------------------------------------+
        | Local Analysis   | |pylint| |flake8| |pydocstyle| |sloccount| |black|   |
        +------------------+------------------------------------------------------+
        | Usage            | |docs| |mybinder| |license| |sourcerank| |zenodo|    |
        +------------------+------------------------------------------------------+
        | Contribution     | |openhub| |gh-commits| |gh-issues| |gh-stars|        |
        +------------------+------------------------------------------------------+
        | PyPI             | |pypi| |pypi-dl| |pypi-ver|                          |
        +------------------+------------------------------------------------------+
        | conda-forge      | |conda| |conda-dl| |conda-platforms|                 |
        +------------------+------------------------------------------------------+

%package license
Summary: license components for the pypi-abydos package.
Group: Default

%description license
license components for the pypi-abydos package.


%package python
Summary: python components for the pypi-abydos package.
Group: Default
Requires: pypi-abydos-python3 = %{version}-%{release}

%description python
python components for the pypi-abydos package.


%package python3
Summary: python3 components for the pypi-abydos package.
Group: Default
Requires: python3-core
Provides: pypi(abydos)
Requires: pypi(deprecation)
Requires: pypi(numpy)

%description python3
python3 components for the pypi-abydos package.


%prep
%setup -q -n abydos-0.5.0
cd %{_builddir}/abydos-0.5.0
pushd ..
cp -a abydos-0.5.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656354289
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-abydos
cp %{_builddir}/abydos-0.5.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-abydos/df07b60f0574125f0136eaa0f2dbdc382bfc647b
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-abydos/df07b60f0574125f0136eaa0f2dbdc382bfc647b

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
