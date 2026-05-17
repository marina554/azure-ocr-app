# Azure OCR App ☁️

---

# English

## Overview

This project is an OCR application that extracts text from images using Azure Document Intelligence.

The application was built with Python and Streamlit, implementing a simple workflow from image upload to OCR execution and text display.

The purpose of this project is to learn OCR technology and API integration in a cloud environment using Azure AI services.

---

## Technologies Used

* Python
* Streamlit
* Microsoft Azure
* Azure Document Intelligence
* OCR
* python-dotenv

---

## Main Features

* Image upload
* OCR execution
* Japanese text extraction
* OCR result display

---

## Application Workflow

### Image Upload

Users can upload image files through the web interface.

### OCR Execution

The application analyzes text in images using Azure Document Intelligence OCR services.

### OCR Result Display

Extracted text is displayed directly on the screen.

---

## Key Implementation Points

* Implemented Japanese OCR using Azure Document Intelligence
* Built a simple and user-friendly UI with Streamlit
* Managed API keys securely using `.env`
* Designed the app to instantly display OCR results
* Integrated cloud-based AI services into the application

---

## Project Structure

```
azure-ocr-app/
├── app.py
├── .env
├── requirements.txt
├── README.md
└── sample.png
```

---

## Setup Instructions

### 1. Clone the Repository

```
git clone <repository-url>
cd azure-ocr-app
```

### 2. Install Required Libraries

```
pip install -r requirements.txt
```

### 3. Create a `.env` File

```
AZURE_ENDPOINT=your_endpoint
AZURE_KEY=your_api_key
```

### 4. Run the Application

```
streamlit run app.py
```

---

## requirements.txt

```
streamlit
azure-ai-formrecognizer
python-dotenv
```

---

## What I Learned

Through this project, I deepened my understanding of:

* How to use Azure AI services
* OCR API integration
* API authentication
* Azure SDK usage
* Simple web app development with Streamlit
* Secure API key management using environment variables
* Basic usage of cloud-based AI services

---

## Future Improvements

* PDF OCR support
* OCR result saving functionality
* Layout analysis
* Table data extraction
* Integration with Azure OpenAI
* OCR accuracy comparison

---

## Background

As I continue studying machine learning and data analysis, I wanted to gain hands-on experience using cloud services and AI APIs.

I chose OCR technology because it has many practical business applications such as workflow automation and document management, and I aim to continue learning AI utilization with Azure.

---

# Japanese

## 概要

Azure Document Intelligence を利用し、画像からテキストを抽出する OCR アプリを作成しました。

本アプリでは、Python と Streamlit を用いて、画像アップロードから OCR 実行・結果表示までをシンプルに実装しています。

Azure の AI サービスを活用し、クラウド環境での OCR 技術や API 利用について学習することを目的として開発しました。

---

## 使用技術

* Python
* Streamlit
* Microsoft Azure
* Azure Document Intelligence
* OCR
* python-dotenv

---

## 主な機能

* 画像アップロード
* OCR 実行
* 日本語テキスト抽出
* OCR結果の画面表示

---

## アプリの流れ

### 画像アップロード

ユーザーが画像ファイルをアップロードできます。

### OCR 実行

Azure Document Intelligence の OCR 機能を利用し、画像内の文字を解析します。

### OCR結果表示

抽出したテキストを画面上に表示します。

---

## 工夫した点

* Azure Document Intelligence を利用し、日本語OCRを実装
* Streamlit を用いてシンプルなUIを構築
* APIキーを `.env` で管理し、セキュリティを意識
* OCR結果を即時確認できる構成にした
* クラウドAIサービスを利用したOCR処理を実装

---

## フォルダ構成

```
azure-ocr-app/
├── app.py
├── .env
├── requirements.txt
├── README.md
└── sample.png
```

---

## セットアップ方法

### 1. リポジトリをクローン

```
git clone <repository-url>
cd azure-ocr-app
```

### 2. ライブラリをインストール

```
pip install -r requirements.txt
```

### 3. `.env` ファイルを作成

```
AZURE_ENDPOINT=your_endpoint
AZURE_KEY=your_api_key
```

### 4. アプリ起動

```
streamlit run app.py
```

---

## requirements.txt

```
streamlit
azure-ai-formrecognizer
python-dotenv
```

---

## 学習したこと

今回の開発を通じて、以下について理解を深めました。

* Azure AI サービスの利用方法
* OCR API の活用
* API認証
* Azure SDK
* Streamlit を用いた簡易Webアプリ開発
* 環境変数によるキー管理
* クラウドAIサービスの基本的な利用方法

---

## 今後の改善案

* PDF OCR 対応
* OCR結果の保存機能
* レイアウト解析
* 表データ抽出
* Azure OpenAI との連携
* OCR精度比較

---

## 背景

機械学習やデータ分析の学習を進める中で、クラウドサービスや AI API を利用した実装経験を深めたいと考え、本アプリを作成しました。

特に OCR 技術は、業務効率化や文書管理など実務での活用機会が多いと考えており、Azure を用いた AI 活用について継続的に学習しています。
