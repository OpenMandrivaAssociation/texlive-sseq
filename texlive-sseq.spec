Name:		texlive-sseq
Version:	31585
Release:	2
Summary:	Typesetting spectral sequence charts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/sseq
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sseq.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sseq.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sseq.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides commands to draw spectral sequence
diagrams, providing facilities for clipping and arranging
multiple symbols so that they do not overlap. The package is
built using pgf, and shares that systems large demands for TeX
system memory. Its geometric commands are based on a turtle
graphics model, and control structures such as loops and
conditionals are available.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/sseq/sseq.sty
%doc %{_texmfdistdir}/doc/latex/sseq/sseq.pdf
#- source
%doc %{_texmfdistdir}/source/latex/sseq/sseq.dtx
%doc %{_texmfdistdir}/source/latex/sseq/sseq.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
