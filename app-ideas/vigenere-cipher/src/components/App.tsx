import React from "react";
import { encryption, decryption } from "./cipher";

export function App() {
  const plainTextRef = React.useRef<HTMLInputElement | null>(null);
  const secretTextRef = React.useRef<HTMLInputElement | null>(null);
  const [result, setResult] = React.useState<string>("");

  function doEncrypt(e: React.MouseEvent<HTMLButtonElement>) {
    e.preventDefault();
    const plainText = plainTextRef.current;
    const secret = secretTextRef.current;

    if (!plainText || plainText.value.length === 0) return;
    if (!secret || secret.value.length === 0) return;

    const result = encryption(plainText.value, secret.value);

    setResult(result);
  }

  function doDecrypt(e: React.MouseEvent<HTMLButtonElement>) {
    e.preventDefault();

    const plainText = plainTextRef.current;
    const secret = secretTextRef.current;

    if (!plainText || plainText.value.length === 0) return;
    if (!secret || secret.value.length === 0) return;

    const result = decryption(plainText.value, secret.value);

    setResult(result);
  }

  return (
    <main id="main">
      <h1>Vigenere Cipher</h1>

      <div className="forms">
        <form action="" method="get" className="form">
          <label htmlFor="plain">Plain Text</label>
          <input type="text" name="plain" id="plain" ref={plainTextRef} />

          <label htmlFor="secret">Secret</label>
          <input type="text" name="secret" id="secret" ref={secretTextRef} />

          <div className="buttons">
            <button type="submit" onClick={(e) => doEncrypt(e)}>
              Encrypt
            </button>

            <button type="submit" onClick={doDecrypt}>
              Decrypt
            </button>
          </div>
        </form>

        <form method="get" className="form">
          <label htmlFor="result">Result</label>
          <input
            type="text"
            name="result"
            id="result"
            value={result}
            readOnly
          />
        </form>
      </div>
    </main>
  );
}
