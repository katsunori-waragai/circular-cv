# circular-cv
check for circular import 

# Why
- OpenCV を利用するパッケージを多数インストールしている状況で、 importErrorを生じることがある。
- そのため、OpenCVのバージョンを固定して開発しがちだ。

## 対策
- Docker環境, venv環境を用いて、他のプロジェクトと環境を分離する。
- 個別に`pip install パッケージ`を重ねることはしない。
- pyproject.toml の
```commandline
dependencies = [
    "numpy<2",
    "opencv-python==3.4.18.65",
]

```
に各パッケージのバージョンの範囲を記述する。
そうすることで、個別にpip install するときよりも、整合性の高いバージョンの組合せを選択できることを期待している。


#### requirements.txt を使わない理由
- 環境の種類によらず、共通の設定で反映させたいため。
- 該当のリポジトリのパッケージを`python3 -m pip install .` する際に余分な操作を必要とさせないため。

# SEE ALSO

[opencv-contrib-pythonが読み込めない](https://qiita.com/Yamakawa0032/items/306acee5532330010b34)

[Cannot import opencv because of circular import](https://stackoverflow.com/questions/72732256/cannot-import-opencv-because-of-circular-import)
