# Socket Programming in Python

Sockets and the socket API are used to send messages across a network.
They provide a form of inter-process communication (IPC).

> Sockets と socket API はネットワークを通じたメッセージ送信に用いられる
> それらは IPC と呼ばれるフォームを与えます

The network can be a logical, local network to the computer,
or one that’s physically connected to an external network,
with its own connections to other networks.
The obvious example is the Internet, which you connect to via your ISP.

> ネットワークは論理的に、ローカルネットワークから PC に
> 外部ネットワークと物理的な接続をしたり、
> もしくは他のネットワークとのコネクションを作ります
> わかりやすい例示としては ISP とコネクションを取るものです

In this tutorial, you’ll create:

- A simple socket server and client
- An improved version that handles multiple connections simultaneously
- A server-client application that functions like a full-fledged socket
  application, complete with its own custom header and content

> 単純な Socket サーバーと Client
> 同時に複数のコネクションを扱うサーバー
> サーバークライアントアプリ を実装します
> 一人前のソケットアプリのような関数 カスタムのヘッダーと内容を持った

By the end of this tutorial, you’ll understand how to use the main
functions and methods in Python’s socket module to write your own
client-server applications.

> チュートリアルの終わりには
> メイン関数やメソッドの使い方を理解しているでしょう
> 自分で書いて CS アプリの Python のソケットモジュールの

You’ll know how to use a custom class to send messages and data between
endpoints, which you can build upon and utilize for your own applications.

> エンドポイント間でメッセージやデータのやり取りを行うカスタムのクラス
> の使い方を知るでしょう
> 自分用のアプリのためにそれらを頼りにしたり、役に立たせる

Networking and sockets are large subjects.
Literal volumes have been written about them.
If you’re new to sockets or networking,
it’s completely normal if you feel overwhelmed
with all of the terms and pieces.

> ネットワークとソケットは大きな分野です
> Literal Volume はそれらについて書かれています(?)
> もしソケットやネットワークが初めてであれば、
> そしてそれらの用語や事事について圧倒される感じがあっても普通やで

Don’t be discouraged though.
This tutorial is for you! As with anything Python-related,
you can learn a little bit at a time.

> 落胆しないで
> このチュートリアルは、あなたのためのものです
> Python に関連することならすべて、少しづつ学んでいけばよいのです

## Socket API Overview

Python's socket module provides an interface to the Berkeley sockets API.
This is the module that you'll use in this tutorial.

> Python's socket module は Berkeley sockets API の Interface を提供します
> このチュートリアルでは以下のモジュールを利用します

The primary socket API functions and methods in this module are:

- socket()
- .bind()
- .listen()
- .accept()
- .connect()
- .connect_ex()
- .send()
- .recv()
- .close()

Python provides a convenient and consistent API that maps directly
to system calls, their C counterparts.
In the next section, you’ll learn how these are used together.

> Python は便利で一貫性のある API を提供します
> システムコールに直接 API をマッピングします

As part of its standard library, Python also has classes that make using
these low-level socket functions easier.
Although it’s not covered in this tutorial, you can check out
the socketserver module, a framework for network servers.

> スタンダードのライブラリは、Python は 低レベルの関数を簡単に
> 使えるようにクラスを持っています
> しかし、このチュートリアルではすべてのカバーしてないので
> socket server module, や network servers のフレームなどをチェックしてね

There are also many modules available that implement higher-level Internet
protocols like HTTP and SMTP.
For an overview, see Internet Protocols and Support.

> HTTP, SMTP のような 高レベルのインターネット・プロトコルなどの実装が
> 利用可能なモジュールがたくさんあります
> Internet Protocols と Support 等見ようぜ

## TCP Sockets

You're going to create a socket object using `socket.socket()`,
specifying the socket type as `socket.SOCK_STREAM`.
When you do that, the default protocol that's used is the TCP.
This is a good default and probably what you want.

> socket.socket() を用いて socket object を作ります
> socket.SOCK_STREAM というタイプです
> socket を作る際　デフォルトのプロトコルは TCP を使います
> こは良いデフォルトであり、おそらくあなたが求めているものです

Why should you use TCP? The Transmission Control Protocol (TCP):

> なぜ TCP が使うべきでしょう, TCP です

- Is reliable: Packets dropped in the network are detected
  and retransmitted by the sender.

- Has in-order data delivery: Data is read by your application
  in the order it was written by the sender.

> 信頼性がある： ネットワークでドロップしたパケットを検出し
> 送信者によって再送信します
> 配送データが順序通り：データはアプリケーションによっては
> 送信者によって書き込まれた順序 データを読み取ります

In contrast, User Datagram Protocol (UDP) sockets created with
`socket.SOCK_DGRAM` aren’t reliable, and data read by the receiver
can be out-of-order from the sender’s writes.

> 一方で、UDP socket は `socket.SOCK_DGRAM` を用いて作られますが
> 信頼性はありませんし
> 受診者によって読み取られるデータは 送信者の書き込みから無順序で
> 読み取られます

Why is this important? Networks are a best-effort delivery system.
There’s no guarantee that your data will reach its destination
or that you’ll receive what’s been sent to you.

> なぜこれが重要なんでしょうか？
> ネットワークは ベストエフォート配送方式です
> データが 相手に届くかどうか もしくは相手が送ったものが
> あなたに届くかどうかは保証がありません

Network devices, such as routers and switches,
have finite bandwidth available and come with their own inherent
system limitations.

> ネットワークのデバイスは（ルーター、スイッチなど）
> は利用できる帯域幅は有限です そして、システムの限界があります

They have CPUs, memory, buses, and interface packet buffers,
just like your clients and servers.

> CPUs, memory, buses, や packet buffers のインタフェースは
> クライアントやサーバーのようなものです

TCP relieves you from having to worry about packet loss,
out-of-order data arrival, and other pitfalls that invariably happen
when you’re communicating across a network.

> ネットワークを通じた通信を行ったときに
> TCP は〜を和らげます パケットロスや、順不定でデータが届いたり、
> 他の落とし穴 を気にする必要がなくなります

![TCP](https://files.realpython.com/media/sockets-tcp-flow.1da426797e37.jpg)

the API calls that the server makes to set up a “listening” socket:

- socket()
- .bind()
- .listen()
- .accept()

A listening socket does just what its name suggests.
It listens for connections from clients.
When a client connects, the server calls `.accept()` to accept,
or complete, the connection.

> Listening socket はその名前が指し示す通りのことを行います
> クライアントからのコネクションを 聞きます
> クライアントがコネクトしたときは
> サーバーは .accept() で コネクションを accept, complete を呼びます

The client calls `.connect()` to establish a connection to the server
and initiate the three-way handshake.

> クライアントから .connect() を呼びます サーバーにコネクションを確立
> するときに そして 3-way handshake を初期化します

The handshake step is important because it ensures that each side
of the connection is reachable in the network,
in other words that the client can reach the server and vice-versa.
It may be that only one host, client, or server can reach the other.

> 3-way handshake step は重要です なぜなら
> これはネットワークのサーバーとクライアントのコネクションの
> 両サイドの 到着を保証するからです

In the middle is the round-trip section,
where data is exchanged between the client and server
using calls to `.send()` and `.recv()`.

> 真ん中の `rount-trip`セクション では
> データーは C to S の間で `send()` `recv` を用いてデータの交換を行います

At the bottom, the client and server close their respective sockets.

最後は C, S の両方で それぞれの socket をクローズします
