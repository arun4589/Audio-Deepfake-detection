from setuptools import setup, find_packages

setup(
    name='audio-deepfake-detection-rawnet2',
    version='1.0.0',
    description='Audio Deepfake Detection using RawNet2',
    author='Arun kumawat',
    author_email='erarunkumawat50@gmail.com',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'tensorflow==2.13.0',
        'librosa==0.10.0',
        'numpy==1.24.3',
        'scipy==1.11.1',
        'pandas==2.0.2',
        'matplotlib==3.7.2',
        'tqdm==4.65.0'
    ],
    python_requires='>=3.8',
)