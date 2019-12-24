import axios from 'axios';

axios.defaults.baseURL = 'https://ndb99xkpdk.execute-api.eu-west-2.amazonaws.com/dev';

export default class PostService {
  getAllPost() {
    return axios.get('/posts');
  }

  getPost(number) {
    return axios.get(`/post/${number}`);
  }

  writePost(post) {
    if(post.id) {
      return axios.put(`/post/${post.id}`, post)
    } else {
      return axios.post('/post', post)
    }
  }

  deletePost(id) {
    return axios.delete(`/post/${id}`)
  }
}