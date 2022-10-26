# Vigenere Cipher

## Tier: 1-Beginner

The rate and impact of security breaches in recent years makes it imperative
that developers understand the methods bad actors use to compromise apps.
Understanding how an app can be compromised is the first step in coming up with effective protection measures.

> 近年、セキュリティの落とし穴の衝撃や比率は
> 開発者が 悪意のあるものがアプを侵害する方法を理解することが 必要不可欠です
> どうやってアプリが侵害されるかを理解することは　最初の段階です
> 侵害を衝突する方法を見つけること

One of the easiest ways bad actors can compromise an app is to access data
that's left unencrypted by the developer.
There are a number of strong encryption algorithms available to ensure that data is not readable
even if access is compromised. These include AES, Blowfish, and TripleDES to name a few.

> 悪意のあるものがアプリを侵害する最も簡単な方法の一つが
> 開発者によって 暗号化されずに残しているデータをアクセスする事です

However, these algorithms can be quite complex to implement so the objective of this app
is to implement a classical encryption algorithm, the Vigenere Cipher to learn the basics of how ciphers work.

> しかしながら 多くのアルゴリズムは実装が非常に複雑なので
> このアプリの主目的が 古典的な暗号化のアルゴリズムを実装しましょう
> Vigenere Cipher を例にして どうやって暗号化が動くかを学びましょう

## Requirements & Constraints

- Developers should use only native language features to implement the Vigenere Cipher.
  Libraries are not allowed.

- Developers should design and implement their own solution using only the description of the steps
  in the Vigenere Cipher algorithm.

- After successfully implementing this algorithm Developer should ask themselves these questions:
  - Would you feel confident encrypting your financial information using the Vigenere Cipher? Why?
  - How would you detect that a message had been encrypted using the Vigenere Cipher?
  - How would you go about trying to crack this encryption?

> - Library は使わないで
> - 下の説明にある VCA だけを用いて自分自身で実装してね
> - 実装に成功したあとで、これらの質問をすべきでしょう
>   - Vigenere Cipher を使ってあなたの金融情報を暗号化することについてどう思いますか
>   - Vigenere Cipher を用いて メッセージの暗号化をすること 発見することはどうすんの
>   - 暗号化をクラックすることを試みることはどう

## User Stories

- User can see the app window with these components:

  - Plain text message input field
  - Encryption key input field
  - Action buttons - 'Encrypt' and 'Decrypt'
  - Resulting encrypted or decrypted message

> - 以下の物が必要
>   - input field
>   - 暗号のキー
>   - Encrypt, Decrypt ボタン
>   - 出力

- User can enter the text to be encrypted in the plain text message input field
- User can enter the Encryption key the Vigenere algorithm will use to encrypt the plain text message.
- User can click see see the 'Decrypt' button disabled until the plain text has been encrypted.
- User can click the 'Encrypt' button to encrypt the plain text message
- User can see the encrypted message displayed in the result field.
- User can see the 'Decrypt' button enabled after the encrypted message has been displayed.
- User can click the 'Decrypt' button to decrypt the encrypted message
  and to display its contents in the result field.

> input field に 平文を入力して 暗号化する
> 暗号キーを入力して　 Vigenere algorithm を利用して 平文を暗号にする
> Decrypt ボタンを押して暗号化する
> Encrypt ボタンを押して復号する
> 暗号したメッセージを結果画面に表示する
> Decrypt ボタンを押して暗号化したメッセージを複合します
> で表示

## Bonus features

- User can see a 'Compare' button after decryption that compares the original plain text message
  with the decrypted message
- User can see an error message if the 'Compare' detects differences in the contents of these two fields.

> Compare ボタンを押すと オリジナルの平文と復号した文章を比較する
> どこが違うのかを表示して、エラーメッセージを出せ
