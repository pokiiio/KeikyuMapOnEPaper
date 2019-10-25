***京急の運行情報ページに変更があったため、現在このライブラリは利用できません***
***近日中に対応予定です***


![pokiiio KeikyuMapOnEPaper](https://lh3.googleusercontent.com/gAKy1D9X09dkf0msIxjfWhUhc_mro92Mvdzg_1zPmXx7KBc1gDK3d4RtEdrPdQFfzk0V3V-ROmOCkrqHy3U-2bC2_y9ZP8ezwYdJZB4WeXm9oIsTMDAIpwpOgy9X5kDGB6bv2YfSYfU=s600 "pokiiio KeikyuMapOnEPaper")

# KeikyuMapOnEPaper
京急の運行情報を路線図とともに電子ペーパーに表示します。



## 概要
京急の運行情報の文字列から、Waveshare製の2.7インチ3色電子ペーパーに、上の写真のような運行情報画面を表示します。


## 使い方

下記のようにPythonスクリプトを実行するだけです。


 ```bash
python path/to/show_keikyu_map.py "(京急運行情報文字列)"
 ```


## 詳細

+ 引数で与えられた文字列から、遅れてる路線と、遅れの具合を解析。
+ PythonのPILで、遅れてる路線をハイライトした路線図と、タイトル・運行情報を文字列で表示したPNG画像を作成。
+ Wavashareのライブラリで電子ペーパーに描画。
+ フォントは毎度おなじみのM+ FONTS [（https://mplus-fonts.osdn.jp/）](https://mplus-fonts.osdn.jp/)を使わせていただいております。ありがとうございます。


## 備考

 + 諸事情により、運行情報の文字列の取得は、このライブラリでは行いません。必要であれば、[こちらのライブラリ](https://github.com/pokiiio/KeikyuPython)をお使いください。
 + Waveshareの2.7インチ三色電子ペーパー向けの実装をしています。他のサイズであったり、他社製の電子ペーパーをお使いの場合は、一部実装を書き換える必要があります。



## Maker Faire Tokyo 2018に出展


[MFT2018に出展しました。](http://makezine.jp/event/makers2018/m0461/)


![pokiiio KeikyuMapOnEPaper](https://lh3.googleusercontent.com/nMdJF9g-Zek4dvVI20-IqjGfAADFRpn8btGzn4srh3H1-N1gbQN1DPlISUA-r-jOFp_ccorh0tzkPb8uqR-cCqVuCKr52XL1Nm1V4OuwiPBF0Gvo9iYStDlc8RPEPb_xCs-DwfKAgUY=s600 "pokiiio KeikyuMapOnEPaper")


## 表示例


![pokiiio KeikyuMapOnEPaper](https://lh3.googleusercontent.com/ez_qvkWS75bV6edqtCEUy346xJz4_cN4y4Wwq32g3mYKdDF1HEJNLNi7FgW7tV5_upOqj_bH5Hw5AtxUEFTO6AI6ceNLoodfES0_G7SzXcd5Oz3kn0I9VB-pTYSMxhnu-gDPIDVTYAM=s600 "pokiiio KeikyuMapOnEPaper")


![pokiiio KeikyuMapOnEPaper](https://lh3.googleusercontent.com/9_EasjMLpjBng2OCY4nXBffzjAiJiq-KyeRr7MGcPBdrAlk5venmxxTLsyvuItcKiM87EZIG8po5R6WD8Funmus5ixwEQD3jbjXNfDjBXfsSdgABn_PB0XWJS07sVVWw5wyFsiyHtEY=s600 "pokiiio KeikyuMapOnEPaper")
