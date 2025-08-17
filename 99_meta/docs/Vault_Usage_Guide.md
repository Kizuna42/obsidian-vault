---
title: "Obsidian Vault Usage Guide"
created: 2025-08-17
updated: 2025-08-17
tags: [guide, vault-management, para-method, zettelkasten]
category: documentation
status: active
---

# Obsidian Vault Usage Guide

最適化されたObsidian知識管理システムの使用方法ガイドです。

## 📁 現在のフォルダ構造

### `00_inbox/` - 情報の入口
- **目的**: 新しい情報の一時保管
- **使用法**: クイックキャプチャー、後で分類
- **処理**: 週次レビューで適切な場所に移動

### `01_daily/` - 日次ノート
- **形式**: YYYY-MM-DD.md
- **用途**: 日々の振り返り、進捗記録
- **テンプレート**: Daily Note Template使用推奨

### `02_zettelkasten/` - 知識ネットワーク
- **`concepts/`** - 概念・理論・キーワード
- **`insights/`** - 洞察・発見・アイデア
  - `personal/` - 個人的な気づき
  - `business/` - ビジネス関連
  - `global-challenges/` - グローバル課題DB
- **`connections/`** - 知識間の関連性
- **`index/`** - ナビゲーション用インデックス
  - **[[Knowledge_Network_Map]]** - 中央ハブ

### `10_projects/` - アクティブプロジェクト
- **Aeterlink/** - AI/IoTコンサルティング
- **42Tokyo/** - プログラミング学習
- **english_study.md** - 英語学習プロジェクト
- **README.md** - プロジェクト概要

### `20_areas/` - 継続的責任領域
- **`personal/`** - 個人管理
  - `goals-planning/` - 目標設定・戦略
  - `lifestyle-hobbies/` - ライフスタイル
  - `entertainment-media/` - 娯楽・メディア
- **`business/home-tutor/`** - ホームチューター事業
- **`education/`** - 学習活動
- **`programming/`** - 技術開発
- **`technical/`** - 技術レポート

### `30_resources/` - 参考資料
- **`templates/`** - 標準テンプレート（4種類）
- **`literature/`** - 書籍・文献要約
- **`references/`** - 技術資料・ドキュメント

### `90_archive/` - アーカイブ
- **`duplicates_20250811/`** - 重複ファイル保管
- **`optimization_docs_archive_20250817/`** - 古い最適化ドキュメント
- 完了プロジェクト・非アクティブ資料

### `99_meta/` - システム管理
- **`scripts/`** - メンテナンススクリプト
- **`docs/`** - システムドキュメント（簡素化済み）
- **`logs/`** - 最適化ログ

## 🔗 知識ネットワークの使い方

### 中央ハブの活用
**[[Knowledge_Network_Map]]** から全てのコンテンツにアクセス：
- 目標設定ネットワーク: Vision → Life Strategy → AI起業計画
- ビジネス機会: Global Challenges → 市場調査 → 事業計画
- 技術スキル: 42Tokyo → プログラミング → 実装

### 関連ノートの構築
```markdown
> **関連ノート**: [[Vision]] | [[Life Strategy]] | [[やりたいこと]]
```

### メタデータの活用
```yaml
---
tags: [personal-development, habits, goals, lifestyle]
related: [Vision, 石野絆：AI起業による売上100万円達成計画]
---
```

## 🎯 日常的なワークフロー

### 1. 朝のルーティン
1. [[Knowledge_Network_Map]] で今日の焦点確認
2. [[Vision]] → 具体的目標の確認
3. Daily Noteで今日のタスク設定

### 2. 情報取り込み
1. 新情報は `00_inbox/` に即座保存
2. 週末に適切なフォルダに分類
3. 関連ノートにリンク追加

### 3. プロジェクト管理
1. アクティブ作業は `10_projects/` で管理
2. 継続的活動は `20_areas/` で追跡
3. 完了時は `90_archive/` に移動

### 4. 知識構築
1. 新概念は `02_zettelkasten/concepts/` で定義
2. 洞察は `insights/` カテゴリで記録
3. 相互リンクで知識ネットワーク強化

## 🛠️ メンテナンス

### 週次レビュー（推奨：日曜日）
- [ ] Inbox整理
- [ ] プロジェクト進捗更新
- [ ] 完了項目のアーカイブ
- [ ] 来週の計画作成

### 月次最適化
- [ ] リンク整合性チェック: `python3 99_meta/scripts/check_broken_links.py`
- [ ] ファイル名最適化: `python3 99_meta/scripts/enhanced_uuid_cleanup.py`
- [ ] 知識ネットワーク強化

## 📊 Dataview活用例

### プロジェクトダッシュボード
```dataview
TABLE status, deadline
FROM "10_projects"
WHERE status != "completed"
SORT deadline ASC
```

### 最近の洞察
```dataview
LIST
FROM "02_zettelkasten/insights"
SORT file.mtime DESC
LIMIT 5
```

## 🎉 成功指標

- **整理された情報**: Inbox定期的にゼロ
- **活発な知識ネットワーク**: 関連ノート間の豊富なリンク
- **明確な進捗**: プロジェクト・目標の可視化
- **効率的な検索**: タグとメタデータの活用

---

このシステムで情報整理・知識蓄積・目標達成を統合的に管理できます。