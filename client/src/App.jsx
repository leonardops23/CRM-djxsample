import './App.css'
import { BrowserRouter, Routes, Route, Navigate} from "react-router-dom"
import TasksPage from './pages/TasksPage'
import TasksFormPage from './pages/TasksFormPage'
import { Navegations } from './components/Navegations'

function App() {
  return(
    <BrowserRouter>
      <Navegations />
      <Routes>
        <Route path='/' element={ <Navigate to={'/tasks'}/> } />
        <Route path='/tasks' element={<TasksPage />}/>
        <Route path='/tasks-create' element={<TasksFormPage />}/>
        <Route path='/tasks/:id' element={<TasksFormPage />}/>
      </Routes>
    </BrowserRouter>
  )
}
export default App
