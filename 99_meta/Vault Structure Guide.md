# Obsidian Vault Structure Guide

このドキュメントは、最適化されたHybrid PARA-Zettelkastenシステムの使用方法を説明します。

## 📁 フォルダ構造

### `00_inbox/`
- **目的**: 未分類・一時保管
- **使用方法**: すべての新しい情報の最初の受け皿
- **処理**: 定期的にトリアージして適切なフォルダに移動

### `01_daily/`  
- **目的**: 日次ノート（YYYY-MM-DD形式）
- **テンプレート**: Daily Note Template
- **自動化**: Dataviewで進捗・学習を自動集計

### `02_zettelkasten/`
原子的知識とアイデアの管理
- `concepts/` - 概念・理論
- `insights/` - 洞察・発見  
- `connections/` - 知識間の関連性

### `10_projects/`
- **目的**: アクティブプロジェクト
- **テンプレート**: Project Template
- **管理**: ステータス・期限・進捗を追跡

### `20_areas/`
継続的責任領域
- `personal/` - 個人的な活動
- `business/home-tutor/` - ホームチューター事業
- `education/` - 学習・教育関連
- `programming/` - 技術・開発
- `technical/` - 技術レポート・分析

### `30_resources/`
参考資料とツール
- `templates/` - ノートテンプレート
- `literature/` - 書籍・文献要約
- `references/` - 会議資料・外部リソース

### `90_archive/`
- **目的**: 完了・非アクティブコンテンツ
- **構成**:
  - `duplicates_20250811/` - 最適化時に除去された重複ファイル
  - `ingested_exports_20250811/` - 外部システムから移行された履歴データ
- **処理**: 完了したプロジェクトや古い資料

### `99_meta/`
- **目的**: システム管理・設定
- **内容**: メンテナンススクリプト・ガイド・最適化ツール

## 🔄 ワークフロー

### 1. 情報の取り込み
1. すべての新情報を`00_inbox/`に保存
2. 週次レビューで適切なフォルダに分類
3. 必要に応じてテンプレートを適用

### 2. プロジェクト管理
1. 新プロジェクトは`10_projects/`でProject Template使用
2. 完了したら`90_archive/`に移動
3. Dataviewで進捗を自動追跡

### 3. 知識管理
1. アイデアは`02_zettelkasten/`で原子化
2. 読書ノートは`30_resources/literature/`
3. バックリンクで知識をネットワーク化

### 4. 日常的な使用
1. 毎日`01_daily/`で振り返り
2. 会議は Meeting Template 使用
3. 学習はLiterature Templateで記録

## 🏷️ タグ戦略

### プライマリタグ
- `#project` - プロジェクト関連
- `#daily` - 日次ノート
- `#literature` - 文献・書籍
- `#zettelkasten` - 知識ノート
- `#meeting` - 会議記録

### セカンダリタグ
- `#business` `#technical` `#personal` - 領域
- `#high` `#medium` `#low` - 優先度
- `#idea` `#insight` `#concept` - 知識タイプ

## 📊 Dataview活用

### プロジェクトダッシュボード
```dataview
TABLE status, due_date, priority
FROM "10_projects"
WHERE status != "completed"
SORT due_date ASC
```

### 最近の活動
```dataview  
LIST
FROM "01_daily"
SORT file.name DESC
LIMIT 7
```

### 未読文献
```dataview
TABLE author, completion
FROM "30_resources/literature"
WHERE completion < 100
SORT completion ASC
```

## 🔧 メンテナンス

### メンテナンススクリプト

#### `enhanced_uuid_cleanup.py` （メイン）
```bash
python3 99_meta/enhanced_uuid_cleanup.py
```
- **目的**: UUIDサフィックスのファイル名正規化
- **機能**: 
  - 空白プレフィックス付きUUIDパターンの除去
  - 32文字16進文字列の除去
  - markdown内部リンクの自動更新
- **実績**: 1,695ファイル処理、76ファイルをリネーム

#### `check_broken_links.py` （診断）
```bash
python3 99_meta/check_broken_links.py
```
- **目的**: 破損した内部リンクの検出
- **出力**: 詳細なリンク解析レポート

#### `fix_broken_links.py` （修復）
```bash
python3 99_meta/fix_broken_links.py
```
- **目的**: 一般的な破損リンクパターンの修復
- **対象**: テンプレートプレースホルダー、URLエンコード問題
- **実績**: 最適化時に29ファイルを修復

#### `cleanup_uuid_files.py` （レガシー）
- 基本的なUUID除去スクリプト
- enhanced版の使用を推奨

### 週次レビュー（日曜日）
- [ ] `00_inbox/`の整理
- [ ] プロジェクトステータス更新
- [ ] 完了項目の`90_archive/`移動
- [ ] 来週の計画作成
- [ ] リンク整合性チェック実行

### 月次レビュー
- [ ] Zettelkastenの接続見直し
- [ ] タグ体系の最適化
- [ ] テンプレート改善
- [ ] システム全体の評価
- [ ] メンテナンススクリプトの実行

## 🎯 成功の指標

- **Inbox Zero**: `00_inbox/`を定期的に空に
- **日次習慣**: Daily Templateの継続使用
- **知識接続**: Zettelkastenでの関連性構築
- **プロジェクト完了**: 計画的な進行管理

このシステムにより、情報の整理・知識の蓄積・プロジェクト管理を統合的に行えます。