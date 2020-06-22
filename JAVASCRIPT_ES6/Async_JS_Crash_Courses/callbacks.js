const posts = [
  { title: "Post One", body: "This is post one" },
  { title: "Post two", body: "This is post two" },
  { title: "Post three", body: "This is post three" }
]

function getPosts() {
  setTimeout(() => {
    let output = "";

    posts.forEach((post, idx) => {
      output += `<li>${post.title}</li>`
    });
    document.body.innerHTML = output;
  }, 1000)
}

function createPost(post, callback) {
  setTimeout(() => {
    posts.push(post);
    callback();
  }, 1500);
}

getPosts();

createPost({ title: "Post Four", body: "I have created new Post"}, getPosts)