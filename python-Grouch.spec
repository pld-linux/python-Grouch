# $Revision: 1.5 $ $Date: 2004-08-02 05:44:37 $

%define 	module	Grouch

Summary:	System for describing and enforcing a Python object schema
Summary(pl):	System opisu i wymuszania schematu obiektów Pythona
Name:		python-%{module}
Version:	0.3
Release:	1
License:	CNRI
Group:		Libraries/Python
Source0:	http://www.mems-exchange.org/software/files/grouch/%{module}-%{version}.tar.gz
# Source0-md5:	37d970a0bb13dcb7c764624fc8bffe93
URL:		http://www.mems-exchange.org/software/grouch/
BuildRequires:	python-devel >= 2.3
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

%description -l pl
Grouch jest systemem opisu i wymuszania zachowania schematu obiektów
Pythona. Schemat obiektów opisuje ka¿d± klasê kolekcji obiektów - w
szczególno¶ci specyfikuje typ ka¿dej instancji atrybutu ka¿dej z klas.
Grouch zawiera jêzyk typów umo¿liwiaj±cy specyfikowanie typów
atrybutów. Zawiera te¿ narzêdzie pozwalaj±ce na parsowanie odpowiednio
sformatowanych ³añcuchów dokumentuj±cych oraz utworzenie kompletnego
schematu obiektów. W sk³ad Grouch wchodzi te¿ narzêdzie potrafi±ce
przeanalizowaæ sta³y graf obiektów w celu stwierdzenia, czy ka¿dy
element danych jest zgodny ze schematem danych wyekstrahowanym z
³añcuchów dokumentuj±cych w klasach. API umo¿liwij±ce definiowanie,
odpytywanie oraz utrzymywanie typów jest kompletne i dobrze
udokumentowane, system typów Groucha mo¿e wiêc byæ u¿yty do innych
celów.

%package doc
Summary:	Documentation for Grouch module
Summary(pl):	Dokumentacja do modu³u Grouch
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description doc
This package contains documentation files for Grouch Python module.

%description doc -l pl
Pakiet zawieraj±cy dokumentacjê dla modu³u Pythona Grouch.

%package examples
Summary:	Examples for Grouch module
Summary(pl):	Przyk³ady do modu³u Grouch
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description examples
This package contains example files for Grouch Python module.

%description examples -l pl
Pakiet zawieraj±cy przyk³adowe skrypty dla modu³u Pythona Grouch.

%package utils
Summary:	Utils for Grouch module
Summary(pl):	Narzêdzia do modu³u Grouch
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description utils
This package contains utility files for Grouch Python module.

%description utils -l pl
Pakiet zawieraj±cy programy narzêdziowe dla modu³u Pythona Grouch.

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
