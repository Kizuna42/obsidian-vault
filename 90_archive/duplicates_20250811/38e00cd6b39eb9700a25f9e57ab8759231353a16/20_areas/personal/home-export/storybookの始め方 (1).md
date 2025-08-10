# storybookの始め方 (1)

### できるようになること

- インタラクティブなドキュメント作成
- コンポーネントの表示単体テスト
    - 引数を与えることもできます

### やらないといけないこと

1. 初期設定（`/frontend`内で実行）

```bash
# 関連ライブラリのインストール・セットアップ / 初回のみ
bun i
bun storybook@latest init
```

1. `storybook`の起動

```bash
bun storybook
```

- `/src/stories`内にテスト用ファイルを配置
    - テスト用ファイルは、元のコンポーネントのパス構造を維持してください。
        - 例：`src/commons/Header.tsx` → `stories/commons/Header.stories.tsx`
    - コード作成は、ファイル作成時点でだいたいAIが提案してくれます
        - でなければ、チャットで聞いてみましょう
            - プロンプト例：`添付ファイルのstorybook用テストを書いて`（テスト対象ファイルを選択して）
    - テストコードの例：
    
    ```tsx
    import type { Meta, StoryObj } from '@storybook/react'
    /* テスト対象のインポート */
    import FooterNavigation from '@/commons/FooterNavigation'
    
    const meta = {
    	/* ここのパスが、Storyboookでの表示上のパスになる */
      title: 'Commons/FooterNavigation',
      component: FooterNavigation,
    } satisfies Meta
    
    export default meta
    type Story = StoryObj<typeof meta>
    
    export const Default: Story = {}
    
    export const Variant: Story = {}
    ```
    

### 確認方法

1. `bun storybook`
2. `localhost:6006`に訪れる
3. 左サイドバーからコンポーネントを選択

### **トラブルシューティング**

- コンポーネントが表示されない場合
    - ファイル名が`.stories.tsx`になっているか確認
    - パスのエイリアス（@/）が正しく解決されているか確認
    - コンソールエラーを確認

### １から導入方法

- ほぼこれ [Next.js + Storybook に Tailwind CSSを適用](https://zenn.dev/akky1991/articles/7a8fb3ec6092dc)
1. ライブラリのインストール

```bash
bunx storybook@latest init
```

1. `stories`ディレクトリの移動
    1. デフォルトの`src/stories`だと`next build`が読みにいってしまうので、`stories`を`src`から出す
2. `.storybook`内の編集
    1. `main.ts`
        1. `stories`があるディレクトリを、`2`で移動したところにする
        
        ```bash
          stories: [
            "../stories/**/*.mdx",
            "../stories/**/*.stories.@(js|jsx|mjs|ts|tsx)",
          ],
        ```
        
    2. `preview.ts` 
        1. `tailwindCSS`を`storybook`に読ませるため、以下を挿入
            
            ```tsx
            import '../src/app/globals.css'
            ```
            

### todo

- [x]  1からの導入方法を再現し明確化