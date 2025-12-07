# Contribution guidelines

翻訳の際は以下を参考にしてください。

- [本リポジトリのwiki][repo:wiki]
- [tModLoader wiki][github:tmlWiki]

> [!IMPORTANT]
> 本リポジトリのwikiには注意点が多く書かれています。**必ず読んでください**。


## 翻訳の方針

- TMLHonyakuには「自力で翻訳したもの」、もしくは「機械翻訳をよく確認し修正したもの」のみをアップロードしてください。
- 他の翻訳ファイルを参考にし、文の調子を合わせるようにしましょう。

## ファイル形式

### TranslatedMods.csv

翻訳されたModと翻訳者を記録しているファイルです。
Modを新しく翻訳した際や更新した際に必ず編集してください。

|     項目      |                                                             説明                                                             |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| steam_id      | steam上でのid。ModをWorkshop上で開いたときのurlに表示されます。                                                              |
| display_name  | steam上での名前。ModをWorkshop上で開いたときのタイトルです。 **この値が昇順に並ぶようにしてください!**                       |
| internal_name | tModLoaderが利用する内部名。<br>ファイル名の`ja-JP_Mods.XXX.hjson`の`XXX`、無ければhjsonファイル内の`Mods`の一つ中にあるキーの名前です。 |
| version       | バージョン。ゲーム内で確認するか、Workshopから変更履歴を見ると書いてあります。                                               |
| translators   | 翻訳者の名前。複数人いる場合は半角スペースなどで区切って書いてください。                                                     |
| internal_note | 翻訳者向けメモ。なにかほかの翻訳者に書き残しておきたいことがあれば利用してください。 |
| display_note  | プレイヤー向けのメモ。JpPackでModListのアイコンにカーソルを合わせると表示されます。<br>翻訳不可部分が多い場合などがあれば書いておいてください。|

### hjson

#### 保存場所

Modの内部名のフォルダを作り、その中にhjsonファイルを作成してください

> 例: CalamityMod
>
> ``CalamityMod/ja-JP_Mods.CalamityMod.hjson``

#### ファイル名

`ja-JP_Mods.XXX.hjson`のようにファイル名にMod名が含まれる書き方にしてください。External Localizer によるファイルの読み込み時の効率が上がります。

> [!NOTE]
> Mods.XXXから始まらないキーを含む場合は、例外としてこれに従う必要はありません。


> ダメな例: ``CalamityMod/ja-JP.hjson``
> 
> ```hjson
> Mods: {
>   CalamityMod: {
>     Vanilla: {
>       WizardChat: {
>         ...
>       }
>     }
>   }
> }
> ```
> 
> 良い例: ``CalamityMod/ja-JP_Mods.CalamityMod.hjson``
> 
> `Mods.CalamityMod`をパスに含めることで、hjsonから該当部分を省略できます。
> 
> ```hjson
> Vanilla: {
>   WizardChat: {
>     ...
>   }
> }
> ```


[github:tmlWiki]:https://github.com/tModLoader/tModLoader/wiki/Localization
[repo:wiki]: https://github.com/ExternalLocalizer/TMLHonyaku/wiki
