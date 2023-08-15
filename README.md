# PokemonBDSPRNGLibrary-python
 
## What's this?
夜綱氏による[PokemonBDSPRNGLibrary](https://github.com/yatsuna827/PokemonBDSPRNGLibrary) をPython向けに移植したものです.

拙作のProject_Xsが複雑怪奇で密結合になっていたことを踏まえて, C#上での優れた実装を逆輸入してより利用しやすいライブラリを提供することを目的としています.

現時点では以下の機能を提供しています.

- ゴンベの瞬きからの基準Seed特定 (`MunchlaxInverter`)
- ゴンベの瞬きからの現在Seed再特定 (`MunchlaxLinearSearch`) (WIP)
- 主人公の瞬きからの基準Seed特定 (`PlayerBlinkInverter`)
- 主人公の瞬きからの現在Seed再特定 (`PlayerLinearSearch`) (WIP)

## 依存ライブラリ
- numpy
