from setuptools import setup, find_packages

setup(
    name="shelves_controller",
    version="1.0.0",
    author='Serhii Shchoholiev',
    packages=find_packages(where="shelves_controller"),
    package_dir={'': 'shelves_controller'},
    package_data={
        'app': ['appconfig.json', 'deviceconfig.json'],
    },
    entry_points={
        'console_scripts': [
            'shelvescontroller=app.app:run',
        ],
    },
    install_requires=[
        'azure-iot-device==2.12.0',
        'certifi==2023.11.17',
        'charset-normalizer==3.3.2',
        'deprecation==2.1.0',
        'idna==3.4',
        'janus==1.0.0',
        'packaging==23.2',
        'paho-mqtt==1.6.1',
        'PySocks==1.7.1',
        'requests==2.31.0',
        'requests-unixsocket==0.3.0',
        'RPi.GPIO==0.7.1',
        'setuptools==68.2.2',
        'typing_extensions==4.8.0',
        'urllib3==1.26.18',
        'wheel==0.41.3',
    ]
)
