********************************************************************************
          Please use a simple string containing a SPDX expression for `project.license`. You can also use `project.license-files`. (Both options available on setuptools>=77.0.0).
  
          By 2026-Feb-18, you need to update your project and remove deprecated calls
          or your builds will no longer be supported.
  
          See https://packaging.python.org/en/latest/guides/writing-pyproject-toml/#license for details.
          ********************************************************************************
  
  !!
    corresp(dist, value, root_dir)
  /private/var/folders/5r/7scst4zn1gd_2n5qw4fcl9xc0000gn/T/pip-build-env-0s7wsxk0/overlay/lib/python3.14/site-packages/setuptools/config/_apply_pyprojecttoml.py:61: SetuptoolsDeprecationWarning: License classifiers are deprecated.
  !!
  
          ********************************************************************************
          Please consider removing the following classifiers in favor of a SPDX license expression:
  
          License :: OSI Approved :: Apache Software License
  
          See https://packaging.python.org/en/latest/guides/writing-pyproject-toml/#license for details.
          ********************************************************************************
  
  !!
    dist._finalize_license_expression()
  /private/var/folders/5r/7scst4zn1gd_2n5qw4fcl9xc0000gn/T/pip-build-env-0s7wsxk0/overlay/lib/python3.14/site-packages/setuptools/dist.py:483: SetuptoolsDeprecationWarning: Pattern '../LICENSE.txt' cannot contain '..'
  !!
  
          ********************************************************************************
          Please ensure the files specified are contained by the root
          of the Python package (normally marked by `pyproject.toml`).
  
          By 2026-Mar-20, you need to update your project and remove deprecated calls
          or your builds will no longer be supported.
  
          See https://packaging.python.org/en/latest/specifications/glob-patterns/ for details.
          ********************************************************************************
  
  !!
    for path in sorted(cls._find_pattern(pattern, enforce_match))
  /private/var/folders/5r/7scst4zn1gd_2n5qw4fcl9xc0000gn/T/pip-build-env-0s7wsxk0/overlay/lib/python3.14/site-packages/setuptools/dist.py:483: SetuptoolsDeprecationWarning: Cannot find any files for the given pattern.
  !!
  
          ********************************************************************************
          Pattern '../LICENSE.txt' did not match any files.
  
          By 2026-Mar-20, you need to update your project and remove deprecated calls
          or your builds will no longer be supported.
          ********************************************************************************
  
  !!
    for path in sorted(cls._find_pattern(pattern, enforce_match))
  /private/var/folders/5r/7scst4zn1gd_2n5qw4fcl9xc0000gn/T/pip-build-env-0s7wsxk0/overlay/lib/python3.14/site-packages/setuptools/dist.py:483: SetuptoolsDeprecationWarning: Pattern '../NOTICE.txt' cannot contain '..'
  !!
  
          ********************************************************************************
          Please ensure the files specified are contained by the root
          of the Python package (normally marked by `pyproject.toml`).
  
          By 2026-Mar-20, you need to update your project and remove deprecated calls
          or your builds will no longer be supported.
  
          See https://packaging.python.org/en/latest/specifications/glob-patterns/ for details.
          ********************************************************************************
  
  !!
    for path in sorted(cls._find_pattern(pattern, enforce_match))
  /private/var/folders/5r/7scst4zn1gd_2n5qw4fcl9xc0000gn/T/pip-build-env-0s7wsxk0/overlay/lib/python3.14/site-packages/setuptools/dist.py:483: SetuptoolsDeprecationWarning: Cannot find any files for the given pattern.
  !!
  
          ********************************************************************************
          Pattern '../NOTICE.txt' did not match any files.
  
          By 2026-Mar-20, you need to update your project and remove deprecated calls
          or your builds will no longer be supported.
          ********************************************************************************
  
  !!
    for path in sorted(cls._find_pattern(pattern, enforce_match))
  /private/var/folders/5r/7scst4zn1gd_2n5qw4fcl9xc0000gn/T/pip-build-env-0s7wsxk0/overlay/lib/python3.14/site-packages/setuptools/dist.py:759: SetuptoolsDeprecationWarning: License classifiers are deprecated.
  !!
  
          ********************************************************************************
          Please consider removing the following classifiers in favor of a SPDX license expression:
  
          License :: OSI Approved :: Apache Software License
  
          See https://packaging.python.org/en/latest/guides/writing-pyproject-toml/#license for details.
          ********************************************************************************
  
  !!
    self._finalize_license_expression()
  running bdist_wheel
  running build
  running build_py
  creating build/lib.macosx-10.15-universal2-cpython-314/pyarrow
  copying pyarrow/orc.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow
  copying pyarrow/conftest.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow
  copying pyarrow/_generated_version.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow
  copying pyarrow/benchmark.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow
  copying pyarrow/_compute_docstrings.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow
  copying pyarrow/ipc.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow
  copying pyarrow/util.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow
  copying pyarrow/flight.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow
  copying pyarrow/cffi.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow
  copying pyarrow/substrait.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow
  copying pyarrow/__init__.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow
  copying pyarrow/types.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow
  copying pyarrow/dataset.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow
  copying pyarrow/cuda.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow
  copying pyarrow/feather.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow
  copying pyarrow/pandas_compat.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow
  copying pyarrow/fs.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow
  copying pyarrow/acero.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow
  copying pyarrow/csv.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow
  copying pyarrow/jvm.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow
  copying pyarrow/json.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow
  copying pyarrow/compute.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow
  running egg_info
  writing pyarrow.egg-info/PKG-INFO
  writing dependency_links to pyarrow.egg-info/dependency_links.txt
  writing requirements to pyarrow.egg-info/requires.txt
  writing top-level names to pyarrow.egg-info/top_level.txt
  listing git files failed - pretending there aren't any
  reading manifest file 'pyarrow.egg-info/SOURCES.txt'
  reading manifest template 'MANIFEST.in'
  warning: no files found matching '../LICENSE.txt'
  warning: no files found matching '../NOTICE.txt'
  warning: no previously-included files matching '*.so' found anywhere in distribution
  warning: no previously-included files matching '*.pyc' found anywhere in distribution
  warning: no previously-included files matching '*~' found anywhere in distribution
  warning: no previously-included files matching '#*' found anywhere in distribution
  warning: no previously-included files matching '.git*' found anywhere in distribution
  warning: no previously-included files matching '.DS_Store' found anywhere in distribution
  no previously-included directories found matching '.asv'
  writing manifest file 'pyarrow.egg-info/SOURCES.txt'
  /private/var/folders/5r/7scst4zn1gd_2n5qw4fcl9xc0000gn/T/pip-build-env-0s7wsxk0/overlay/lib/python3.14/site-packages/setuptools/command/build_py.py:212: _Warning: Package 'pyarrow.includes' is absent from the `packages` configuration.
  !!
  
          ********************************************************************************
          ############################
          # Package would be ignored #
          ############################
          Python recognizes 'pyarrow.includes' as an importable package[^1],
          but it is absent from setuptools' `packages` configuration.
  
          This leads to an ambiguous overall configuration. If you want to distribute this
          package, please make sure that 'pyarrow.includes' is explicitly added
          to the `packages` configuration field.
  
          Alternatively, you can also rely on setuptools' discovery methods
          (for example by using `find_namespace_packages(...)`/`find_namespace:`
          instead of `find_packages(...)`/`find:`).
  
          You can read more about "package discovery" on setuptools documentation page:
  
          - https://setuptools.pypa.io/en/latest/userguide/package_discovery.html
  
          If you don't want 'pyarrow.includes' to be distributed and are
          already explicitly excluding 'pyarrow.includes' via
          `find_namespace_packages(...)/find_namespace` or `find_packages(...)/find`,
          you can try to use `exclude_package_data`, or `include-package-data=False` in
          combination with a more fine grained `package-data` configuration.
  
          You can read more about "package data files" on setuptools documentation page:
  
          - https://setuptools.pypa.io/en/latest/userguide/datafiles.html
  
  
          [^1]: For Python, any directory (with suitable naming) can be imported,
                even if it does not contain any `.py` files.
                On the other hand, currently there is no concept of package data
                directory, all directories are treated like packages.
          ********************************************************************************
  
  !!
    check.warn(importable)
  /private/var/folders/5r/7scst4zn1gd_2n5qw4fcl9xc0000gn/T/pip-build-env-0s7wsxk0/overlay/lib/python3.14/site-packages/setuptools/command/build_py.py:212: _Warning: Package 'pyarrow.interchange' is absent from the `packages` configuration.
  !!
  
          ********************************************************************************
          ############################
          # Package would be ignored #
          ############################
          Python recognizes 'pyarrow.interchange' as an importable package[^1],
          but it is absent from setuptools' `packages` configuration.
  
          This leads to an ambiguous overall configuration. If you want to distribute this
          package, please make sure that 'pyarrow.interchange' is explicitly added
          to the `packages` configuration field.
  
          Alternatively, you can also rely on setuptools' discovery methods
          (for example by using `find_namespace_packages(...)`/`find_namespace:`
          instead of `find_packages(...)`/`find:`).
  
          You can read more about "package discovery" on setuptools documentation page:
  
          - https://setuptools.pypa.io/en/latest/userguide/package_discovery.html
  
          If you don't want 'pyarrow.interchange' to be distributed and are
          already explicitly excluding 'pyarrow.interchange' via
          `find_namespace_packages(...)/find_namespace` or `find_packages(...)/find`,
          you can try to use `exclude_package_data`, or `include-package-data=False` in
          combination with a more fine grained `package-data` configuration.
  
          You can read more about "package data files" on setuptools documentation page:
  
          - https://setuptools.pypa.io/en/latest/userguide/datafiles.html
  
  
          [^1]: For Python, any directory (with suitable naming) can be imported,
                even if it does not contain any `.py` files.
                On the other hand, currently there is no concept of package data
                directory, all directories are treated like packages.
          ********************************************************************************
  
  !!
    check.warn(importable)
  /private/var/folders/5r/7scst4zn1gd_2n5qw4fcl9xc0000gn/T/pip-build-env-0s7wsxk0/overlay/lib/python3.14/site-packages/setuptools/command/build_py.py:212: _Warning: Package 'pyarrow.parquet' is absent from the `packages` configuration.
  !!
  
          ********************************************************************************
          ############################
          # Package would be ignored #
          ############################
          Python recognizes 'pyarrow.parquet' as an importable package[^1],
          but it is absent from setuptools' `packages` configuration.
  
          This leads to an ambiguous overall configuration. If you want to distribute this
          package, please make sure that 'pyarrow.parquet' is explicitly added
          to the `packages` configuration field.
  
          Alternatively, you can also rely on setuptools' discovery methods
          (for example by using `find_namespace_packages(...)`/`find_namespace:`
          instead of `find_packages(...)`/`find:`).
  
          You can read more about "package discovery" on setuptools documentation page:
  
          - https://setuptools.pypa.io/en/latest/userguide/package_discovery.html
  
          If you don't want 'pyarrow.parquet' to be distributed and are
          already explicitly excluding 'pyarrow.parquet' via
          `find_namespace_packages(...)/find_namespace` or `find_packages(...)/find`,
          you can try to use `exclude_package_data`, or `include-package-data=False` in
          combination with a more fine grained `package-data` configuration.
  
          You can read more about "package data files" on setuptools documentation page:
  
          - https://setuptools.pypa.io/en/latest/userguide/datafiles.html
  
  
          [^1]: For Python, any directory (with suitable naming) can be imported,
                even if it does not contain any `.py` files.
                On the other hand, currently there is no concept of package data
                directory, all directories are treated like packages.
          ********************************************************************************
  
  !!
    check.warn(importable)
  /private/var/folders/5r/7scst4zn1gd_2n5qw4fcl9xc0000gn/T/pip-build-env-0s7wsxk0/overlay/lib/python3.14/site-packages/setuptools/command/build_py.py:212: _Warning: Package 'pyarrow.src.arrow.python' is absent from the `packages` configuration.
  !!
  
          ********************************************************************************
          ############################
          # Package would be ignored #
          ############################
          Python recognizes 'pyarrow.src.arrow.python' as an importable package[^1],
          but it is absent from setuptools' `packages` configuration.
  
          This leads to an ambiguous overall configuration. If you want to distribute this
          package, please make sure that 'pyarrow.src.arrow.python' is explicitly added
          to the `packages` configuration field.
  
          Alternatively, you can also rely on setuptools' discovery methods
          (for example by using `find_namespace_packages(...)`/`find_namespace:`
          instead of `find_packages(...)`/`find:`).
  
          You can read more about "package discovery" on setuptools documentation page:
  
          - https://setuptools.pypa.io/en/latest/userguide/package_discovery.html
  
          If you don't want 'pyarrow.src.arrow.python' to be distributed and are
          already explicitly excluding 'pyarrow.src.arrow.python' via
          `find_namespace_packages(...)/find_namespace` or `find_packages(...)/find`,
          you can try to use `exclude_package_data`, or `include-package-data=False` in
          combination with a more fine grained `package-data` configuration.
  
          You can read more about "package data files" on setuptools documentation page:
  
          - https://setuptools.pypa.io/en/latest/userguide/datafiles.html
  
  
          [^1]: For Python, any directory (with suitable naming) can be imported,
                even if it does not contain any `.py` files.
                On the other hand, currently there is no concept of package data
                directory, all directories are treated like packages.
          ********************************************************************************
  
  !!
    check.warn(importable)
  /private/var/folders/5r/7scst4zn1gd_2n5qw4fcl9xc0000gn/T/pip-build-env-0s7wsxk0/overlay/lib/python3.14/site-packages/setuptools/command/build_py.py:212: _Warning: Package 'pyarrow.src.arrow.python.vendored' is absent from the `packages` configuration.
  !!
  
          ********************************************************************************
          ############################
          # Package would be ignored #
          ############################
          Python recognizes 'pyarrow.src.arrow.python.vendored' as an importable package[^1],
          but it is absent from setuptools' `packages` configuration.
  
          This leads to an ambiguous overall configuration. If you want to distribute this
          package, please make sure that 'pyarrow.src.arrow.python.vendored' is explicitly added
          to the `packages` configuration field.
  
          Alternatively, you can also rely on setuptools' discovery methods
          (for example by using `find_namespace_packages(...)`/`find_namespace:`
          instead of `find_packages(...)`/`find:`).
  
          You can read more about "package discovery" on setuptools documentation page:
  
          - https://setuptools.pypa.io/en/latest/userguide/package_discovery.html
  
          If you don't want 'pyarrow.src.arrow.python.vendored' to be distributed and are
          already explicitly excluding 'pyarrow.src.arrow.python.vendored' via
          `find_namespace_packages(...)/find_namespace` or `find_packages(...)/find`,
          you can try to use `exclude_package_data`, or `include-package-data=False` in
          combination with a more fine grained `package-data` configuration.
  
          You can read more about "package data files" on setuptools documentation page:
  
          - https://setuptools.pypa.io/en/latest/userguide/datafiles.html
  
  
          [^1]: For Python, any directory (with suitable naming) can be imported,
                even if it does not contain any `.py` files.
                On the other hand, currently there is no concept of package data
                directory, all directories are treated like packages.
          ********************************************************************************
  
  !!
    check.warn(importable)
  /private/var/folders/5r/7scst4zn1gd_2n5qw4fcl9xc0000gn/T/pip-build-env-0s7wsxk0/overlay/lib/python3.14/site-packages/setuptools/command/build_py.py:212: _Warning: Package 'pyarrow.tests' is absent from the `packages` configuration.
  !!
  
          ********************************************************************************
          ############################
          # Package would be ignored #
          ############################
          Python recognizes 'pyarrow.tests' as an importable package[^1],
          but it is absent from setuptools' `packages` configuration.
  
          This leads to an ambiguous overall configuration. If you want to distribute this
          package, please make sure that 'pyarrow.tests' is explicitly added
          to the `packages` configuration field.
  
          Alternatively, you can also rely on setuptools' discovery methods
          (for example by using `find_namespace_packages(...)`/`find_namespace:`
          instead of `find_packages(...)`/`find:`).
  
          You can read more about "package discovery" on setuptools documentation page:
  
          - https://setuptools.pypa.io/en/latest/userguide/package_discovery.html
  
          If you don't want 'pyarrow.tests' to be distributed and are
          already explicitly excluding 'pyarrow.tests' via
          `find_namespace_packages(...)/find_namespace` or `find_packages(...)/find`,
          you can try to use `exclude_package_data`, or `include-package-data=False` in
          combination with a more fine grained `package-data` configuration.
  
          You can read more about "package data files" on setuptools documentation page:
  
          - https://setuptools.pypa.io/en/latest/userguide/datafiles.html
  
  
          [^1]: For Python, any directory (with suitable naming) can be imported,
                even if it does not contain any `.py` files.
                On the other hand, currently there is no concept of package data
                directory, all directories are treated like packages.
          ********************************************************************************
  
  !!
    check.warn(importable)
  /private/var/folders/5r/7scst4zn1gd_2n5qw4fcl9xc0000gn/T/pip-build-env-0s7wsxk0/overlay/lib/python3.14/site-packages/setuptools/command/build_py.py:212: _Warning: Package 'pyarrow.tests.data.feather' is absent from the `packages` configuration.
  !!
  
          ********************************************************************************
          ############################
          # Package would be ignored #
          ############################
          Python recognizes 'pyarrow.tests.data.feather' as an importable package[^1],
          but it is absent from setuptools' `packages` configuration.
  
          This leads to an ambiguous overall configuration. If you want to distribute this
          package, please make sure that 'pyarrow.tests.data.feather' is explicitly added
          to the `packages` configuration field.
  
          Alternatively, you can also rely on setuptools' discovery methods
          (for example by using `find_namespace_packages(...)`/`find_namespace:`
          instead of `find_packages(...)`/`find:`).
  
          You can read more about "package discovery" on setuptools documentation page:
  
          - https://setuptools.pypa.io/en/latest/userguide/package_discovery.html
  
          If you don't want 'pyarrow.tests.data.feather' to be distributed and are
          already explicitly excluding 'pyarrow.tests.data.feather' via
          `find_namespace_packages(...)/find_namespace` or `find_packages(...)/find`,
          you can try to use `exclude_package_data`, or `include-package-data=False` in
          combination with a more fine grained `package-data` configuration.
  
          You can read more about "package data files" on setuptools documentation page:
  
          - https://setuptools.pypa.io/en/latest/userguide/datafiles.html
  
  
          [^1]: For Python, any directory (with suitable naming) can be imported,
                even if it does not contain any `.py` files.
                On the other hand, currently there is no concept of package data
                directory, all directories are treated like packages.
          ********************************************************************************
  
  !!
    check.warn(importable)
  /private/var/folders/5r/7scst4zn1gd_2n5qw4fcl9xc0000gn/T/pip-build-env-0s7wsxk0/overlay/lib/python3.14/site-packages/setuptools/command/build_py.py:212: _Warning: Package 'pyarrow.tests.data.orc' is absent from the `packages` configuration.
  !!
  
          ********************************************************************************
          ############################
          # Package would be ignored #
          ############################
          Python recognizes 'pyarrow.tests.data.orc' as an importable package[^1],
          but it is absent from setuptools' `packages` configuration.
  
          This leads to an ambiguous overall configuration. If you want to distribute this
          package, please make sure that 'pyarrow.tests.data.orc' is explicitly added
          to the `packages` configuration field.
  
          Alternatively, you can also rely on setuptools' discovery methods
          (for example by using `find_namespace_packages(...)`/`find_namespace:`
          instead of `find_packages(...)`/`find:`).
  
          You can read more about "package discovery" on setuptools documentation page:
  
          - https://setuptools.pypa.io/en/latest/userguide/package_discovery.html
  
          If you don't want 'pyarrow.tests.data.orc' to be distributed and are
          already explicitly excluding 'pyarrow.tests.data.orc' via
          `find_namespace_packages(...)/find_namespace` or `find_packages(...)/find`,
          you can try to use `exclude_package_data`, or `include-package-data=False` in
          combination with a more fine grained `package-data` configuration.
  
          You can read more about "package data files" on setuptools documentation page:
  
          - https://setuptools.pypa.io/en/latest/userguide/datafiles.html
  
  
          [^1]: For Python, any directory (with suitable naming) can be imported,
                even if it does not contain any `.py` files.
                On the other hand, currently there is no concept of package data
                directory, all directories are treated like packages.
          ********************************************************************************
  
  !!
    check.warn(importable)
  /private/var/folders/5r/7scst4zn1gd_2n5qw4fcl9xc0000gn/T/pip-build-env-0s7wsxk0/overlay/lib/python3.14/site-packages/setuptools/command/build_py.py:212: _Warning: Package 'pyarrow.tests.data.parquet' is absent from the `packages` configuration.
  !!
  
          ********************************************************************************
          ############################
          # Package would be ignored #
          ############################
          Python recognizes 'pyarrow.tests.data.parquet' as an importable package[^1],
          but it is absent from setuptools' `packages` configuration.
  
          This leads to an ambiguous overall configuration. If you want to distribute this
          package, please make sure that 'pyarrow.tests.data.parquet' is explicitly added
          to the `packages` configuration field.
  
          Alternatively, you can also rely on setuptools' discovery methods
          (for example by using `find_namespace_packages(...)`/`find_namespace:`
          instead of `find_packages(...)`/`find:`).
  
          You can read more about "package discovery" on setuptools documentation page:
  
          - https://setuptools.pypa.io/en/latest/userguide/package_discovery.html
  
          If you don't want 'pyarrow.tests.data.parquet' to be distributed and are
          already explicitly excluding 'pyarrow.tests.data.parquet' via
          `find_namespace_packages(...)/find_namespace` or `find_packages(...)/find`,
          you can try to use `exclude_package_data`, or `include-package-data=False` in
          combination with a more fine grained `package-data` configuration.
  
          You can read more about "package data files" on setuptools documentation page:
  
          - https://setuptools.pypa.io/en/latest/userguide/datafiles.html
  
  
          [^1]: For Python, any directory (with suitable naming) can be imported,
                even if it does not contain any `.py` files.
                On the other hand, currently there is no concept of package data
                directory, all directories are treated like packages.
          ********************************************************************************
  
  !!
    check.warn(importable)
  /private/var/folders/5r/7scst4zn1gd_2n5qw4fcl9xc0000gn/T/pip-build-env-0s7wsxk0/overlay/lib/python3.14/site-packages/setuptools/command/build_py.py:212: _Warning: Package 'pyarrow.tests.interchange' is absent from the `packages` configuration.
  !!
  
          ********************************************************************************
          ############################
          # Package would be ignored #
          ############################
          Python recognizes 'pyarrow.tests.interchange' as an importable package[^1],
          but it is absent from setuptools' `packages` configuration.
  
          This leads to an ambiguous overall configuration. If you want to distribute this
          package, please make sure that 'pyarrow.tests.interchange' is explicitly added
          to the `packages` configuration field.
  
          Alternatively, you can also rely on setuptools' discovery methods
          (for example by using `find_namespace_packages(...)`/`find_namespace:`
          instead of `find_packages(...)`/`find:`).
  
          You can read more about "package discovery" on setuptools documentation page:
  
          - https://setuptools.pypa.io/en/latest/userguide/package_discovery.html
  
          If you don't want 'pyarrow.tests.interchange' to be distributed and are
          already explicitly excluding 'pyarrow.tests.interchange' via
          `find_namespace_packages(...)/find_namespace` or `find_packages(...)/find`,
          you can try to use `exclude_package_data`, or `include-package-data=False` in
          combination with a more fine grained `package-data` configuration.
  
          You can read more about "package data files" on setuptools documentation page:
  
          - https://setuptools.pypa.io/en/latest/userguide/datafiles.html
  
  
          [^1]: For Python, any directory (with suitable naming) can be imported,
                even if it does not contain any `.py` files.
                On the other hand, currently there is no concept of package data
                directory, all directories are treated like packages.
          ********************************************************************************
  
  !!
    check.warn(importable)
  /private/var/folders/5r/7scst4zn1gd_2n5qw4fcl9xc0000gn/T/pip-build-env-0s7wsxk0/overlay/lib/python3.14/site-packages/setuptools/command/build_py.py:212: _Warning: Package 'pyarrow.tests.parquet' is absent from the `packages` configuration.
  !!
  
          ********************************************************************************
          ############################
          # Package would be ignored #
          ############################
          Python recognizes 'pyarrow.tests.parquet' as an importable package[^1],
          but it is absent from setuptools' `packages` configuration.
  
          This leads to an ambiguous overall configuration. If you want to distribute this
          package, please make sure that 'pyarrow.tests.parquet' is explicitly added
          to the `packages` configuration field.
  
          Alternatively, you can also rely on setuptools' discovery methods
          (for example by using `find_namespace_packages(...)`/`find_namespace:`
          instead of `find_packages(...)`/`find:`).
  
          You can read more about "package discovery" on setuptools documentation page:
  
          - https://setuptools.pypa.io/en/latest/userguide/package_discovery.html
  
          If you don't want 'pyarrow.tests.parquet' to be distributed and are
          already explicitly excluding 'pyarrow.tests.parquet' via
          `find_namespace_packages(...)/find_namespace` or `find_packages(...)/find`,
          you can try to use `exclude_package_data`, or `include-package-data=False` in
          combination with a more fine grained `package-data` configuration.
  
          You can read more about "package data files" on setuptools documentation page:
  
          - https://setuptools.pypa.io/en/latest/userguide/datafiles.html
  
  
          [^1]: For Python, any directory (with suitable naming) can be imported,
                even if it does not contain any `.py` files.
                On the other hand, currently there is no concept of package data
                directory, all directories are treated like packages.
          ********************************************************************************
  
  !!
    check.warn(importable)
  /private/var/folders/5r/7scst4zn1gd_2n5qw4fcl9xc0000gn/T/pip-build-env-0s7wsxk0/overlay/lib/python3.14/site-packages/setuptools/command/build_py.py:212: _Warning: Package 'pyarrow.vendored' is absent from the `packages` configuration.
  !!
  
          ********************************************************************************
          ############################
          # Package would be ignored #
          ############################
          Python recognizes 'pyarrow.vendored' as an importable package[^1],
          but it is absent from setuptools' `packages` configuration.
  
          This leads to an ambiguous overall configuration. If you want to distribute this
          package, please make sure that 'pyarrow.vendored' is explicitly added
          to the `packages` configuration field.
  
          Alternatively, you can also rely on setuptools' discovery methods
          (for example by using `find_namespace_packages(...)`/`find_namespace:`
          instead of `find_packages(...)`/`find:`).
  
          You can read more about "package discovery" on setuptools documentation page:
  
          - https://setuptools.pypa.io/en/latest/userguide/package_discovery.html
  
          If you don't want 'pyarrow.vendored' to be distributed and are
          already explicitly excluding 'pyarrow.vendored' via
          `find_namespace_packages(...)/find_namespace` or `find_packages(...)/find`,
          you can try to use `exclude_package_data`, or `include-package-data=False` in
          combination with a more fine grained `package-data` configuration.
  
          You can read more about "package data files" on setuptools documentation page:
  
          - https://setuptools.pypa.io/en/latest/userguide/datafiles.html
  
  
          [^1]: For Python, any directory (with suitable naming) can be imported,
                even if it does not contain any `.py` files.
                On the other hand, currently there is no concept of package data
                directory, all directories are treated like packages.
          ********************************************************************************
  
  !!
    check.warn(importable)
  copying pyarrow/__init__.pxd -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow
  copying pyarrow/_acero.pxd -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow
  copying pyarrow/_acero.pyx -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow
  copying pyarrow/_azurefs.pyx -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow
  copying pyarrow/_compute.pxd -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow
  copying pyarrow/_compute.pyx -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow
  copying pyarrow/_csv.pxd -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow
  copying pyarrow/_csv.pyx -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow
  copying pyarrow/_cuda.pxd -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow
  copying pyarrow/_cuda.pyx -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow
  copying pyarrow/_dataset.pxd -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow
  copying pyarrow/_dataset.pyx -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow
  copying pyarrow/_dataset_orc.pyx -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow
  copying pyarrow/_dataset_parquet.pxd -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow
  copying pyarrow/_dataset_parquet.pyx -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow
  copying pyarrow/_dataset_parquet_encryption.pyx -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow
  copying pyarrow/_dlpack.pxi -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow
  copying pyarrow/_feather.pyx -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow
  copying pyarrow/_flight.pyx -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow
  copying pyarrow/_fs.pxd -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow
  copying pyarrow/_fs.pyx -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow
  copying pyarrow/_gcsfs.pyx -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow
  copying pyarrow/_hdfs.pyx -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow
  copying pyarrow/_json.pxd -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow
  copying pyarrow/_json.pyx -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow
  copying pyarrow/_orc.pxd -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow
  copying pyarrow/_orc.pyx -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow
  copying pyarrow/_parquet.pxd -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow
  copying pyarrow/_parquet.pyx -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow
  copying pyarrow/_parquet_encryption.pxd -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow
  copying pyarrow/_parquet_encryption.pyx -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow
  copying pyarrow/_pyarrow_cpp_tests.pxd -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow
  copying pyarrow/_pyarrow_cpp_tests.pyx -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow
  copying pyarrow/_s3fs.pyx -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow
  copying pyarrow/_substrait.pyx -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow
  copying pyarrow/array.pxi -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow
  copying pyarrow/benchmark.pxi -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow
  copying pyarrow/builder.pxi -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow
  copying pyarrow/compat.pxi -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow
  copying pyarrow/config.pxi -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow
  copying pyarrow/device.pxi -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow
  copying pyarrow/error.pxi -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow
  copying pyarrow/gandiva.pyx -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow
  copying pyarrow/io.pxi -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow
  copying pyarrow/ipc.pxi -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow
  copying pyarrow/lib.pxd -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow
  copying pyarrow/lib.pyx -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow
  copying pyarrow/memory.pxi -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow
  copying pyarrow/pandas-shim.pxi -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow
  copying pyarrow/public-api.pxi -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow
  copying pyarrow/scalar.pxi -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow
  copying pyarrow/table.pxi -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow
  copying pyarrow/tensor.pxi -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow
  copying pyarrow/types.pxi -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow
  creating build/lib.macosx-10.15-universal2-cpython-314/pyarrow/includes
  copying pyarrow/includes/__init__.pxd -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/includes
  copying pyarrow/includes/common.pxd -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/includes
  copying pyarrow/includes/libarrow.pxd -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/includes
  copying pyarrow/includes/libarrow_acero.pxd -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/includes
  copying pyarrow/includes/libarrow_cuda.pxd -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/includes
  copying pyarrow/includes/libarrow_dataset.pxd -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/includes
  copying pyarrow/includes/libarrow_dataset_parquet.pxd -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/includes
  copying pyarrow/includes/libarrow_feather.pxd -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/includes
  copying pyarrow/includes/libarrow_flight.pxd -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/includes
  copying pyarrow/includes/libarrow_fs.pxd -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/includes
  copying pyarrow/includes/libarrow_python.pxd -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/includes
  copying pyarrow/includes/libarrow_substrait.pxd -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/includes
  copying pyarrow/includes/libgandiva.pxd -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/includes
  copying pyarrow/includes/libparquet.pxd -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/includes
  copying pyarrow/includes/libparquet_encryption.pxd -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/includes
  creating build/lib.macosx-10.15-universal2-cpython-314/pyarrow/interchange
  copying pyarrow/interchange/__init__.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/interchange
  copying pyarrow/interchange/buffer.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/interchange
  copying pyarrow/interchange/column.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/interchange
  copying pyarrow/interchange/dataframe.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/interchange
  copying pyarrow/interchange/from_dataframe.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/interchange
  creating build/lib.macosx-10.15-universal2-cpython-314/pyarrow/parquet
  copying pyarrow/parquet/__init__.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/parquet
  copying pyarrow/parquet/core.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/parquet
  copying pyarrow/parquet/encryption.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/parquet
  creating build/lib.macosx-10.15-universal2-cpython-314/pyarrow/src/arrow/python
  copying pyarrow/src/arrow/python/CMakeLists.txt -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/src/arrow/python
  copying pyarrow/src/arrow/python/api.h -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/src/arrow/python
  copying pyarrow/src/arrow/python/arrow_to_pandas.cc -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/src/arrow/python
  copying pyarrow/src/arrow/python/arrow_to_pandas.h -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/src/arrow/python
  copying pyarrow/src/arrow/python/arrow_to_python_internal.h -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/src/arrow/python
  copying pyarrow/src/arrow/python/async.h -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/src/arrow/python
  copying pyarrow/src/arrow/python/benchmark.cc -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/src/arrow/python
  copying pyarrow/src/arrow/python/benchmark.h -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/src/arrow/python
  copying pyarrow/src/arrow/python/common.cc -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/src/arrow/python
  copying pyarrow/src/arrow/python/common.h -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/src/arrow/python
  copying pyarrow/src/arrow/python/csv.cc -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/src/arrow/python
  copying pyarrow/src/arrow/python/csv.h -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/src/arrow/python
  copying pyarrow/src/arrow/python/datetime.cc -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/src/arrow/python
  copying pyarrow/src/arrow/python/datetime.h -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/src/arrow/python
  copying pyarrow/src/arrow/python/decimal.cc -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/src/arrow/python
  copying pyarrow/src/arrow/python/decimal.h -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/src/arrow/python
  copying pyarrow/src/arrow/python/extension_type.cc -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/src/arrow/python
  copying pyarrow/src/arrow/python/extension_type.h -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/src/arrow/python
  copying pyarrow/src/arrow/python/filesystem.cc -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/src/arrow/python
  copying pyarrow/src/arrow/python/filesystem.h -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/src/arrow/python
  copying pyarrow/src/arrow/python/flight.cc -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/src/arrow/python
  copying pyarrow/src/arrow/python/flight.h -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/src/arrow/python
  copying pyarrow/src/arrow/python/gdb.cc -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/src/arrow/python
  copying pyarrow/src/arrow/python/gdb.h -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/src/arrow/python
  copying pyarrow/src/arrow/python/helpers.cc -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/src/arrow/python
  copying pyarrow/src/arrow/python/helpers.h -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/src/arrow/python
  copying pyarrow/src/arrow/python/inference.cc -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/src/arrow/python
  copying pyarrow/src/arrow/python/inference.h -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/src/arrow/python
  copying pyarrow/src/arrow/python/io.cc -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/src/arrow/python
  copying pyarrow/src/arrow/python/io.h -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/src/arrow/python
  copying pyarrow/src/arrow/python/ipc.cc -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/src/arrow/python
  copying pyarrow/src/arrow/python/ipc.h -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/src/arrow/python
  copying pyarrow/src/arrow/python/iterators.h -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/src/arrow/python
  copying pyarrow/src/arrow/python/numpy_convert.cc -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/src/arrow/python
  copying pyarrow/src/arrow/python/numpy_convert.h -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/src/arrow/python
  copying pyarrow/src/arrow/python/numpy_init.cc -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/src/arrow/python
  copying pyarrow/src/arrow/python/numpy_init.h -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/src/arrow/python
  copying pyarrow/src/arrow/python/numpy_internal.h -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/src/arrow/python
  copying pyarrow/src/arrow/python/numpy_interop.h -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/src/arrow/python
  copying pyarrow/src/arrow/python/numpy_to_arrow.cc -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/src/arrow/python
  copying pyarrow/src/arrow/python/numpy_to_arrow.h -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/src/arrow/python
  copying pyarrow/src/arrow/python/parquet_encryption.cc -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/src/arrow/python
  copying pyarrow/src/arrow/python/parquet_encryption.h -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/src/arrow/python
  copying pyarrow/src/arrow/python/platform.h -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/src/arrow/python
  copying pyarrow/src/arrow/python/pyarrow.cc -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/src/arrow/python
  copying pyarrow/src/arrow/python/pyarrow.h -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/src/arrow/python
  copying pyarrow/src/arrow/python/pyarrow_api.h -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/src/arrow/python
  copying pyarrow/src/arrow/python/pyarrow_lib.h -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/src/arrow/python
  copying pyarrow/src/arrow/python/python_test.cc -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/src/arrow/python
  copying pyarrow/src/arrow/python/python_test.h -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/src/arrow/python
  copying pyarrow/src/arrow/python/python_to_arrow.cc -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/src/arrow/python
  copying pyarrow/src/arrow/python/python_to_arrow.h -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/src/arrow/python
  copying pyarrow/src/arrow/python/type_traits.h -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/src/arrow/python
  copying pyarrow/src/arrow/python/udf.cc -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/src/arrow/python
  copying pyarrow/src/arrow/python/udf.h -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/src/arrow/python
  copying pyarrow/src/arrow/python/util.cc -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/src/arrow/python
  copying pyarrow/src/arrow/python/util.h -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/src/arrow/python
  copying pyarrow/src/arrow/python/visibility.h -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/src/arrow/python
  creating build/lib.macosx-10.15-universal2-cpython-314/pyarrow/src/arrow/python/vendored
  copying pyarrow/src/arrow/python/vendored/CMakeLists.txt -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/src/arrow/python/vendored
  copying pyarrow/src/arrow/python/vendored/pythoncapi_compat.h -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/src/arrow/python/vendored
  creating build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests
  copying pyarrow/tests/__init__.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests
  copying pyarrow/tests/arrow_16597.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests
  copying pyarrow/tests/arrow_39313.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests
  copying pyarrow/tests/arrow_7980.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests
  copying pyarrow/tests/bound_function_visit_strings.pyx -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests
  copying pyarrow/tests/conftest.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests
  copying pyarrow/tests/extensions.pyx -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests
  copying pyarrow/tests/pandas_examples.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests
  copying pyarrow/tests/pandas_threaded_import.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests
  copying pyarrow/tests/pyarrow_cython_example.pyx -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests
  copying pyarrow/tests/read_record_batch.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests
  copying pyarrow/tests/strategies.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests
  copying pyarrow/tests/test_acero.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests
  copying pyarrow/tests/test_adhoc_memory_leak.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests
  copying pyarrow/tests/test_array.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests
  copying pyarrow/tests/test_builder.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests
  copying pyarrow/tests/test_cffi.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests
  copying pyarrow/tests/test_compute.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests
  copying pyarrow/tests/test_convert_builtin.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests
  copying pyarrow/tests/test_cpp_internals.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests
  copying pyarrow/tests/test_csv.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests
  copying pyarrow/tests/test_cuda.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests
  copying pyarrow/tests/test_cuda_numba_interop.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests
  copying pyarrow/tests/test_cython.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests
  copying pyarrow/tests/test_dataset.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests
  copying pyarrow/tests/test_dataset_encryption.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests
  copying pyarrow/tests/test_deprecations.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests
  copying pyarrow/tests/test_device.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests
  copying pyarrow/tests/test_dlpack.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests
  copying pyarrow/tests/test_exec_plan.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests
  copying pyarrow/tests/test_extension_type.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests
  copying pyarrow/tests/test_feather.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests
  copying pyarrow/tests/test_flight.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests
  copying pyarrow/tests/test_flight_async.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests
  copying pyarrow/tests/test_fs.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests
  copying pyarrow/tests/test_gandiva.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests
  copying pyarrow/tests/test_gdb.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests
  copying pyarrow/tests/test_io.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests
  copying pyarrow/tests/test_ipc.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests
  copying pyarrow/tests/test_json.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests
  copying pyarrow/tests/test_jvm.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests
  copying pyarrow/tests/test_memory.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests
  copying pyarrow/tests/test_misc.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests
  copying pyarrow/tests/test_orc.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests
  copying pyarrow/tests/test_pandas.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests
  copying pyarrow/tests/test_scalars.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests
  copying pyarrow/tests/test_schema.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests
  copying pyarrow/tests/test_sparse_tensor.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests
  copying pyarrow/tests/test_strategies.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests
  copying pyarrow/tests/test_substrait.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests
  copying pyarrow/tests/test_table.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests
  copying pyarrow/tests/test_tensor.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests
  copying pyarrow/tests/test_types.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests
  copying pyarrow/tests/test_udf.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests
  copying pyarrow/tests/test_util.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests
  copying pyarrow/tests/test_without_numpy.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests
  copying pyarrow/tests/util.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests
  copying pyarrow/tests/wsgi_examples.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests
  creating build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests/data/feather
  copying pyarrow/tests/data/feather/v0.17.0.version.2-compression.lz4.feather -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests/data/feather
  creating build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests/data/orc
  copying pyarrow/tests/data/orc/README.md -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests/data/orc
  copying pyarrow/tests/data/orc/TestOrcFile.emptyFile.jsn.gz -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests/data/orc
  copying pyarrow/tests/data/orc/TestOrcFile.emptyFile.orc -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests/data/orc
  copying pyarrow/tests/data/orc/TestOrcFile.test1.jsn.gz -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests/data/orc
  copying pyarrow/tests/data/orc/TestOrcFile.test1.orc -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests/data/orc
  copying pyarrow/tests/data/orc/TestOrcFile.testDate1900.jsn.gz -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests/data/orc
  copying pyarrow/tests/data/orc/TestOrcFile.testDate1900.orc -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests/data/orc
  copying pyarrow/tests/data/orc/decimal.jsn.gz -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests/data/orc
  copying pyarrow/tests/data/orc/decimal.orc -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests/data/orc
  creating build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests/data/parquet
  copying pyarrow/tests/data/parquet/v0.7.1.all-named-index.parquet -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests/data/parquet
  copying pyarrow/tests/data/parquet/v0.7.1.column-metadata-handling.parquet -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests/data/parquet
  copying pyarrow/tests/data/parquet/v0.7.1.parquet -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests/data/parquet
  copying pyarrow/tests/data/parquet/v0.7.1.some-named-index.parquet -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests/data/parquet
  creating build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests/interchange
  copying pyarrow/tests/interchange/__init__.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests/interchange
  copying pyarrow/tests/interchange/test_conversion.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests/interchange
  copying pyarrow/tests/interchange/test_interchange_spec.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests/interchange
  creating build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests/parquet
  copying pyarrow/tests/parquet/__init__.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests/parquet
  copying pyarrow/tests/parquet/common.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests/parquet
  copying pyarrow/tests/parquet/conftest.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests/parquet
  copying pyarrow/tests/parquet/encryption.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests/parquet
  copying pyarrow/tests/parquet/test_basic.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests/parquet
  copying pyarrow/tests/parquet/test_compliant_nested_type.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests/parquet
  copying pyarrow/tests/parquet/test_data_types.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests/parquet
  copying pyarrow/tests/parquet/test_dataset.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests/parquet
  copying pyarrow/tests/parquet/test_datetime.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests/parquet
  copying pyarrow/tests/parquet/test_encryption.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests/parquet
  copying pyarrow/tests/parquet/test_metadata.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests/parquet
  copying pyarrow/tests/parquet/test_pandas.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests/parquet
  copying pyarrow/tests/parquet/test_parquet_file.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests/parquet
  copying pyarrow/tests/parquet/test_parquet_writer.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/tests/parquet
  creating build/lib.macosx-10.15-universal2-cpython-314/pyarrow/vendored
  copying pyarrow/vendored/__init__.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/vendored
  copying pyarrow/vendored/docscrape.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/vendored
  copying pyarrow/vendored/version.py -> build/lib.macosx-10.15-universal2-cpython-314/pyarrow/vendored
  running build_ext
  creating /private/var/folders/5r/7scst4zn1gd_2n5qw4fcl9xc0000gn/T/pip-install-cmvb0na0/pyarrow_f14bfe39afb34ba7a56a9323298f0239/build/temp.macosx-10.15-universal2-cpython-314
  -- Running cmake for PyArrow
  cmake -DCMAKE_INSTALL_PREFIX=/private/var/folders/5r/7scst4zn1gd_2n5qw4fcl9xc0000gn/T/pip-install-cmvb0na0/pyarrow_f14bfe39afb34ba7a56a9323298f0239/build/lib.macosx-10.15-universal2-cpython-314/pyarrow -DPYTHON_EXECUTABLE=/usr/local/bin/python3 -DPython3_EXECUTABLE=/usr/local/bin/python3 -DPYARROW_CXXFLAGS= -DPYARROW_BUNDLE_ARROW_CPP=off -DPYARROW_BUNDLE_CYTHON_CPP=off -DPYARROW_GENERATE_COVERAGE=off -DCMAKE_BUILD_TYPE=release /private/var/folders/5r/7scst4zn1gd_2n5qw4fcl9xc0000gn/T/pip-install-cmvb0na0/pyarrow_f14bfe39afb34ba7a56a9323298f0239
  error: command 'cmake' failed: No such file or directory
  [end of output]
