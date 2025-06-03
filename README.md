# TMLHonyaku
<a target="_blank" href="https://discord.gg/ch2DVxf2jY"><img src="https://dcbadge.limes.pink/api/server/ch2DVxf2jY?style=flat" alt="" /></a>

[tModLoader][github:tModLoader]で使用できるhjsonファイルの翻訳置き場

大型Modを含む200以上のModに対応しています。
完全なリストは[TranslatedMods.csv][repo:TranslatedMods.csv]を参照してください。

## 使い方
[External Localizer][steam:ExternalLocalizer]を使って読み込ませるとテラリアのModを日本語化できます。
詳しくは、wiki[repo:wiki-HowToUse]を参照してください。

## ライセンス
### ・ [Terraria/ja-JP.hjson][repo:Terraria/ja-JP.hjson]
[synctam様][blog:synctam]による翻訳データをhjson形式に変換したものです。 \
したがって、[Terraria/ja-JP.hjson][repo:Terraria/ja-JP.hjson]は「[CC BY-NC-SA 4.0（表示 - 非営利 - 継承 4.0 国際）][hp:CC]」を継承します。

### ・ 各MODの翻訳データ
各MODの翻訳データは、それぞれ異なる翻訳者によって提供されているため、統一されたライセンスは設定されておりません。
個人利用およびTMLHonyakuへの貢献以外の目的で、翻訳データの改変や再配布を行う場合は、必ずDiscordにて該当の翻訳者へご確認ください。

## 免責事項
本プロジェクトは非公式の日本語翻訳であり、元のMOD制作者およびtModLoader公式とは一切関係ありません。
また翻訳の正確性や動作は保証されておらず、利用によって生じた不具合や損害について、当プロジェクトは責任を負いません。

## PRするときのお願い
- [本リポジトリのwiki][repo:wiki]をよく読んでください。
- TMLHonyakuには「自力で翻訳したもの」、もしくは「機械翻訳をよく確認し修正したもの」のみをアップロードしてください。
- hjsonを含むフォルダの名前はModの内部名にしてください。(`Mods.XXX.Items...`のうちXXXの部分)
- 新規翻訳を追加するときは[TranslatedMods.csv][repo:TranslatedMods.csv]に、情報を追加してください。`display_name`が昇順になるようにしてください。
- 可能であれば`ja-JP_Mods.XXX.hjson`のようにファイル名にMod名が含まれる書き方にしてください。External Localizerによるファイルの読み込み時の効率が上がります。

[github:tModLoader]: https://github.com/tModLoader/tModLoader
[repo:TranslatedMods.csv]: https://github.com/External-Localizer/TMLHonyaku/blob/main/TranslatedMods.csv
[repo:wiki]: https://github.com/ExternalLocalizer/TMLHonyaku/wiki
[repo:wiki-HowToUse]: https://github.com/ExternalLocalizer/TMLHonyaku/wiki#%E7%BF%BB%E8%A8%B3%E3%82%92%E4%BD%BF%E7%94%A8%E3%81%99%E3%82%8B
[steam:ExternalLocalizer]: https://steamcommunity.com/sharedfiles/filedetails/?id=2986383249
[github:tmlWiki]:https://github.com/tModLoader/tModLoader/wiki/Localization
[blog:synctam]: https://synctam.blogspot.com/2017/05/terraria_20.html
[repo:Terraria/ja-JP.hjson]: https://github.com/External-Localizer/TMLHonyaku/blob/main/Terraria/ja-JP.hjson
[hp:CC]: https://creativecommons.org/licenses/by-nc-sa/4.0/deed.ja
