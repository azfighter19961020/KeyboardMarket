import { host,port } from '@/apis/constant.js'
import axios from 'axios'

export function getProductFavorite(pid,token,username){
  return axios.get(`http://${host()}:${port()}/favorite/${pid}`,{
    params:{
      "username":username
    },
    headers:{
      "AUTHORIZATION":token
    }
  })
}

export function addFavorite(pid,token,username){
  return axios.post(`http://${host()}:${port()}/favorite`,{
    "username":username,
    "pid":pid
  },{
    headers:{
      "AUTHORIZATION":token
    }
  })
}

export function getAllFavorite(username,token){
  return axios.get(`http://${host()}:${port()}/favorite`,{
    params:{
      "username":username
    },
    headers:{
      "AUTHORIZATION":token
    }
  })
}