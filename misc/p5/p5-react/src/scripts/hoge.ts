import p5 from "p5";

export const Hoge = (p: p5) => {
  p.setup = () => {
    p.createCanvas(400, 400);
  };

  p.draw = () => {
    for (let i = 1; i < 10; i++) {
      p.ellipse(50 + i * 10, 50 + i * 10, 80 + i * 10, 80 + i * 10);
    }
  };
};
