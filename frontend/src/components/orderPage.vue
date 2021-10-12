<template>
	<html lang="zh-Hant-TW">
	<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
	<link rel="icon" type="image/x-con" href="@/assets/favicon.ico">
		<div id="app">
			<headerComponent></headerComponent>
			<div id="search" style="width: 50%;height: 100px;margin: 0 auto;">
				<b-form @submit="onSearchSubmit" inline>
					<b-row>
						<b-col cols="9">
							<b-form-input
							id="searchText"
							placeholder="搜尋訂單編號"
							v-model="searchText"
							required
							>
							</b-form-input>
						</b-col>
						<b-col cols="1">
							<b-button type="submit" variant="info"><img src="@/assets/search.svg" alt="" style="width:20px;height: 20px;"></b-button>
						</b-col>
					</b-row>
				</b-form>
			</div>
			<div id="orderList">
				<b-row>
					<b-col cols="1">
						<span>sort by</span>
					</b-col>
					<b-col cols="3">
						<b-form-select
						id="sortOrder"
						:options="[{ text: '排序', value: null }, '日期', '編號', '商品數量']"
						:value="null"
						v-model="selected"
						></b-form-select>
					</b-col>
				</b-row>
				<b-table striped hover :items="orders" :fields="fields" ref="orderTable" @sort-changed="handleSortChange" :filter="searchText" :filter-function="filterTable">
					<template #cell(orderid)="data">
						<b-button variant="info" @click="renderDetail(data.value)">前往詳情</b-button>
					</template>
				</b-table>
			</div>

		</div>
	</html>
</template>

<script>
  import { getAllOrderData } from '@/apis/order.js'
  import { STATUS_OK } from '@/apis/constant.js'
  export default{
    name: "orderPage",
    components:{
      'headerComponent':() => import('@/components/header.vue')
    },
    data(){
      return {
        isLogin:false,
        searchText:"",
        selected:null,
        fields:[{key:"orderno",label:"訂單編號"},{key:"detail",label:"詳情"},{key:"date",label:"日期"},{key:"orderId",label:"前往"}],
        orders:[
          {
            orderno:"0a00b0c",
            detail: "耳機 x1 ...",
            date: "2021-09-17 01:45 a.m.",
            orderId:"1"
          }
        ]
      }
    },
    watch:{
      selected:function(newSelected){
        console.log(newSelected)
        this.$refs.orderTable.$emit('sort-changed')
      }
    },
    created(){
      var username = window.localStorage.getItem("username")
      var token = window.localStorage.getItem("token")
      if(username != null && token != null){
        getAllOrderData(username,token).then((response) => {
          var orderid = 0
          console.log(response.data.data)
          if(response.data.code == STATUS_OK){
            this.orders = []
            response.data.data.data.forEach((item) =>{
              this.orders.push({
                orderno:item.orderno,
                detail: item.products.map((x) => x.name).join() + "...",
                products:item.products,
                date: item.created_time,
                orderId: orderid,
                amount: item.amount
              })
              orderid = orderid + 1
            })
          }else{
            this.$fire({type:"error",text:response.data})
          }
        })
      }else{
        this.$fire({type:"error",text:"請登入!"}).then(() => {
          window.location.href = "/#/login"
          window.location.reload()
        })
      }
    },
    methods: {
      filterTable(row,filter){
        if(row.orderno.includes(filter) || 
          row.detail.includes(filter) ||
          row.date.toString().includes(filter) ||
          row.orderId.toString().includes(filter) ||
          row.amount.toString().includes(filter)){
          return true
        }
        return false
      },
      handleSortChange(){
        console.log("into handle Sort Chagne")
        if(this.selected == "日期"){
          this.orders.sort(function(a,b){
            if(a.date > b.date){
              return 1
            }else if(a.date < b.date){
              return -1
            }
            return 0
          })
        }else if(this.selected == "編號"){
          this.orders.sort(function(a,b){
            if(a.orderno > b.orderno){
              return 1
            }else if(a.orderno < b.orderno){
              return -1
            }
            return 0
          })
        }else if(this.selected == "商品數量"){
          this.orders.sort(function(a,b){
            return a.amount - b.amount
          })
        }
      },
      onSearchSubmit(){
        alert("on searchSubmit!")
      },
      renderDetail(orderid){
        this.orders.forEach((item) => {
          if(item.orderId == orderid){
            location.href = `/#/orderDetail/${item.orderno}`
          }
        })
      }
    }
  }
</script>