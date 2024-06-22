const mongoose=require("mongoose")
const client=mongoose.connect("mongodb+srv://HYDRATION_PASS:PASS_HYDRATION@cluster0.ggf7zs1.mongodb.net/HYDRATION", 
    {
        useNewUrlParser: true,
    useUnifiedTopology: true
});
if(client)
{
    console.log("Succesfully connected to Database");
}
//console.log("connected");
    const sch ={
        FirstName :{type:String,required:true},
        LastName :{type:String,required:true},
        PhoneNo :{type:Number,required:true,unique:true},
        password :{type:String,required:true},
        ConfirmPassword :{type:String,required:true},
    }
    const monmodel =mongoose.model("user_signup", sch);
    module.exports=monmodel;


    