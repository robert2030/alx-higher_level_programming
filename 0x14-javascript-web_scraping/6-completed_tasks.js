#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request.get(apiUrl, function (err, response, body) {
  if (err) {
    console.error(err);
    return;
  }

  const todos = JSON.parse(body);
  const completedTasksByUser = {};

  todos.forEach(todo => {
    if (todo.completed) {
      const userId = todo.userId;
      completedTasksByUser[userId] = (completedTasksByUser[userId] || 0) + 1;
    }
  });

  console.log(completedTasksByUser);
});
