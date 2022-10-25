# 剽窃確認アプリ

## Needs

- Scraping
  - Google Search

- Read Doc
  - MS Word document
  - Google Doc

## Impl

1. upload files
2. extract file contents
3. search random words on Google Search
4. Scraping Google Search
5. get searching result's contents
6. check user file and results

## Introduction

You'll be building an automated solution that handles plagiarism detection.
This might be used for publishing companies to replace a manual process
in which they search for phrases from submitted manuscripts on Google to find pre-existing work.

> パクリ確認疑惑を自動で解決アプリ
> Google 上で すでにその文章が存在しているかどうかを確認してください

## Requirements

Your task is to build a web application where a user can upload a file
(e.g. an MS Word document or Google Doc file) and get matches for similar content around the Internet.

> User が upload したファイルを インターネットに似たような内容の物がないかどうかを確認してください

In the back-end, your program should read the content from the uploaded file,
extract some random phrases of around 5-10 words each, and run a Google search on them.

> upload file の 中身を確認 適当な文字を 5 - 10 文字ずつ読んでいき
> それらを google 検索で確認して

The program should then load the pages for each of the top five Google search results
for each phrase and compare the content in that page with the content of the submitted file.

> Google検索の top 5 検索結果に出てきたやつを確認して upload ファイルと称号して

The program should then return a percentage of how similar the content is
and also list the similar phrases and original URLs.

> 検索結果に出たやつをとどれくらい似ているかを確認してください percentage で表示してね
> (文字列検索の面倒なやつ このアルゴリズムは全く知らんので、飛ばす)

More specifically, the program should:

- Consist of a web page where the user can upload a document.
- Extract random phrases from the document.
- Run a Google search against the random phrases.
- Scrape the content from the top five Google search results for each phrase.
  - Clean the scraped content: remove headers etc, and just keep the main text.
- Compare the content of the submitted file with each of the scraped results.
  You can use any text similarity metric, or make this customisable.
- Return a percentage of how similar the uploaded content is to the scraped content.
- Return the similar parts of the content with a link to the original scraped URL.

- For an extra challenge: You can add a PDF generation pipeline that allows the user
  to download the results in a PDF formatted report.

## Suggested Implementation

This project can be implemented with the Python programming language,
the Flask web framework, ScrapingBee or a similar service to scrape Google search results,
and BeautifulSoup to clean the HTML. You can use Bootstrap for the front-end.
