
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
      getProducts: function () {
          const res = axios({
              method: "POST",
              data: {
                  query: `
                  {allProducts{id name price discount image}}
                  `
              }
          }).then( res => {
             this.products = res.data.data.allProducts;
          }).catch(err => {
              console.log(err);
          });
      }
    }
});