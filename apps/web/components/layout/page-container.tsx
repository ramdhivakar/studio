import { ReactNode } from "react";

type PageContainerProps = {
  children: ReactNode;
};

export function PageContainer({ children }: PageContainerProps) {
  return (
    <section className="mx-auto w-full max-w-7xl px-6 py-6">{children}</section>
  );
}
