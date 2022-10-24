import { nanoid } from "nanoid";

export class LinkType {
  link: string;
  shorten_link: string;

  constructor(link: string) {
    this.link = link;
    this.shorten_link = this.shorten();
  }

  shorten(): string {
    return nanoid();
  }
}
