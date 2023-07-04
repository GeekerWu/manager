import { axios } from '@/utils/request'

/**
 * login func
 * parameter: {
 *     username: '',
 *     password: '',
 *     remember_me: true,
 *     captcha: '12345'
 * }
 * @param parameter
 * @returns {*}
 */

const api = {
  SendSms: '/account/sms',
  saveinit:'/save_init',
  loadinit:'/load_init',
  deleteinit:'/delete_init',
  poseset:'/pose_set',
  saveanima:'/save_anima',
  updateanima:'/update_anima',
  playanima:'/play_anima',
  deleteanima:'/delete_anima'
}
export function loadinit () {
  return axios({
    url: api.loadinit,
    method: 'get',
  })
}
export function playanima (parameter) {
  return axios({
    url: api.playanima,
    method: 'post',
    data: parameter
  })
}

export function updateanima (parameter) {
  return axios({
    url: api.updateanima,
    method: 'post',
    data: parameter
  })
}
export function saveanima (parameter) {
  return axios({
    url: api.saveanima,
    method: 'post',
    data: parameter
  })
}
export function deleteanima (parameter) {
  return axios({
    url: api.deleteanima,
    method: 'post',
    data: parameter
  })
}


export function deleteinit (parameter) {
  return axios({
    url: api.deleteinit,
    method: 'post',
    data: parameter
  })
}

export function saveinit (parameter) {
  return axios({
    url: api.saveinit,
    method: 'post',
    data: parameter
  })
}

export function poseset (parameter) {
  return axios({
    url: api.poseset,
    method: 'post',
    data: parameter
  })
}


export function login (parameter) {
  return axios({
    url: '/auth/login',
    method: 'post',
    data: parameter
  })
}

export function getSmsCaptcha (parameter) {
  return axios({
    url: api.SendSms,
    data: parameter
  })
}

