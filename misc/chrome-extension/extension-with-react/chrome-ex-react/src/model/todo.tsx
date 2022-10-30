export class TodoModel {
  id: string;
  title: string;

  constructor(id: string, title: string) {
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
export function ParseTitle(title: string, todoId: string): React.ReactNode {
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
