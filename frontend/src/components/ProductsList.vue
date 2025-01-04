<template>
    <div>
        <h1>Products</h1>
        <ul>
            <li v-for="product in products" :key="product.product_id">
                {{ product.name }} - ${{ product.price }}
            </li>
        </ul>
    </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import API from "@/api/api";
import type { Product } from "@/types/types";

export default defineComponent({
    name: "ProductsList",
    data() {
        return {
            products: [] as Product[],
        };
    },
    mounted() {
        API.get<Product[]>("/products/")
            .then((response) => {
                this.products = response.data;
            })
            .catch((error) => {
                console.error("Error fetching products:", error);
            });
    },
});
</script>
