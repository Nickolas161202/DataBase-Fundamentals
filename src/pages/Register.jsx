import { useState, useEffect, use } from 'react'
import InputLabel from './components/inputLabel'
import './App.css'
import PrimaryButton from './components/PrimaryButton'

function RegisterPage() {
  const [mail, setusrMail] = useState("")
  const [pwd, setpwd] = useState("")
  const [name, setName] =  useState("")
  
  const post = async (e) => {
    let user = {username: name, email: mail, password: pwd }
    e.preventDefault()
    let res = await fetch('/api/login', {
      method:'POST',
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(user)})
      const data = await res.json()
      console.log(data);
      
  }
  return (
    <>
    <h1>Register</h1>
      <form onSubmit={post}>
        <InputLabel content={"Nome"}/>
        <input type='text'  onChange={(e) => setName(e.target.value)}/>
        <InputLabel content={"email"}/>
        <input type='text'  onChange={(e) => setusrMail(e.target.value)}/>
        <InputLabel content={"password"}/>
        <input type='text' onChange={(e) => setpwd(e.target.value)}/>
        <PrimaryButton label={"Create"}/>
      </form>      
          
          
    </>
  )
}

export default RegisterPage
