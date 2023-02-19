# Badstore docker

BadStore.net presents a 3-tier web app with security mistakes for training, evaluation, and testing.

## Introduction
BadStore.net presents a typical three-tier web storefront application. This self-contained application was built from the ground up with typical security mistakes to serve as a platform for demonstration, security training, evaluation, and testing purposes.

## Docker image
The BadStore.net application is delivered as a docker image. The image runs the Debian latest operating system, Apache web server, a CGI (Common Gateway Interface) application, and full MySQL interaction with multiple database tables. This architecture is commonly known as LAMP (Linux, Apache, MySQL, Perl), and presents a real application environment that uses real coding methods. Rather than being a simulation, BadStore.net operates in the same way as many commercial websites, albeit with a high concentration of application security vulnerabilities.

More details about the environment are found in subsequent sections. After boot, BadStore.net acts as a network-accessible server that clients may interact with using a Web browser. This educational playground exists for you to break. And, best of all, when you reboot, everything is back to where you started! There's no need to rebuild after successful "hacks" screw everything up. So get out your browser and start enjoying the world of web application security.

<a href="https://cryptopone.com/downloads/BadStore_net_v2_1_Manual.pdf">Documentation</a>

## Installation
To run the BadStore.net application, simply pull or build the image into a docker host.
Using the Docker Hub repository:
```
docker pull jvhoof/badstore-docker
docker run -d -p 80:80 jvhoof/badstore-docker
```

For the GitHub Container repository:
```
docker pull ghcr.io/jvhoof/badstore-docker:main
docker run -d -p 80:80 ghcr.io/jvhoof/badstore-docker:main
```

## License
BadStore.net is currently available in English and Japanese language versions and was released under the terms of the GNU General Public License.
