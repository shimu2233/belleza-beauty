# belleza-beauty

個人脱毛サロン **Belleza** の公式ホームページです。Djangoで構築し、Renderにデプロイしています。

- 本番URL: https://belleza-beauty-2.onrender.com/

## 技術スタック

| 項目 | 使用技術 |
| バックエンド | Django 6.0.4 |
| DB | MySQL（`dj_database_url` 経由で `DATABASE_URL` から接続設定を読み込み） |
| 画像ストレージ | Cloudinary（`django-cloudinary-storage`） |
| 静的ファイル配信 | WhiteNoise |
| 本番サーバー | gunicorn |
| フロントエンド | Bootstrap 5.3（CDN） / Google Fonts「Noto Serif JP」 |
| デプロイ先 | Render |

## ディレクトリ構成

```
belleza-beauty/
└── myapp/                      # Djangoプロジェクト本体（実際の作業はここが起点）
    ├── manage.py
    ├── requirements.txt        # 実際にデプロイで使われる依存関係一覧
    ├── myapp/                  # プロジェクト設定（settings.py, urls.py）
    └── belleza/                # メインアプリ
        ├── models.py           # Category, Shop, News
        ├── views.py            # 各ページのビュー
        ├── urls.py             # ルーティング
        ├── templates/belleza/  # 各ページのテンプレート
        └── static/belleza/images/

## ページ構成

`base.html` を共通レイアウトとして、各ページがこれを継承しています。ナビゲーションバーには常時「ご予約はこちら」ボタン（LINE遷移）を表示し、各ページの本文末尾にも同ボタンを共通表示しています。

| URL | ページ | 内容 |
| `/belleza/` | トップページ | `shop_list.html`（`IndexView`）。お店の紹介文＋予約ボタン |
| `/belleza/commitment` | こだわり | 都度払い・カスタマイズ・使用機械をカード形式で紹介 |
| `/belleza/price` | 価格・支払い | 料金表（画像）と支払い方法 |
| `/belleza/questionnaireandbook` | SNS | LINE・InstagramへのリンクSNS一覧 |
| `/belleza/access` | アクセス | 大まかな所在地（詳細は予約後に案内） |
| `/belleza/news` | ビフォーアフター | `News`モデルの一覧。ログインユーザーのみ投稿・編集・削除可 |
| `/belleza/point` | プライバシーポリシー | プライバシーポリシー |
| `/admin/` | Django管理画面 | Shop / Category / News などの管理 |

## ローカルでの動かし方

```bash
cd myapp
python -m venv venv
venv\Scripts\activate        # Windowsの場合
pip install -r requirements.txt
```

以下の環境変数を設定してください（`.env` は `.gitignore` 済み）。

| 変数名 | 用途 |
|---|---|
| `DATABASE_URL` | DB接続文字列（例: `sqlite:///db.sqlite3` でローカルはSQLiteでも可） |
| `CLOUD_NAME` / `API_KEY` / `API_SECRET` | Cloudinaryの認証情報（画像アップロード先） |

```bash
python manage.py migrate
python manage.py createsuperuser   # News投稿用の管理者アカウント作成
python manage.py runserver
```

`settings.py` は `DEBUG = False` 固定になっているため、ローカルで静的ファイルの挙動を本番同様に確認したい場合は `python manage.py collectstatic` を一度実行してください。

## デザインの方向性

- 配色は黒背景（`#111`）＋ゴールド（`#d4af37`）を基調とした高級感のあるテイスト
- 見出しはゴールド、本文は白系（`#e8e8e8`）で可読性を確保
- 予約導線はLINEブランドカラー（`#06C755`）のボタン（`.btn-line`）で統一し、ナビバーと各ページ末尾に常設
- カード表示（`.card-belleza`）を使う場合、BootstrapのCSS変数（`--bs-card-bg` / `--bs-card-color` / `--bs-card-title-color`）を上書きして色を指定する（`.card`側のデフォルト色に負けて文字が見えなくなるため）
- 画像を`img-fluid`でレスポンシブ対応する際は、インラインstyleで固定幅（`width: 500px`など）を指定しないこと（インラインstyleがクラス指定より優先されてしまい、レスポンシブが効かなくなるため）

## 今後のTODO

- トップページ・こだわりページへの実写真の追加（準備中）
