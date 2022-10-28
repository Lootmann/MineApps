# how to add new components

## 1. App.tsx

```js
<li>
  <Link to={"/your-routing"}>Add Me</Link>
</li>
```

## 2. index.tsx, add router children

```js
import { Hoge } from "./scripts/hogehgoe";

{
    children: [
      {
        path: "/test",
        element: <Canvas sketch={Hoge} />,
      },
    ],
}
```

## ## 3. scripts/hoge.ts

```js
// Create Your Animations
import p5 from "p5";

export const Circle = (p: p5) => {
  p.setup = () => {};

  p.draw = () => {
    p.ellipse(50, 50, 80, 80);
  };
};
```

## 4. Done :^)
