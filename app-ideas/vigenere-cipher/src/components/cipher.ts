/*
plain: GEEKSFORGEEKS
secret AYUSH

result GCYCZFMLYLEIM
*/

const isAlpha = (ch: string) =>
  ("a" <= ch && ch <= "z") || ("A" <= ch && ch <= "Z");
const isLower = (ch: string) => ch === ch.toLowerCase();
const isUpper = (ch: string) => ch === ch.toUpperCase();

function getCharCode(ch: string): number {
  if (isLower(ch)) {
    return ch.charCodeAt(0) - "a".charCodeAt(0);
  }
  return ch.charCodeAt(0) - "A".charCodeAt(0);
}

/**
 * move the char code of originCh by the char code of moveCh
 *
 * @param originCh string
 * @param moveCh string
 * @param extra boolean - when extra is True, (a, b) => 'z', not 'b'
 * @returns shift string
 */
function rot(originCh: string, moveCh: string, extra: boolean = false): string {
  const originIdx = getCharCode(originCh);
  const moveIdx = getCharCode(moveCh);
  const result = extra
    ? (originIdx - moveIdx + 26) % 26
    : (originIdx + moveIdx) % 26;

  if (!isAlpha(originCh)) return originCh;

  if (isLower(originCh)) {
    return String.fromCharCode(result + "a".charCodeAt(0));
  } else {
    return String.fromCharCode(result + "A".charCodeAt(0));
  }
}

export function encryption(plainText: string, secretKey: string): string {
  let result = "";

  for (let i = 0; i < plainText.length; i++) {
    result += rot(plainText[i], secretKey[i % secretKey.length]);
  }

  return result;
}

export function decryption(encrypedText: string, secretKey: string): string {
  let result = "";

  for (let i = 0; i < encrypedText.length; i++) {
    result += rot(encrypedText[i], secretKey[i % secretKey.length], true);
  }

  return result;
}
