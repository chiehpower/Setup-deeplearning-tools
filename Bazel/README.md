# Build Bazel from scratch on AGX Jetson device

[![](https://img.shields.io/badge/Bazel-v3.4.0-blue)](./) [![](https://img.shields.io/badge/JetPack-v4.4-lightgrey)](https://developer.nvidia.com/embedded/jetpack) [![](https://img.shields.io/badge/CUDA-v10.2-red)](https://developer.nvidia.com/cuda-10.2-download-archive) [![](https://img.shields.io/badge/TensorRT-v7.1.0.16-orange)](https://developer.nvidia.com/nvidia-tensorrt-7x-download)

- My steps are referred from [here](https://jkjung-avt.github.io/build-tensorflow-1.8.0/)
- Download bazel versions from [here](https://github.com/bazelbuild/bazel/releases)

## Whole Steps:

```
wget https://github.com/bazelbuild/bazel/releases/download/3.4.0/bazel-3.4.0-dist.zip
mkdir -p ~/src 
cd ~/src
unzip ~/ssd256/github/bazel-3.4.0-dist.zip -d bazel-3.4.0-dist   
cd bazel-3.4.0-dist 
./compile.sh
```

Output: 
`Build successful! Binary is here: /home/nvidia/src/bazel-3.4.0-dist/output/bazel
`

▍Copy the executive file to /bin fodler

```
sudo cp output/bazel /usr/local/bin
```

▍Check the bazel

```
bazel help
```

Output:
```
Extracting Bazel installation...
Starting local Bazel server and connecting to it...
                                               [bazel release 3.4.0- (@non-git)]
Usage: bazel <command> <options> ...

Available commands:
  analyze-profile     Analyzes build profile data.
  aquery              Analyzes the given targets and queries the action graph.
  build               Builds the specified targets.
  canonicalize-flags  Canonicalizes a list of bazel options.
  clean               Removes output files and optionally stops the server.
  coverage            Generates code coverage report for specified test targets.
  cquery              Loads, analyzes, and queries the specified targets w/ configurations.
  dump                Dumps the internal state of the bazel server process.
  fetch               Fetches external repositories that are prerequisites to the targets.
  help                Prints help for commands, or the index.
  info                Displays runtime info about the bazel server.
  license             Prints the license of this software.
  mobile-install      Installs targets to mobile devices.
  print_action        Prints the command line args for compiling a file.
  query               Executes a dependency graph query.
  run                 Runs the specified target.
  shutdown            Stops the bazel server.
  sync                Syncs all repositories specified in the workspace file
  test                Builds and runs the specified test targets.
  version             Prints version information for bazel.

Getting more help:
  bazel help <command>
                   Prints help and options for <command>.
  bazel help startup_options
                   Options for the JVM hosting bazel.
  bazel help target-syntax
                   Explains the syntax for specifying targets.
  bazel help info-keys
                   Displays a list of keys used by the info command.
```

Then done.