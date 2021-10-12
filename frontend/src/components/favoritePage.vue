<template>
	<html lang="zh-Hant-TW">
		<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
		<link rel="icon" type="image/x-con" href="@/assets/favicon.ico">
		<div id="app">
			<headerComponent></headerComponent>
			<div id="favoriteHeader" style="width:100%;height:100px;background-image: linear-gradient(to right,#C9C9C9,#F2FFFF,#00E6E6);padding-top: 40px;">
				<h3>按讚好物</h3>
			</div>
			<b-row>
				<b-col cols="2" v-for="item in items" :key="item.id" style="margin: 20px;border:1px solid #5B5B5B;padding: 10px;text-align: center;box-shadow:3px 3px 12px #4F4F4F;border-radius: 30px;">
					<a :href="'/#/productDetail/' + item.product.id">
						<img :src="'http://localhost:8000' + item.product.img" alt="" style="width: 200px;height: 200px;">
					</a>
					<h4 class="productTitle">
						{{ item.product.name }}
					</h4>
					<h5 class="productPrice">
						{{ item.product.price }}
					</h5>
					<div>
						<b-button variant="danger" @click="cancel(item.product.id)">
							取消按讚
						</b-button>
					</div>
				</b-col>
			</b-row>
		</div>

	</html>
</template>

<script>
  import { getAllFavorite,addFavorite } from '@/apis/favorite.js'
  import { STATUS_OK } from '@/apis/constant.js'
  export default{
    name: "favoritePage",
    components:{
      'headerComponent':() => import('@/components/header.vue')
    },
    data(){
      return {
        items:[
          {
            "id":1,
            "username":"admin123",
            "product":{
              "id":3,
              "name":"耳機",
              "price":123,
              "stored_amount":12,
              "img":"/media/productImage/airpod.png"
            }
          }
        ]
      }
    },
    created(){
      var token = window.localStorage.getItem("token")
      var username = window.localStorage.getItem("username")
      if(token == null || username == null){
        this.$fire({type:"error",text:"請登入"}).then(() => {
          location.href = "/#/login"
        })
      }
      getAllFavorite(username,token).then((response) => {
        if(response.data.code == STATUS_OK){
          this.items = response.data.data
        }else{
          this.$fire({type:"error",text:response.data.data})
        }
      })
    },
    methods:{
      cancel(data){
        var token = window.localStorage.getItem("token")
        var username = window.localStorage.getItem("username")
        var pid = data
        addFavorite(pid,token,username).then((response) => {
          if(response.data.code == STATUS_OK){
            this.items.forEach((item,index) => {
              if(item.product.id == pid){
                this.items.splice(index,1)
              }
            })
          }
        })
      }
    }
  }
</script>