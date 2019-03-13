const posts = [
    {id: 1, upVotes: 2, title: 'Title 1'},
    {id: 2, upVotes: 89, title: 'Title 2'},
    {id: 3, upVotes: 1, title: 'Title 1'},
    {id: 13, title: 'Title 221'},
    {id: 5, title: 'Title 102'},
    {id: 131, title: 'Title 18'},
    {id: 55, title: 'Title 234'}
];

const totalUpvotes = posts.reduce((acc, currentValue) => acc + currentValue.upVotes, 0);
console.log("totalUpvotes", totalUpvotes);

const integers = [1, 2, 3, 4, 6, 7];

const multipleInteger = integers.map(item => item * 2);
console.log(multipleInteger)

const findPostId = posts.find(i => i.id === 1);
console.log(findPostId);

const evenIntegers = integers.filter(i => i % 2 === 0);

const findIndexWithId = (id) => posts.map(i => i.id).indexOf(id);
console.log(findIndexWithId)

