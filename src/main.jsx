import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'
import RegisterPage from './pages/Register.jsx'
import { createBrowserRouter, RouterProvider } from 'react-router-dom'
const route =  createBrowserRouter([
  {path: "/", element: <App/>},
  {path: "/register", element: <RegisterPage/>}
])
createRoot(document.getElementById('root')).render(
  <StrictMode>
    <RouterProvider router={route}/>
  </StrictMode>,
)
