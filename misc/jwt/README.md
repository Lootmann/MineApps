# JWT

Jwt (ジョット)

## Links

[Introduction](https://jwt.io/introduction)
[Claim](https://www.rfc-editor.org/rfc/rfc7519#section-4.1)

## What is JSON Web Token?

JSON Web Token (JWT) is an open standard (RFC 7519) that defines a compact
and self-contained way for securely transmitting information between parties as a JSON object.
This information can be verified and trusted because it is digitally signed.
JWTs can be signed using a secret (with the `HMAC` algorithm)
or a public/private key pair using `RSA` or `ECDSA`.

> JSON Web Token とは RFC 7519 でオープン標準になっている、
> 簡潔でかつ self-contianed な方法で JSON のオブジェクトの様に情報をセキュアに送信する企画です
> この情報は 電子署名をされているため認証済みでかつ信用できる情報になります
> JWTs は HMAC アルゴリズムを用いて暗号化されるか
> RSA or ECDSA を使い 公開/秘密鍵のペアを用いて署名されます

Although JWTs can be encrypted to also provide secrecy between parties,
we will focus on signed tokens. Signed tokens can verify the integrity of the claims contained within it,
while encrypted tokens hide those claims from other parties.
When tokens are signed using public/private key pairs,
the signature also certifies that only the party holding the private key is the one that signed it.

> JWT は parties(送信者の間?) の間で 秘匿性を確保できる一方で
> 署名されたトークンに注力しています Signed tokens は JWT の中に含まれている claims(?) の
> 正しさを検証できます 暗号化されたトークンを他の人から claims を秘匿化する一方で
> トークンが公開鍵暗号化方式で署名された時
> signature(署名) も 秘密鍵を持っている人・サービスだけから 正しいと証明することが出来ます

## When should you use JSON Web Tokens?

Here are some scenarios where JSON Web Tokens are useful:

> いくつかのシナリオで JWT は有用です

- `Authorization`: This is the most common scenario for using JWT.
  Once the user is logged in, each subsequent request will include the JWT,
  allowing the user to access routes, services, and resources that are permitted with that token.
  Single Sign On is a feature that widely uses JWT nowadays, because of its small overhead
  and its ability to be easily used across different domains.

> 権限: これが最も一般的な JWT の利用先です
> 一旦 user がログインしたら、それぞれのリクエストに JWT をいれます
> そうすると Router やサービス、リソースにアクセスする際にトークンを用いて認証を行えます
> Single Sitn On は 今日 JWT が広く使われている認証技術の一つですが
> その理由は JWT はオーバーヘッドが小さく、そして異なるドメイン領域に渡って簡単に使えからです

- `Information Exchange`: JSON Web Tokens are a good way of securely transmitting information between parties.
  Because JWTs can be signed - for example, using public/private key pairs - you can be sure the senders are
  who they say they are. Additionally, as the signature is calculated using the header and the payload,
  you can also verify that the content hasn't been tampered with.

> 情報交換: JWT は通信物の間でセキュアに情報を送信できる良い方法です
> なぜなら JWT は署名が行えるからです 例えば公開鍵暗号方式を利用するのであれば
> 送信者が誰であるのかを確認することが出来ます それに加えて、header, payload を用いて
> 署名を計算するときに、内容が改ざんされていないことを検証できます

## What is the JSON Web Token structure?

In its compact form, JSON Web Tokens consist of three parts separated
by dots (.), which are

- Header
- Payload
- Signature

Therefore, a JWT typically looks like the following.

`xxxxx.yyyyy.zzzz`

### Header

The header typically consists of two parts: the type of the token,
which is JWT, and the signing algorithm being used,
such as HMAC SHA256(HS256) or RSA.

```json
{
  "alg": "HS256",
  "typ": "JWT"
}
```
