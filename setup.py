from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# long_description(後述)に、GitHub用のREADME.mdを指定
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='gxsimcom', # パッケージ名(プロジェクト名)
    packages=find_packages(where='./src'), # パッケージ内(プロジェクト内)のパッケージ名をリスト形式で指定
    package_dir={'': 'src'},

    version='0.0.2', # バージョン

    license='MIT', # ライセンス

    install_requires=['psutil'], # pip installする際に同時にインストールされるパッケージ名をリスト形式で指定

    author='tyaromax', # パッケージ作者の名前
    author_email='tkentyan@hotmail.com', # パッケージ作者の連絡先メールアドレス

    url='https://github.com/tyaro/GXSim2Com', # パッケージに関連するサイトのURL(GitHubなど)

    description='Communication to GXSimulator2', # パッケージの簡単な説明
    long_description=long_description, # PyPIに'Project description'として表示されるパッケージの説明文
    long_description_content_type='text/markdown', # long_descriptionの形式を'text/plain', 'text/x-rst', 'text/markdown'のいずれかから指定
    keywords ='GXSimulator GXSim gxsimcom', # PyPIでの検索用キーワードをスペース区切りで指定

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ], # パッケージ(プロジェクト)の分類。https://pypi.org/classifiers/に掲載されているものを指定可能。
)