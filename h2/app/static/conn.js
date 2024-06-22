const { MongoClient } = require('mongodb');
const { Cursor } = require('mongoose');

const uri = "mongodb+srv://HYDRATION_PASS:PASS_HYDRATION@cluster0.ggf7zs1.mongodb.net/tyu";

MongoClient.connect(uri, (err, database) => { 
  db = database.db('HYDRATION'); 
if(!err){
  console.log("connected");
}
else{
  console.log(err);
}});
