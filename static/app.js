
const app = new Vue({
    el: "#app",
    delimiters: ['[[', ']]'],
    data: {
        message: 'this is working',
        added: false,
        quantity: 1,
        cart: { },
        categories: [],
        products: [],
        counties: []
    },
    mounted(){
        this.getCategories();
        this.getCart();
        this.getCounties();
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
                query: `{cart{count summary items{unit quantity total product{id name image price}}}}`
            });
            this.cart = res.data.data.cart;
        },

        addToCart: async function (id) {
            const res = await axios.post(`/graphql/`, {
                query: `mutation($quantity:Int,$prodId:Int){addToCart(prodId:$prodId,quantity:$quantity){success}}`,
                variables: {
                    prodId: id,
                    quantity: parseInt(this.quantity)
                }
            }
            );
            const success = await res.data.data.addToCart.success;
            if (success){
                this.quantity = 1
            }else{
                console.log('err')
            }
            await this.getCart()
        },
        removeItem: async function (id){
            const res = await axios.post('/graphql/', {
                query: `mutation($prodId:Int){removeItem(prodId:$prodId){success}}`,
                variables: {
                    prodId: id
                }
            });
            await this.getCart()
        },
        updateCart: async function(id, quantity){
            const res = await axios.post('/graphql/', {
                query: `mutation($prodId:Int,$quantity:Int){update(prodId:$prodId,quantity:$quantity){success}}`,
                variables: {
                    prodId: id,
                    quantity: parseInt(quantity)
                }
            })
        },
        getCounties: async function(){
            const res = await axios.post('/graphql/', {
                query: `{allCounties{code name}}`,
            });
            this.counties = res.data.data.allCounties;
        }
    }
});