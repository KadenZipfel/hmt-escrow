import setuptools

setuptools.setup(
    name="human-contracts",
    version=.1,
    author="HUMAN Protocol",
    description=
    "A python library to launch escrow contracts to the HUMAN network.",
    url="https://github.com/hCaptcha/hmt-escrow",
    include_package_data=True,
    zip_safe=True,
    classifiers=[
        "Intended Audience :: Developers",
        "Operating System :: OS Independent", "Programming Language :: Python"
    ],
    packages=setuptools.find_packages(),
)