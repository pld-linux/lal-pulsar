# TODO:
# - CUDA on bcond
# - PSS (--enable-pss, BR: pss.pc, libpss+libpsssfb+libpssastro+libpssnovas)
# - SIStr (--enable-sistr, BR: gds/dtt/SIStr.h, libSIStr)
Summary:	LAL routines for pulsar and continuous wave gravitational wave data analysis
Summary(pl.UTF-8):	Procedury LAL do analizy danych fal grawitacyjnych pulsarów i fal ciągłych
Name:		lal-pulsar
Version:	6.1.0
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://software.igwn.org/lscsoft/source/lalsuite/lalpulsar-%{version}.tar.xz
# Source0-md5:	bade823b2acebeef91252784ad9c7ee2
Patch0:		lalpulsar-env.patch
Patch1:		lalpulsar-format.patch
Patch2:		lalpulsar-sse2.patch
Patch3:		lalpulsar-build.patch
URL:		https://wiki.ligo.org/Computing/LALSuite
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	cfitsio-devel
BuildRequires:	fftw3-devel >= 3
BuildRequires:	fftw3-single-devel >= 3
BuildRequires:	gsl-devel >= 1.13
BuildRequires:	help2man >= 1.37
BuildRequires:	lal-devel >= 7.5.0
BuildRequires:	lal-frame-devel >= 3.0.0
BuildRequires:	lal-inference-devel >= 4.1.0
BuildRequires:	lal-simulation-devel >= 5.4.0
BuildRequires:	libgomp-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:2
BuildRequires:	octave-devel >= 1:3.2.0
BuildRequires:	pkgconfig
BuildRequires:	python3-devel >= 1:3.5
BuildRequires:	python3-numpy-devel >= 1:1.7
BuildRequires:	swig >= 4.1.0
BuildRequires:	swig-python >= 3.0.11
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	zlib-devel
Requires:	gsl >= 1.13
Requires:	lal >= 7.5.0
Requires:	lal-frame >= 3.0.0
Requires:	lal-inference >= 4.1.0
Requires:	lal-simulation >= 5.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LAL routines for pulsar and continuous wave gravitational wave data
analysis.

%description -l pl.UTF-8
Procedury LAL do analizy danych fal grawitacyjnych pulsarów i fal
ciągłych.

%package devel
Summary:	Header files for lal-pulsar library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki lal-pulsar
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gsl-devel >= 1.13
Requires:	lal-devel >= 7.5.0
Requires:	lal-frame-devel >= 3.0.0
Requires:	lal-inference-devel >= 4.1.0
Requires:	lal-simulation-devel >= 5.4.0

%description devel
Header files for lal-pulsar library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki lal-pulsar.

%package static
Summary:	Static lal-pulsar library
Summary(pl.UTF-8):	Statyczna biblioteka lal-pulsar
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static lal-pulsar library.

%description static -l pl.UTF-8
Statyczna biblioteka lal-pulsar.

%package -n octave-lalpulsar
Summary:	Octave interface for LAL Pulsar
Summary(pl.UTF-8):	Interfejs Octave do biblioteki LAL Pulsar
Group:		Applications/Math
Requires:	%{name} = %{version}-%{release}
Requires:	octave-lal >= 7.5.0

%description -n octave-lalpulsar
Octave interface for LAL Pulsar.

%description -n octave-lalpulsar -l pl.UTF-8
Interfejs Octave do biblioteki LAL Pulsar.

%package -n python3-lalpulsar
Summary:	Python bindings for LAL Pulsar
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki LAL Pulsar
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
Requires:	python3-lal >= 7.5.0
Requires:	python3-lalframe >= 2.0.0
Requires:	python3-lalinference >= 4.1.0
Requires:	python3-lalsimulation >= 3.1.0
Requires:	python3-modules >= 1:3.5
Requires:	python3-numpy >= 1:1.7
Requires:	python3-scipy
Requires:	python3-six
# TODO: astropy h5py

