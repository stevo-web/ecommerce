
const app = new Vue({
    el: "#app",
    delimiters: ['[[', ']]'],
    data: {
        message: 'this is working',
        products: []
    },
    mounted(){
        this.getProducts();
    },
    methods: {
      getProducts: async function (){
          const res = await axios.post('/graphql/', {
              query:  `{allProducts{id name price discount image}}`
          });
          this.products = res.data.data.allProducts;
      }

    }
});