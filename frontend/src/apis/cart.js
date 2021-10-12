import axios from 'axios'
import { host,port } from '@/apis/constant.js'

export function getCartData(username,token){
  return axios.get(`http://${host()}:${port()}/usercart/${username}`,{
    headers: {
      "AUTHORIZATION":token
    }
  })
}

export function addCartData(data,token){
  return axios.post(`http://${host()}:${port()}/usercart`,data,{
    headers:{
      "AUTHORIZATION":token
    }
  })
}

export function fixCartData(data,token){
   return axios.put(`http://${host()}:${port()}/usercart`,data,{
     headers:{
       "AUTHORIZATION":token
     }
   })
}

export function deleteCartData(cid,token){
   return axios.delete(`http://${host()}:${port()}/usercart/${cid}`,{
     headers:{
       "AUTHORIZATION":token
     }
   })
}

