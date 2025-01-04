import { createRouter, createWebHistory } from "vue-router";
import ProductsList from "@/components/ProductsList.vue";

const routes = [
    {
        path: "/products",
        name: "ProductsList",
        component: ProductsList,
    },
];

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes,
});

export default router;
