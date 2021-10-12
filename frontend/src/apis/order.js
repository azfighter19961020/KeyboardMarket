import axios from 'axios'
import {host,port} from '@/apis/constant.js'

export function createOrderData(username,token){
  return axios.post(`http://${host()}:${port()}/userorder`,{
    "username":username
  },{
    headers:{
      "AUTHORIZATION":token
    }
  })
}

export function captureOrder(orderID,token){
  return axios.post(`http://${host()}:${port()}/userorder/capture/${orderID}`,{
    headers:{
      "AUTHORIZATION":token
    }
  })
}

export function getAllOrderData(username,token){
  return axios.get(`http://${host()}:${port()}/userorder`,{
    params:{
      "username":username
    },
    headers:{
      "AUTHORIZATION":token
    }
  })
}

export function getDetailOrderData(username,token,orderno){
  return axios.get(`http://${host()}:${port()}/userorder/${orderno}`,{
    params: {
      "username":username
    },
    headers:{
      "AUTHORIZATION":token
    }
  })
}