%description -n python3-lalpulsar
Python bindings for LAL Pulsar.

%description -n python3-lalpulsar -l pl.UTF-8
Wiązania Pythona do biblioteki LAL Pulsar.

%prep
%setup -q -n lalpulsar-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__libtoolize}
%{__aclocal} -I gnuscripts
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--enable-swig
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/liblalpulsar.la

install -d $RPM_BUILD_ROOT/etc/shrc.d
%{__mv} $RPM_BUILD_ROOT%{_sysconfdir}/*sh $RPM_BUILD_ROOT/etc/shrc.d

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README.md
%attr(755,root,root) %{_bindir}/lalpulsar_Compute*
%attr(755,root,root) %{_bindir}/lalpulsar_CopyPublicSFTs
%attr(755,root,root) %{_bindir}/lalpulsar_DriveHoughMulti
%attr(755,root,root) %{_bindir}/lalpulsar_FstatMetric_v2
%attr(755,root,root) %{_bindir}/lalpulsar_HierarchSearchGCT
%attr(755,root,root) %{_bindir}/lalpulsar_HierarchicalSearch
%attr(755,root,root) %{_bindir}/lalpulsar_MakeSFTs
%attr(755,root,root) %{_bindir}/lalpulsar_Makefakedata_v4
%attr(755,root,root) %{_bindir}/lalpulsar_Makefakedata_v5
%attr(755,root,root) %{_bindir}/lalpulsar_PredictFstat
%attr(755,root,root) %{_bindir}/lalpulsar_PrintDetectorState
%attr(755,root,root) %{_bindir}/lalpulsar_SFTclean
%attr(755,root,root) %{_bindir}/lalpulsar_SFTvalidate
%attr(755,root,root) %{_bindir}/lalpulsar_Weave*
%attr(755,root,root) %{_bindir}/lalpulsar_WriteSFTsfromSFDBs
%attr(755,root,root) %{_bindir}/lalpulsar_compareFstats
%attr(755,root,root) %{_bindir}/lalpulsar_compareSFTs
%attr(755,root,root) %{_bindir}/lalpulsar_create_solar_system_ephemeris
%attr(755,root,root) %{_bindir}/lalpulsar_create_time_correction_ephemeris
%attr(755,root,root) %{_bindir}/lalpulsar_crosscorr_v2
%attr(755,root,root) %{_bindir}/lalpulsar_dumpSFT
%attr(755,root,root) %{_bindir}/lalpulsar_fits_*
%attr(755,root,root) %{_bindir}/lalpulsar_frequency_evolution
%attr(755,root,root) %{_bindir}/lalpulsar_heterodyne
%attr(755,root,root) %{_bindir}/lalpulsar_parameter_estimation_nested
%attr(755,root,root) %{_bindir}/lalpulsar_spec_*
%attr(755,root,root) %{_bindir}/lalpulsar_splitSFTs
%attr(755,root,root) %{_bindir}/lalpulsar_ssbtodetector
%attr(755,root,root) %{_bindir}/lalpulsar_synthesize*
%attr(755,root,root) %{_bindir}/lalpulsar_version
%attr(755,root,root) %{_libdir}/liblalpulsar.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liblalpulsar.so.29
%{_datadir}/lalpulsar
/etc/shrc.d/lalpulsar-user-env.csh
/etc/shrc.d/lalpulsar-user-env.fish
/etc/shrc.d/lalpulsar-user-env.sh
%{_mandir}/man1/lalpulsar_version.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblalpulsar.so
%{_includedir}/lal/BinaryPulsarTiming.h
%{_includedir}/lal/CWMakeFakeData.h
%{_includedir}/lal/ComputeFstat.h
%{_includedir}/lal/ComputeSky.h
%{_includedir}/lal/DetectorStates.h
%{_includedir}/lal/DopplerFullScan.h
%{_includedir}/lal/DopplerScan.h
%{_includedir}/lal/ExtrapolatePulsarSpins.h
%{_includedir}/lal/FITSFileIO.h
%{_includedir}/lal/FITSPulsarIO.h
%{_includedir}/lal/FstatisticTools.h
%{_includedir}/lal/GSLHelpers.h
%{_includedir}/lal/GeneratePulsarSignal.h
%{_includedir}/lal/GenerateSpinOrbitCW.h
%{_includedir}/lal/GenerateTaylorCW.h
%{_includedir}/lal/GetEarthTimes.h
%{_includedir}/lal/HeapToplist.h
%{_includedir}/lal/HeterodynedPulsarModel.h
%{_includedir}/lal/HoughMap.h
%{_includedir}/lal/LALBarycenter.h
%{_includedir}/lal/LALComputeAM.h
%{_includedir}/lal/LALHough.h
%{_includedir}/lal/LALInitBarycenter.h
%{_includedir}/lal/LALPulsarConfig.h
%{_includedir}/lal/LALPulsarVCSInfo.h
%{_includedir}/lal/LALPulsarVCSInfoHeader.h
%{_includedir}/lal/LFTandTSutils.h
%{_includedir}/lal/LISAspecifics.h
%{_includedir}/lal/LUT.h
%{_includedir}/lal/LatticeTiling.h
%{_includedir}/lal/LineRobustStats.h
%{_includedir}/lal/MetricUtils.h
%{_includedir}/lal/NormalizeSFTRngMed.h
%{_includedir}/lal/PHMD.h
%{_includedir}/lal/PSDutils.h
%{_includedir}/lal/ProbabilityDensity.h
%{_includedir}/lal/PtoleMetric.h
%{_includedir}/lal/PulsarCrossCorr.h
%{_includedir}/lal/PulsarCrossCorr_v2.h
%{_includedir}/lal/PulsarDataTypes.h
%{_includedir}/lal/PulsarSimulateCoherentGW.h
%{_includedir}/lal/ReadPulsarParFile.h
%{_includedir}/lal/SFTClean.h
%{_includedir}/lal/SFTReferenceLibrary.h
%{_includedir}/lal/SFTfileIO.h
%{_includedir}/lal/SFTutils.h
%{_includedir}/lal/SSBtimes.h
%{_includedir}/lal/SWIGLALPulsarTest.h
%{_includedir}/lal/SimulatePulsarSignal.h
%{_includedir}/lal/SinCosLUT.h
%{_includedir}/lal/Statistics.h
%{_includedir}/lal/SuperskyMetrics.h
%{_includedir}/lal/SynthesizeCWDraws.h
%{_includedir}/lal/TascPorbTiling.h
%{_includedir}/lal/TransientCW_utils.h
%{_includedir}/lal/TwoDMesh.h
%{_includedir}/lal/UniversalDopplerMetric.h
%{_includedir}/lal/Velocity.h
%{_includedir}/lal/SWIGLALPulsarAlpha.i
%{_includedir}/lal/SWIGLALPulsarOmega.i
%{_includedir}/lal/swiglalpulsar.i
%{_pkgconfigdir}/lalpulsar.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/liblalpulsar.a

%files -n octave-lalpulsar
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/octave/*/site/oct/*/lalpulsar.oct

%files -n python3-lalpulsar
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lalpulsar_MakeSFTDAG
%attr(755,root,root) %{_bindir}/lalpulsar_combine_crosscorr_toplists
%attr(755,root,root) %{_bindir}/lalpulsar_create_solar_system_ephemeris_python
%attr(755,root,root) %{_bindir}/lalpulsar_knope*
%attr(755,root,root) %{_bindir}/lalpulsar_run_crosscorr_v2
%dir %{py3_sitedir}/lalpulsar
%attr(755,root,root) %{py3_sitedir}/lalpulsar/_lalpulsar.so
%{py3_sitedir}/lalpulsar/*.py
%{py3_sitedir}/lalpulsar/__pycache__
