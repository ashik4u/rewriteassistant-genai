from setuptools import setup, find_packages

setup(
    name='clipboard_rewriter',
    version='1.0.0',
    author='Your Name',
    description='Clipboard grammar checker and rewriting tool using Google Gemini',
    packages=find_packages(),
    install_requires=[
        'pyperclip',
        'keyboard',
        'pystray',
        'pillow',
        'winotify',
        'google-generativeai'
    ],
    entry_points={
        'console_scripts': [
            'clipboard-rewriter=rewriteassistant-genai:main'
        ]
    },
)
