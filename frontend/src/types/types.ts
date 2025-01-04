export interface Product {
    product_id: number;
    name: string;
    description: string;
    price: number;
    discount: number;
    stock: number;
    sku: string;
    category: number;
    images: Record<string, string>;
    dimensions: {
        length: number;
        width: number;
        height: number;
    };
    weight: number;
    created_at: string;
}
