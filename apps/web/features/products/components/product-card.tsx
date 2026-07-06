import { Card, CardContent } from "@/components/ui/card";

import type { Product } from "../types/product";

type ProductCardProps = {
  product: Product;
};

export function ProductCard({ product }: ProductCardProps) {
  return (
    <Card className="cursor-pointer transition-all hover:shadow-md">
      <CardContent className="space-y-5 p-6">
        <div>
          <h3 className="text-base font-semibold">{product.name}</h3>

          <p className="mt-1 text-sm text-muted-foreground">
            {product.description}
          </p>
        </div>

        <div className="flex gap-6 text-sm">
          <div>
            <p className="font-semibold">{product.stats.articles}</p>
            <p className="text-muted-foreground">Articles</p>
          </div>

          <div>
            <p className="font-semibold">{product.stats.techDocs}</p>
            <p className="text-muted-foreground">TechDocs</p>
          </div>

          <div>
            <p className="font-semibold">{product.stats.guides}</p>
            <p className="text-muted-foreground">Guides</p>
          </div>
        </div>
      </CardContent>
    </Card>
  );
}
