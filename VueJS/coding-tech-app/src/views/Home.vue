<template>
  <div>
    <div class="row">
      <div class="col s6">
        <!-- Form  -->
        <PostForm/>
      </div>
    </div>
    <div class="row">
      <div class="col s6" v-for='(post, index) in posts'
      v-bind:item="post"
      :index="index"
      :key="post.id"
      >
        <div class="card">
          <div class="card-content">
            <p class="card-title">
              {{ post.title }}
            </p>
            <p class="timestamp">
              {{ post.createdAt }}
            </p>
            <p>{{ post.body }}</p>
          </div>
          <div class="card-action">
            <a href="#" class="btn-edit">Edit</a>
            <a href="#" class="btn-delete">Delete</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import PostForm from '@/components/PostForm';

import PostService from '../PostService';
const postService = new PostService();

export default {
  name: 'Home',
  components: {
    PostForm
  },
  data() {
    return {
      posts: []
    }
  },
  created() {
    postService.getAllPost()
              .then(res => {
                this.posts = res.data
              }).catch(error => console.log("==== ERROR", error))
  }
}
</script>

<style scoped>
  .card .card-content .card-title {
    margin-bottom: 0;
  }

  .card .card-content .timestamp {
    color: #999;
    margin-bottom: 10px;
  }

  .btn-delete {
    color: red !important;
  }
</style>
