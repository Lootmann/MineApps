type LinkProps = {
  link: string;
  shorten_link: string;
};

export function Link(props: LinkProps) {
  return (
    <>
      <a href={props.link}>{props.shorten_link}</a>
    </>
  );
}
