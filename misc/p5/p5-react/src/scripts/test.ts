import p5 from "p5";

export const Circle = (p: p5) => {
  p.setup = () => {
    p.createCanvas(400, 400);
  };

  p.draw = () => {
    p.ellipse(50, 50, 80, 80);
  };
};
