import React from "react";
import p5 from "p5";

export const Canvas = (props: any) => {
  React.useEffect(() => {
    new p5(props.sketch);
  }, [props]);
  return (
    <>
      <h1>Canvas</h1>
    </>
  );
};
