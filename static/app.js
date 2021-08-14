
const app = new Vue({
    el: "#app",
    delimiters: ['[[', ']]'],
    data: {
        message: 'this is working',
        added: false,
        quantity: null,
        cart: null,
        categories: [],
        products: []
    },
    mounted(){
        this.getCategories()
        this.getCart()
    },
    methods: {
        getCategories: async function() {
            const res = await axios.post('/graphql/', {
                query: `{allCategories{id name sub_category{id name}}}`
            });
            this.categories = res.data.data.allCategories;
        },

        toCategory: function(cat_id, sub_id) {
          window.location.href = `/category/${cat_id}`
        },

        getCart: async function() {
            const res = await axios.post('/graphql/', {
                query: `{
                          cart{
                            count
                            summary
                          }
                        }`
            });
            this.cart = res.data.data.cart;
        },

        addToCart: async function (id, quantity) {
            const res = await axios.get(`/cart/add-item/${id}/${quantity}`);
            alert('product added to cart');
            this.getCart();
        }
    }

});