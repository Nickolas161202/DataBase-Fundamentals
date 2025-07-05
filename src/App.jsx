import { useState, useEffect, use } from 'react'
import InputLabel from './components/inputLabel'
import './App.css'
import PrimaryButton from './components/PrimaryButton'

function App() {
  const [count, setCount] = useState(0)
  const [mail, setusrMail] = useState("")
  const [pwd, setpwd] = useState("")
  const post = async (e) => {
    let user = {username: mail, password: pwd }
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
    <h1>Login</h1>
      <form onSubmit={post}>
        <InputLabel content={"email"}/>
        <input type='text'  onChange={(e) => setusrMail(e.target.value)}/>
        <InputLabel content={"password"}/>
        <input type='text' onChange={(e) => setpwd(e.target.value)}/>
        <PrimaryButton label={"login"}/>
      </form>      
          
          
    </>
  )
}

export default App
