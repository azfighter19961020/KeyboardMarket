<template>
	<html lang="zh-Hant-TW">
	<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
	<link rel="icon" type="image/x-con" href="@/assets/favicon.ico">
		<div id="app">
			<headerComponent></headerComponent>
			<div id="selfHeader" style="width:100%;height:100px;background-image: linear-gradient(to right,#C9C9C9,#F2FFFF,#00E6E6);padding-top: 40px;">
				<h3>個人資料</h3>
			</div>
			<b-row align-h="center" style="margin-top:10px;">
				<b-col cols="3">
					<div id="userImage" style="border-radius: 10px 100px;width: 80%;height: 80%;overflow: hidden;">
						<img :src="'http://localhost:8000' + avatarURL" alt="" style="max-width: 100%;max-height: 100%;">
					</div>
					<b-form-file v-model="avatar"></b-form-file>
					<b-button variant="info" @click="uploadAvatar">修改大頭貼</b-button>
				</b-col>
				<b-col cols="7">
					<b-form-group
					label="用戶名稱"
					label-for="username"
					>
						<b-form-input v-model="username" id="username">
						</b-form-input>
					</b-form-group>
					<b-form-group
					label="地址"
					label-for="address"
					>
						<b-form-input v-model="address" id="address"></b-form-input>
					</b-form-group>
					<b-form-group
					label="電話"
					label-for="phone"
					>
						<b-form-input v-model="phone" id="phone"></b-form-input>
					</b-form-group>
					<br>
					<br>
					<b-button @click="onSubmit" variant="info">修改</b-button>
				</b-col>
			</b-row>
		</div>
	</html>
</template>

<script>
  import { getdata,fixdata,uploadImage } from '@/apis/users.js'
  import { STATUS_OK } from '@/apis/constant.js'
  export default{
    name: "selfPage",
    components: {
      'headerComponent':() => import('@/components/header.vue')
    },
    data(){
      return {
        username:"",
        address: "",
        phone: "",
        avatar:null,
        isLogin:false,
        avatarURL:""
      }
    },
    methods: {
      uploadAvatar(){
        var token = window.localStorage.getItem('token')
        var username = window.localStorage.getItem('username')
        let formData = new FormData()
        formData.append('avatar',this.avatar)
        formData.append('username',username)
        uploadImage(formData,token).then((response) => {
          if(response.data.code == STATUS_OK){
            this.$fire({type:'success',text:'上傳成功'}).then(() => {
              window.location.reload()
            })
          }else{
            this.$fire({type:'error',text:response.data.data})
          }
        })
      },
      onSubmit(){
        var data = {
          "username":this.username,
          "address":this.address,
          "phone":this.phone
        }
        var token = window.localStorage.getItem('token')
        fixdata(data,token).then((response) => {
          if(response.data.code == STATUS_OK){
            this.$fire({type:'success',text:'更新成功'})
          }else{
            this.$fire({type:'error',text:response.data.data})
          }
        })
      }
    },
    created(){
      var username = window.localStorage.getItem('username')
      var token = window.localStorage.getItem('token')
      if(username != null && token != null){
        getdata(username,token).then((response) => {
          if(response.data.code == STATUS_OK){
            var rdata = response.data.data.data
            console.log(rdata.avatar)
            this.username = rdata.username
            this.phone = rdata.phone
            this.address = rdata.address
            this.avatarURL = rdata.avatar
          }else{
            this.$fire({type:'error',text:response.data.data}).then(() => {
              window.location.href = "/#/login"
              window.location.reload()
            })
          }
        })
      }else{
        this.$fire({type:'error',text:"Please login"}).then(() => {
          window.location.href = "/#/login"
          window.location.reload()
        })
      }
    }
  }
</script>