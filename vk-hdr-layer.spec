%global tag 0
%global date 20231001
%global commit abc123
%global longcommit abc123def456

Name:           vk-hdr-layer
Version:        %{tag}
Release:        1.%{date}git%{commit}%{?dist}
Summary:        Implements HDR vulkan extensions in Wayland compositors that support it.

# SPDX
License:        GPL-3.0-only
URL:            https://github.com/Zamundaaa/VK_hdr_layer
Source0:        https://github.com/Zamundaaa/VK_hdr_layer/archive/%{longcommit}.tar.gz

BuildRequires:       pkgconfig(x11)
BuildRequires:       pkgconfig(vulkan)
BuildRequires:       pkgconfig(wayland-client)
BuildRequires:       pkgconfig(wayland-scanner)

%description
The %{name} package contains the VK_hdr_layer Vulkan layer which implements HDR vulkan extensions in Wayland compositors that support it.

%prep
%autosetup -p1 -n %{name}-%{version}

%build

%meson
%meson_build

%install
%meson_install

%files
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/256x256/apps/*.png
%{_datadir}/%{name}/*
%{_datadir}/applications/%{name}.desktop

%changelog
%autochangelog
