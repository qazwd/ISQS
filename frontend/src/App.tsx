import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

export default function App() {
  const { count, increment, reset } = useCounter()

  return (
    <>
      <div>
        <LogoLink href="https://vite.dev" src={viteLogo} alt="Vite logo" />
        <LogoLink href="https://react.dev" src={reactLogo} className="react" alt="React logo" />
      </div>
      <h1>Vite + React</h1>
      <div className="card">
        <button onClick={increment}>
          count is {count}
        </button>
        <button onClick={reset} style={{ marginLeft: '1rem' }}>
          Reset
        </button>
        <p>
          Edit <code>src/App.tsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  )
}

const useCounter = () => {
  const [count, setCount] = useState(0)
  
  const increment = () => setCount(prev => prev + 1)
  const reset = () => setCount(0)
  
  return { count, increment, reset }
}

// Logo 链接组件
const LogoLink = ({ href, src, alt, className = "" }: { 
  href: string, 
  src: string, 
  alt: string,
  className?: string 
}) => (
  <a href={href} target="_blank" rel="noopener noreferrer">
    <img src={src} className={`logo ${className}`} alt={alt} />
  </a>
)
