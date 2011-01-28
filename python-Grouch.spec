
%define 	module	Grouch

Summary:	System for describing and enforcing a Python object schema
Summary(pl.UTF-8):	System opisu i wymuszania schematu obiektów Pythona
Name:		python-%{module}
Version:	0.4
Release:	3
License:	CNRI
Group:		Libraries/Python
Source0:	http://www.mems-exchange.org/software/files/grouch/%{module}-%{version}.tar.gz
# Source0-md5:	02d4894bff29a5c862ddf959fd0da16e
URL:		http://www.mems-exchange.org/software/grouch/
BuildRequires:	python-devel >= 1:2.3
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
Requires:	python >= 2.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Grouch is a system for describing and enforcing a Python object
schema. An object schema describes every class in a collection of
objects -- in particular, it specifies the type of every instance
attribute of every class. Grouch includes a type language for
specifying attribute types, a tool to parse specially-formatted class
docstrings and output a complete object schema, and another tool for
walking a persistent object graph and ensuring that every scrap of
data in it conforms to the object schema extracted from your class
docstrings. The API for defining, querying, and enforcing types is
fairly complete and well-documented, so you can use Grouch's type
system in other ways as well.

%description -l pl.UTF-8
Grouch jest systemem opisu i wymuszania zachowania schematu obiektów
Pythona. Schemat obiektów opisuje każdą klasę kolekcji obiektów - w
szczególności specyfikuje typ każdej instancji atrybutu każdej z klas.
Grouch zawiera język typów umożliwiający specyfikowanie typów
atrybutów. Zawiera też narzędzie pozwalające na parsowanie odpowiednio
sformatowanych łańcuchów dokumentujących oraz utworzenie kompletnego
schematu obiektów. W skład Grouch wchodzi też narzędzie potrafiące
przeanalizować stały graf obiektów w celu stwierdzenia, czy każdy
element danych jest zgodny ze schematem danych wyekstrahowanym z
łańcuchów dokumentujących w klasach. API umożliwiające definiowanie,
odpytywanie oraz utrzymywanie typów jest kompletne i dobrze
udokumentowane, system typów Groucha może więc być użyty do innych
celów.

%package doc
Summary:	Documentation for Grouch module
Summary(pl.UTF-8):	Dokumentacja do modułu Grouch
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description doc
This package contains documentation files for Grouch Python module.

%description doc -l pl.UTF-8
Pakiet zawierający dokumentację dla modułu Pythona Grouch.

%package examples
Summary:	Examples for Grouch module
Summary(pl.UTF-8):	Przykłady do modułu Grouch
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description examples
This package contains example files for Grouch Python module.

%description examples -l pl.UTF-8
Pakiet zawierający przykładowe skrypty dla modułu Pythona Grouch.

%package utils
Summary:	Utils for Grouch module
Summary(pl.UTF-8):	Narzędzia do modułu Grouch
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description utils
This package contains utility files for Grouch Python module.

%description utils -l pl.UTF-8
Pakiet zawierający programy narzędziowe dla modułu Pythona Grouch.

%prep
%setup -q -n %{module}-%{version}

%build
python setup.py build_ext

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{py_sitescriptdir},%{_examplesdir}/%{name}-%{version},%{_bindir}}

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--install-lib=%{py_sitescriptdir} \
	--optimize=2

find $RPM_BUILD_ROOT%{py_sitescriptdir} -name \*.py -exec rm {} \;

cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.txt README.txt
%{py_sitescriptdir}/grouch

%files doc
%defattr(644,root,root,755)
%doc doc/*

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
