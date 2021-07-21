# Generated from sahara-0.0.17.gem by gem2rpm -*- rpm-spec -*-
%global gem_name sahara

Name: rubygem-%{gem_name}
Version: 0.0.17
Release: 1%{?dist}
Summary: Vagrant box creation
# Stated in README.md
License: MIT
URL: http://github.com/jedi4ever/sahara/
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel >= 1.3.6
BuildRequires: ruby
BuildArch: noarch

%description
Allows you to sandbox your vagrant.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}

%gemspec_remove_dep -g popen4
%gemspec_add_dep -g POpen4

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%{gem_libdir}
%{gem_instdir}/locales
%exclude %{gem_cache}
%{gem_spec}
%license %{gem_instdir}/README.md

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%{gem_instdir}/sahara.gemspec

%changelog
* Wed Jul 07 2021 Pavel Valena <pvalena@redhat.com> - 0.0.17-1
- Initial package
