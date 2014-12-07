# revision 28715
# category Package
# catalog-ctan /graphics/pgf/contrib/tikzinclude
# catalog-date 2013-01-03 19:43:19 +0100
# catalog-license lppl1.3
# catalog-version 1.0
Name:		texlive-tikzinclude
Version:	1.0
Release:	8
Summary:	Import TikZ images from colletions
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pgf/contrib/tikzinclude
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikzinclude.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikzinclude.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikzinclude.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package addresses the problem of importing only one TikZ-
image from a file holding multiple images.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/tikzinclude/tikzinclude.sty
%doc %{_texmfdistdir}/doc/latex/tikzinclude/README
%doc %{_texmfdistdir}/doc/latex/tikzinclude/tikzinclude.pdf
#- source
%doc %{_texmfdistdir}/source/latex/tikzinclude/tikzinclude.dtx
%doc %{_texmfdistdir}/source/latex/tikzinclude/tikzinclude.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
