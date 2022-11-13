Name:		texlive-tikzinclude
Version:	28715
Release:	1
Summary:	Import TikZ images from colletions
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pgf/contrib/tikzinclude
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikzinclude.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikzinclude.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikzinclude.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
