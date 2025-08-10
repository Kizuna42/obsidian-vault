# wise saying

- 他者が、自分にとって何をしてくれるのかを期待する人生に、今日、終止符を打て。自分が、他者のために、何ができるのかを考え始めるのだ。それこそが、開国だ。

- 母が無知だと病気になり、父が無知だと貧乏になる。

- 一時間 幸せになりたかったら 酒を飲みなさい・三日間 幸せになりたかったら 結婚しなさい・永遠に 幸せになりたかったら 釣りを覚えなさい　　中国の古いことわざより

- **思考に気をつけなさい、それは、いつか言葉になるから。言葉に気をつけなさい、それは、いつか行動になるから。行動に気をつけなさい、それは、いつか習慣になるから。習慣に気をつけなさい、それは、いつか性格になるから。性格に気をつけなさい、それは、いつか運命になるから。**

『私たち人間は、長大なビルを作りあげたが、いっぽうで気は短くなった。　道路を広くしたわりに、視野は狭くなった。　お金を使っても身につくものはなく、ものを買っても楽しみは少ない。　家は大きくなったが、家族との関わりは小さい。　便利になったのに、時間はない。　専門家が増えても、それ以上に問題も増えた。　薬は増えたのに、健康な人は減った。　私たちは、酒を飲みすぎ、タバコを吸いすぎ、時間をムダに過ごし、少ししか笑わず、毎日を急ぎすぎ、怒りすぎ、夜更けまで起きすぎ、目覚めたらすでに疲れている』ワシントン州の牧師、ボブ・ムーアヘッド氏「現代の矛盾」

理二を目指すと早稲田になり
理一を目指すと理二になり
京医を目指すと阪医になり
理三を目指すと高卒になる

高きを望まずんば低きを得ずども、極みを望めば底をも失うのである。

以下、修正が必要なことを書きました。
bad/mapシリーズです。

maps/bad/forbidden.cub
動作してしまう、本当はエラーとして弾かなくてはいけないパターンです。
確認修正して。

・map_first.cub
Error
Multiple player positions found

・map_middle.cub
Error
Invalid character in map

・map_only.cub
Error
Missing north texture (NO)

エラーメッセージがこれで適切なのかは考えたほうがいいのかも。。。？
確認修正して。

次はgoodケースになります。assets/maps/good/
想定としては正しいmap、読み込んで正しく動作できることを想定していますが以下、現在の実装でのエラーたちになります。確認して修正してみて！

・wall_none.cub
Error
Texture file not found or not readable
と出て動作しない

・test_map_hole.cub
Error
Map not closed by walls
と出て動作しない

・test_pos_bottom.cub
・test_pos_left.cub
・test_pos_right.cub
・test_pos_top.cub
・test_textures.cub
天井が白、床が黒になってる？

・test_whitespace.cub
Error
Missing west texture (WE)
が出て動かない

・works.cub
Error
Texture file not found or not readable
が出て動かない

テストまでして、完璧に修正できたと思ったら、norminetteチェックしてgit push