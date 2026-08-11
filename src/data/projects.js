/**
 * REALTEK ENGINEERING PTE. LTD. — Project Portfolio Data Architecture
 * 
 * Instructions for Owners & Developers:
 * - Genuine Projects: Set `isDemo: false`.
 * - Temporary Demo Projects: Set `isDemo: true`.
 * - Photos: Place project images in /public/projects/<project-id>/ and reference paths here.
 * - Note: Technology Products (ezyHR, ezyBooks, ezyCRM) are showcased separately under Technology Products / ezy SaaS.
 */

export const projectCategories = [
    { id: 'all', label: 'All Engineering Projects' },
    { id: 'solar', label: 'Solar & Renewable Energy' },
    { id: 'electrical', label: 'Electrical Engineering' },
    { id: 'industrial', label: 'Industrial Engineering' }
];

export const projectsData = [
    {
        id: 'changi-business-park-solar',
        title: 'Changi Business Park Solar Grid',
        category: 'solar',
        categoryLabel: 'Solar & Renewable Energy',
        location: 'Changi Business Park, Singapore',
        year: 'Details being updated',
        status: 'Project details being updated',
        description: 'Project details will be updated upon confirmation by REALTEK ENGINEERING PTE. LTD.',
        scope: [],
        specifications: {},
        highlights: [],
        images: [
            '/projects/changi-business-park-solar/main.svg'
        ],
        featured: true,
        isDemo: false
    },
    {
        id: 'demo-solar-installation',
        title: 'DEMO PROJECT — Rooftop Solar Array Installation',
        category: 'solar',
        categoryLabel: 'Solar & Renewable Energy',
        location: 'Jurong Industrial Estate, Singapore (Sample)',
        year: '2025 (Sample)',
        status: 'DEMO / SAMPLE',
        description: 'Sample layout representing industrial rooftop solar array installation, cabling routing, and inverter panel integration.',
        scope: [
            'Sample structural mounting layout',
            'Sample DC/AC cabling tray management',
            'Sample inverter integration & monitoring'
        ],
        specifications: {
            'System Type': 'Rooftop Solar PV (Sample)',
            'Mounting': 'Ballasted Frame (Sample)',
            'Status': 'DEMO LAYOUT ONLY'
        },
        highlights: [
            'Sample solar layout presentation',
            'Demonstrates portfolio detail capabilities'
        ],
        images: [
            '/projects/demo-solar-installation/main.svg',
            '/projects/demo-solar-installation/detail1.svg'
        ],
        featured: false,
        isDemo: true
    },
    {
        id: 'demo-electrical-works',
        title: 'DEMO PROJECT — Industrial Control Panel & E&I Works',
        category: 'electrical',
        categoryLabel: 'Electrical Engineering',
        location: 'Tuas Industrial Zone, Singapore (Sample)',
        year: '2025 (Sample)',
        status: 'DEMO / SAMPLE',
        description: 'Sample layout representing high-voltage electrical control panel assembly, power distribution, and instrumentation wiring.',
        scope: [
            'Sample control panel assembly & wiring',
            'Sample high-density cable tray installation',
            'Sample power distribution panel testing'
        ],
        specifications: {
            'Voltage Rating': 'Industrial E&I (Sample)',
            'Enclosure': 'IP66 Rated Panel (Sample)',
            'Status': 'DEMO LAYOUT ONLY'
        },
        highlights: [
            'Sample electrical control panel presentation',
            'Demonstrates portfolio detail capabilities'
        ],
        images: [
            '/projects/demo-electrical-works/main.svg',
            '/projects/demo-electrical-works/detail1.svg'
        ],
        featured: false,
        isDemo: true
    },
    {
        id: 'demo-commercial-solar',
        title: 'DEMO PROJECT — Commercial Facility Solar System',
        category: 'solar',
        categoryLabel: 'Solar & Renewable Energy',
        location: 'Woodlands Industrial Park, Singapore (Sample)',
        year: '2025 (Sample)',
        status: 'DEMO / SAMPLE',
        description: 'Sample layout representing commercial warehouse rooftop solar integration and power management system.',
        scope: [
            'Sample commercial roof assessment & mounting',
            'Sample solar grid connection wiring',
            'Sample system performance testing'
        ],
        specifications: {
            'Facility': 'Commercial Warehouse (Sample)',
            'Inverter': 'Central Inverter System (Sample)',
            'Status': 'DEMO LAYOUT ONLY'
        },
        highlights: [
            'Sample commercial solar layout',
            'Demonstrates portfolio grid presentation'
        ],
        images: [
            '/projects/demo-commercial-solar/main.svg',
            '/projects/demo-commercial-solar/detail1.svg'
        ],
        featured: false,
        isDemo: true
    },
    {
        id: 'demo-industrial-panel',
        title: 'DEMO PROJECT — Industrial Automation & Cable Routing',
        category: 'industrial',
        categoryLabel: 'Industrial Engineering',
        location: 'Gul Circle, Singapore (Sample)',
        year: '2025 (Sample)',
        status: 'DEMO / SAMPLE',
        description: 'Sample layout representing industrial automation panel wiring, sensor instrumentation, and structural cable management.',
        scope: [
            'Sample automation PLC panel integration',
            'Sample sensor & transducer wiring',
            'Sample containment & trunking installation'
        ],
        specifications: {
            'System': 'Industrial PLC & Containment (Sample)',
            'Location': 'Factory Floor (Sample)',
            'Status': 'DEMO LAYOUT ONLY'
        },
        highlights: [
            'Sample industrial automation layout',
            'Demonstrates technical specification structure'
        ],
        images: [
            '/projects/demo-industrial-panel/main.svg',
            '/projects/demo-industrial-panel/detail1.svg'
        ],
        featured: false,
        isDemo: true
    }
];
