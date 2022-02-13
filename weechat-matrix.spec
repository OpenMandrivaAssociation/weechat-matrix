%global debug_package %{nil}

Summary:	An extensible chat client for Matrix.
Name:		weechat-matrix
Version:	0.3.0
Release:	1
Group:		Networking/IRC
License:	MIT
URL:		https://github.com/poljar/%{name}
Source0:	https://github.com/poljar/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:	pkgconfig(python3)
BuildRequires:	python3dist(hypothesis)
BuildRequires:	python3dist(matrix-nio)
BuildRequires:	python3dist(pygments)
BuildRequires:	python3dist(pytest)
BuildRequires:	python3dist(setuptools)
BuildRequires:	python3dist(webcolors)

Requires:	pkgconfig(python3)
Requires:	python3dist(pyopenssl)
Requires:	python3dist(webcolors)
#Requires:	python3dist(future)
Requires:	python-atomicwrites
#Requires:	python3dist(attrs)
Requires:	python3dist(logbook)
Requires:	python3dist(pygments)
Requires:	python3dist(matrix-nio)
Requires:	python3dist(aiohttp)
Requires:	python3dist(file-magic)
Requires:	python3dist(requests)

%description
weechat-matrix is stable and quite usable as a daily driver. It already
supports large parts of the Matrix protocol, including end-to-end encryption
(though some features like cross-signing and session unwedging are
unimplemented).

However, due to some inherent limitations of Weechat scripts, development
has moved to weechat-matrix-rs, a Weechat plugin written in Rust. As such,
weechat-matrix is in maintenance mode and will likely not be receiving
substantial new features.

%files
%license LICENSE
%doc README.md
%{_libdir}/weechat/plugins/python/matrix.py
%dir %{_libdir}/weechat/plugins/python/matrix/
%{_libdir}/weechat/plugins/python/matrix/*

#--------------------------------------------------------------------

%prep
%autosetup

%build
# nothig to do here

%install
export WEECHAT_HOME=%{_libdir}/weechat/plugins
%make_install
