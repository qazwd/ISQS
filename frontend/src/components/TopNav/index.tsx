import './index.scss'
import type { CSSProperties } from 'react';

interface TopNavProps {
    className?: string;
    style?: CSSProperties;
    children?: React.ReactNode;
}

export default function TopNav({ 
    className, style, children
 }: TopNavProps) {
    return (
        <nav 
            className={className}
            style={style}
        >
            {children}
        </nav>
    )
}
