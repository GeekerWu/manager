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

}
export function loadinit () {
  return axios({
    url: api.loadinit,
    method: 'get',
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

