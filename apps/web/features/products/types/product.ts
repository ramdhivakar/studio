export type Product = {
  id: string;
  name: string;
  description: string;

  stats: {
    articles: number;
    techDocs: number;
    guides: number;
  };
};
