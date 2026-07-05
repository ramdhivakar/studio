import { Button } from "@/components/ui/button";

import { AppShell } from "@/components/layout/app-shell";
import { PageContainer } from "@/components/layout/page-container";
import { PageToolbar } from "@/components/layout/page-toolbar";

import { ProductGrid } from "@/features/products/components/product-grid";

export default function ProductsPage() {
  return (
    <AppShell
      title="Products"
      description="Manage enterprise product knowledge."
    >
      <PageContainer>
        <PageToolbar>
          <Button>New Product</Button>
        </PageToolbar>

        <ProductGrid />
      </PageContainer>
    </AppShell>
  );
}
