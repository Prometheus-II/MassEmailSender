from setuptools import setup

setup(
    name='MassEmailSender',
    version='0.1.0',
    py_modules=['MassEmailSender'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'MassEmailSender = MassEmailSender:send',
        ],
    },
)
