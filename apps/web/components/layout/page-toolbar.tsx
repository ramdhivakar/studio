import { ReactNode } from "react";

type PageToolbarProps = {
  children?: ReactNode;
};

export function PageToolbar({ children }: PageToolbarProps) {
  return <div className="mb-6 flex items-center justify-end">{children}</div>;
}
