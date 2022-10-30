export class TodoModel {
  id: number;
  title: string;

  constructor(id: number, title: string) {
    this.id = id;
    this.title = title;
  }
}

/**
 * parseTitle
 *
 * when TodoModel.title has 'http://*' or https://*',
 * convert string to <a> tag links
 */
export function ParseTitle(title: string, todoId: number): React.ReactNode {
  const result = [];

  for (const chunk of title.split(" ")) {
    if (chunk.startsWith("http://") || chunk.startsWith("https://")) {
      result.push(
        <a
          href={chunk}
          className="todo-url"
          key={todoId}
          target="_blank"
          rel="noopener noreferrer"
        >
          {chunk}
        </a>
      );
    } else {
      result.push(chunk + " ");
    }
  }

  return <>{result}</>;
}
