import './index.scss'
import type { CSSProperties } from 'react';

interface MapViewerProps {
    className?: string;
    style?: CSSProperties;
}

export default function MapViewer({ 
    className, style
 }: MapViewerProps) {
    return (
        <div
            className={className}
            style={style}
        >
            <h1>MapViewer</h1>
        </div>
    )
}
