<template>
	<html lang="zh-Hant-TW">
		<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
		<link rel="icon" type="image/x-con" href="@/assets/favicon.ico">
		<div id="app">
			<headerComponent></headerComponent>
			<div id="resetHeader" style="width:100%;height:100px;background-image: linear-gradient(to right,#C9C9C9,#F2FFFF,#00E6E6);padding-top: 40px;">
				<h3>重置密碼</h3>
			</div>
			<div id="resetForm" style="width: 50%;height: 500px;">
				<b-form @submit="onSubmit" style="width:100%;">
					<b-form-group
					id="password_group"
					label="密碼:"
					label-for="password"
					style="margin:10px;"
					>
						<b-form-input
						id="password"
						placeholder="請輸入密碼"
						v-model="password"
						required
						>
						</b-form-input>
					</b-form-group>
					<b-form-group
					id="password1_group"
					label="密碼2:"
					label-for="password1"
					style="margin:10px;"
					>
						<b-form-input
						id="password1"
						placeholder="請再次輸入密碼"
						v-model="password1"
						required
						>
						</b-form-input>
					</b-form-group>
					<b-button type="submit" variant="info" style="width: 80px;margin: 10px;">重設</b-button>
				</b-form>
			</div>
		</div>
	</html>
</template>

<script>
  import { resetValidate,resetPassword } from '@/apis/reset.js'
  import { STATUS_OK } from '@/apis/constant.js'
  export default{
    name:"resetPage",
    components:{
      'headerComponent':() => import('@/components/header.vue')
    },
    data(){
      return {
        password:"",
        password1:""
      }
    },
    methods:{
      onSubmit(e){
        e.preventDefault()
        if(this.password != this.password1){
          this.$fire({type:"error",text:"兩次密碼不一致"}).then(() => {
            return
          })
        }
        var token = this.$route.query.token
        resetPassword(this.password,token).then((response) => {
          if(response.data.code == STATUS_OK){
            this.$fire({type:"success",text:"修改密碼成功，將導回登入頁"}).then(() => {
              location.href = "/#/login"
            })
          }else{
            this.$fire({type:"error",text:response.data.data}).then(() => {
              location.href = "/#/index"
            })
          }
        })
      }
    },
    created(){
      var token = this.$route.query.token
      resetValidate(token).then((response) => {
        if(response.data.code == STATUS_OK){
          this.$fire({type:"success",text:"token驗證成功，請進行重置"})
        }else{
          this.$fire({type:"error",text:"Token驗證失敗:" + response.data.data}).then(() => {
            location.href = "/#/index"
          })
        }
      })
    }
  }
</script>