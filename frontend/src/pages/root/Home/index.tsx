import './index.scss'
import TopNav from '@/components/TopNav'
import MapViewer from '@/components/MapViewer'

export default function Home() {
    return (
        <div>
            <h1>Welcome to the Home Page</h1>
            <p>This is the main landing page of the application.</p>
            <TopNav 
                className='top-nav'
            >
                {/* 顶部导航栏 */}
            </TopNav>
            <MapViewer 
                className='main-map'
            >
                {/* 地图 */}
            </MapViewer>
        </div>
    )
}
