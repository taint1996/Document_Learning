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

function createPost(post) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      posts.push(post);

      const error = false;

      if (!error) {
        resolve();
      } else {
        reject("Error !!!")
      }
    }, 2000);
  })
}

// createPost({ title: "post 4", body: "This post created by me"})
//           .then(getPosts)
//           .catch(err => console.log(err))


// Async / await
// async function init() {
//   await createPost({ title: "post 4", body: "This post created by me"})

//   getPosts();
// }

// init();

// Async / Await with fetch
async function fetchUsers() {
  const res = await fetch("https://jsonplaceholder.typicode.com/users")

  const data = await res.json();
  console.log(data);
}

fetchUsers();



// promise All
// const promise1 = Promise.resolve("Hello");
// const promise2 = 10;
// const promise3 = new Promise((resolve, reject) => {
//   return setTimeout(resolve, 2000, "AAA");
// })

// const promise4 = fetch("https://jsonplaceholder.typicode.com/users").then(res => res.json())
// Promise.all([promise1, promise2, promise3, promise4])
//         .then((values) => console.log(values));