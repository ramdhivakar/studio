import { ProductCard } from "./product-card";
import type { Product } from "../types/product";

const products: Product[] = [
  {
    id: "vmware",
    name: "VMware",
    description: "Virtualization and cloud infrastructure.",
    stats: {
      articles: 42,
      techDocs: 18,
      guides: 7,
    },
  },
  {
    id: "symantec",
    name: "Symantec",
    description: "Enterprise security platform.",
    stats: {
      articles: 85,
      techDocs: 33,
      guides: 15,
    },
  },
  {
    id: "carbon-black",
    name: "Carbon Black",
    description: "Endpoint protection and EDR.",
    stats: {
      articles: 21,
      techDocs: 9,
      guides: 4,
    },
  },
];

export function ProductGrid() {
  return (
    <div className="grid gap-5 md:grid-cols-2 xl:grid-cols-3">
      {products.map((product) => (
        <ProductCard key={product.id} product={product} />
      ))}
    </div>
  );
}
