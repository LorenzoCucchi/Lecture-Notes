# P.I.G.N.A.
<div align="center">
	<img src="https://avatars2.githubusercontent.com/u/8077370?s=200&v=4" alt="Skyward" width="200"></a>
<h1>P.I.G.N.A.</h1>
<h2>Parafoil Interface Guidance Navigation Algorithm</h2>
</div>

PIGNA is a simulator, written in C++, for developing and analyzing the guidance navigation algorithms used for the parfoil. 

Building is made with Cmake in the build folder.

## Content

| Path             | Description                                                 |
| ---------------- | ----------------------------------------------------------- |
| src/             | cpp files                                                   |
| include/         | class and header definition                                 |
| libs/            | library with required dependencies                          |
| .vscode/         | vscode setup files                                          |

In the main folder you will find n the main folder you will find **CMakeLists.txt** which is used to configure the build system.

## Getting Started

### Dependencies

* CMake
* Boost Odeint library is included in the libs folder
* Eigen is included in the libs folder

### Cloning the repo

Clone this repo with the `--recursive` option.
```sh
git clone --recursive git@git.skywarder.eu:avn/gnc/pigna.git
cd pigna
```
## Building

You can use directly CMake:
```sh
mkdir build
cd build
cmake ..
make
```

