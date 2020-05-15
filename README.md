このディレクトリについての説明
  各人の名前のディレクトリには先日提出してもらったプログラムを髙瀬が添削したものをUploadしている．
  /transmittanceにはある日の透過率測定のデータファイルをUploadしている．

透過率のデータファイルについて
    data_01.csv
        各周波数に対してある測定値が記載されている(セパレータは",")
        測定値の物理量はヘッダーに記載されている．
        [freq] 周波数
        [att_value] アッテネータの値．単位は[dB]
        [Rate] 1分間での測定値揺らぎ．１以下になると測定スタートするように設定してある．
        [air_power] 空気伝搬時の検出電圧．
        [sample_power] サンプル伝搬時の検出電圧．
        [Transmittans] 透過率．(sample_power/air_power)
        [air_thrmcp] 空気伝搬時の逓倍器の温度
        [sample_thrmcp] サンプル伝搬時の逓倍器の温度

    air_array01.csv
        Air測定時において各周波数についてN回データ取得を行ったときの電圧値．
        これにより電圧の平均値をはじめとする種々の統計量を計算することができる．
        誤差を計算する場合はこのファイルを用いる．
    sample_arrau01.csv
        Sample測定時においてair_array01.csvと同様の内容．

    information_spp_IPMU_01.csv
        サンプル情報と測定条件が記載されている．
            [thickness] サンプル厚さ
            [angle] 平行波ビームに対するサンプル角度．単位は[deg(度)]
            [start_offset] 測定開始時のオフセット
            [end_offset] 測定終了時のオフセット
            ~オフセットとは~
            電圧が検出されていないときでも，ノイズなどの影響である電圧が測定されてしまう．
            例えば，なんらかの影響で1mVが平均的に検出されてしまっている場合は，
            解析時には測定値から1mVのオフセットを引く必要が生じる．
            [elapsed_time] 測定開始から終了までの時間[s]

    Transmittance_spp_IPMU_01.png
        透過率の周波数依存性のグラフ．測定終了時に自動出力されたもの．


pythonプログラムについて
  theory_curve.py
  透過率の理論曲線を計算するためのモジュール．主に長野が開発して，髙瀬が各種チューニングを施している．
  主にtheory_curve関数から派生した関数がパッケージされている．
    theory_curve( n, d, freq_in, angle_in, incpol)
      透過率の理論曲線を計算する関数．
      n : 屈折率 type -->> float
      d : サンプル厚さ type -->> float
      freq_in : 入力周波数．type -->> numpy.array
      angle_in : サンプル角度　type -->> float
      incpol : P偏光orS偏光　type -->> int   -1を指定すること．

    fit_2(freq_in, n)
      フィッティング用関数．scipy.curve_fitで使用する．
