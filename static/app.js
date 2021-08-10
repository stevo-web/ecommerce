
const app = new Vue({
    el: "#app",
    delimiters: ['[[', ']]'],
    data: {
        message: 'this is working',
        url: 'http://localhost:8000',
        added: false,
        quantity: null,
        cart: {
            count: null,
            summary: null
        },
        products: []
    },
    mounted(){
        this.getCart()
    },
    methods: {
        getCart: async function() {
            const res = await axios(`${this.url}/cart/api`)
            let cart = res.data.split(" ")
            this.cart.count = cart[0]
            this.cart.summary = cart[1]
        },

        addToCart: async function (id, quantity) {
            const res = await axios.get(`/cart/add-item/${id}/${quantity}`);
            alert('product added to cart');
            this.getCart();
        }
    }

});