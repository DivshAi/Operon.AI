# AI Agentic Platform - UI Mockups and Style Guide

## Overview
This document provides the visual design specifications and style guide for the AI Agentic Platform. It includes color schemes, typography, iconography, and component designs to ensure consistent user experience across web platform.

## Design Principles

### User-Centered Design
- Intuitive navigation and information architecture
- Accessible interface with WCAG 2.1 compliance
- Responsive design for all device sizes
- Consistent interaction patterns throughout the application

### Visual Design Goals
- Clean, modern aesthetic that conveys professionalism
- Clear visual hierarchy to guide user attention
- Consistent use of color, typography, and spacing
- Visual feedback for user interactions

## Color Palette

### Primary Colors
- **Primary Blue (#007bff)**: Used for primary actions, links, and important UI elements
- **Secondary Gray (#6c757d)**: Used for secondary actions and neutral elements
- **Success Green (#28a745)**: Used for success states, confirmations, and positive feedback
- **Danger Red (#dc3545)**: Used for error states, warnings, and destructive actions

### Neutral Colors
- **Dark Gray (#343a40)**: Used for primary text and headings
- **Medium Gray (#6c757d)**: Used for secondary text and disabled elements
- **Light Gray (#f8f9fa)**: Used for backgrounds and subtle UI elements
- **White (#ffffff)**: Used for main backgrounds and cards

### Status Colors
- **Warning Yellow (#ffc107)**: Used for warnings and cautionary information
- **Info Cyan (#17a2b8)**: Used for informational messages and hints

## Typography

### Font Family
- Primary font: System UI, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif
- Monospace font: Consolas, Monaco, "Courier New", monospace (for code snippets)

### Font Sizes and Weights
- **Heading 1 (H1)**: 1.5rem (24px), Bold (700)
- **Heading 2 (H2)**: 1.25rem (20px), Semi-Bold (600)
- **Heading 3 (H3)**: 1.125rem (18px), Semi-Bold (600)
- **Body Text**: 1rem (16px), Regular (400)
- **Small Text**: 0.875rem (14px), Regular (400)
- **Caption**: 0.75rem (12px), Regular (400)

### Line Heights
- Headings: 1.2
- Body text: 1.5
- Code blocks: 1.6

## Spacing System

### Base Unit
- 0.5rem = 8px (used as the foundation for all spacing)

### Spacing Scale
- **Extra Small**: 0.25rem (4px)
- **Small**: 0.5rem (8px)
- **Medium**: 1rem (16px)
- **Large**: 1.5rem (24px)
- **Extra Large**: 2rem (32px)
- **Double Extra Large**: 3rem (48px)

## Component Design

### Buttons
- **Primary Button**: Blue background (#007bff), white text, rounded corners (4px)
- **Secondary Button**: White background with blue border (#007bff), blue text, rounded corners (4px)
- **Destructive Button**: Red background (#dc3545), white text, rounded corners (4px)
- **Text Button**: Transparent background, blue text (#007bff), no border
- All buttons have hover and active states with appropriate visual feedback

### Cards
- Rounded corners: 8px
- Shadow: Light shadow for depth (0 2px 4px rgba(0,0,0,0.1))
- Padding: 1.5rem (24px) on all sides
- Background: White (#ffffff)

### Forms
- Input fields: Rounded corners (4px), 1px border, padding of 0.75rem (12px)
- Labels: Bold text with appropriate spacing
- Error states: Red border and error message below input
- Focus states: Blue outline around focused elements

### Navigation
- Top navigation bar: Height of 60px, white background (#ffffff)
- Sidebar navigation: Collapsible with appropriate spacing
- Breadcrumb navigation: Light gray background with subtle separators

## Iconography

### Icon Set
- Use consistent icon style throughout the application
- Icons should be clearly recognizable and scalable
- Icons should have appropriate contrast against backgrounds
- All icons should be accessible with proper ARIA labels

### Icon Sizes
- Small: 16px × 16px
- Medium: 24px × 24px
- Large: 32px × 32px

## Responsive Design

### Breakpoints
- **Mobile**: Up to 768px
- **Tablet**: 769px to 1024px
- **Desktop**: 1025px and above

### Grid System
- 12-column responsive grid
- Flexible layouts that adapt to screen size
- Appropriate spacing adjustments for different devices

## Accessibility

### Color Contrast
- All text must meet WCAG 2.1 AA standards (4.5:1 contrast ratio)
- Sufficient color contrast between interactive elements and backgrounds
- Avoid using color alone to convey information

### Keyboard Navigation
- All interactive elements must be accessible via keyboard
- Clear focus indicators for keyboard users
- Logical tab order throughout the application

### Screen Reader Support
- Proper semantic HTML structure
- ARIA attributes where needed
- Descriptive labels for all interactive elements

## UI Patterns

### Dashboard Layout
- Grid-based layout with cards for different information sections
- Consistent use of metrics and visualizations
- Quick access to common actions

### Agent Configuration
- Tabbed interface for different configuration sections
- Visual representation of agent relationships
- Clear status indicators

### Team Management
- Drag-and-drop interface for managing agents
- Visual team structure representation
- Collaborative editing capabilities

### Prompt Repository
- Search and filter capabilities
- Version comparison tools
- Tag-based organization system

## Implementation Guidelines

### CSS Framework
- Utilize Tailwind CSS for consistent styling
- Maintain a consistent component library
- Follow atomic design principles for reusable components

### Component States
- Define clear visual states for all interactive elements:
  - Default state
  - Hover state
  - Active state
  - Focus state
  - Disabled state
  - Error state

### Animation and Feedback
- Subtle animations for transitions between states
- Visual feedback for user actions
- Loading indicators for asynchronous operations

## Design Assets

### Mockup Examples
- Dashboard overview with performance metrics
- Agent creation and configuration interface
- Team management with drag-and-drop functionality
- Prompt repository with versioning capabilities
- User authentication flows

### Style Guide Implementation
- All components should follow the defined style guide
- Consistent use of spacing, typography, and color
- Regular updates to maintain design consistency