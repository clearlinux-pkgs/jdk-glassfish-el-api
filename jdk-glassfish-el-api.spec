Name     : jdk-glassfish-el-api
Version  : 3.0.0
Release  : 1
URL      : http://repo.maven.apache.org/maven2/javax/el/javax.el-api/3.0.0/javax.el-api-3.0.0.jar
Source0  : http://repo.maven.apache.org/maven2/javax/el/javax.el-api/3.0.0/javax.el-api-3.0.0.jar
Source1  : http://repo.maven.apache.org/maven2/javax/el/javax.el-api/3.0.0/javax.el-api-3.0.0.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
BuildRequires : javapackages-tools
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six

%description
No detailed description available

%prep

%build

%install
mkdir -p %{buildroot}/usr/share/maven-poms
mkdir -p %{buildroot}/usr/share/maven-metadata
mkdir -p %{buildroot}/usr/share/java

mv %{SOURCE0} %{buildroot}/usr/share/java/glassfish-el-api.jar
mv %{SOURCE1} %{buildroot}/usr/share/maven-poms/glassfish-el-api.pom

# Creates metadata
python3 /usr/share/java-utils/maven_depmap.py \
-n "" \
--pom-base %{buildroot}/usr/share/maven-poms \
--jar-base %{buildroot}/usr/share/java \
%{buildroot}/usr/share/maven-metadata/glassfish-el-api.xml \
%{buildroot}/usr/share/maven-poms/glassfish-el-api.pom \
%{buildroot}/usr/share/java/glassfish-el-api.jar \

%files
%defattr(-,root,root,-)
/usr/share/maven-metadata/glassfish-el-api.xml
/usr/share/maven-poms/glassfish-el-api.pom
/usr/share/java/glassfish-el-api.jar
