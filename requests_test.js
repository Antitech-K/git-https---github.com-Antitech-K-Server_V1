const requests = new Request ('http://127.0.0.1/5000/', {
    method: "POST",
    body: '{"foo": "bar"}'});

const url = request.url;
const method = request.method;
const credentials = request.credentials;
const bodyUsed = request.bodyUsed;

console.dir(requests)