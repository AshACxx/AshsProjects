<?php
/**
 * All editable site content lives here.
 * Change names, links, and text in this file — you shouldn't need to
 * touch index.php or style.css just to update your info.
 */

$profile = [
    'name'       => 'Arshdip Chera',
    'role'       => 'Data Science &amp; AI Engineering Student',
    'tagline'    => 'Interested in data analytics, machine learning, and building practical, intelligent systems.',
    'cv_path'    => 'assets/cv.pdf', // drop your CV file at this path
    'email'      => 'you@example.com',
    'linkedin'   => 'https://www.linkedin.com/in/your-handle',
    'github'     => 'https://github.com/your-handle',
];

$about = [
    "I'm a Data Science and AI Engineering student at Technological University Dublin (TU Dublin), currently studying TU850.",
    "I'm interested in using data, artificial intelligence, and software development to solve real-world problems and build practical, intelligent systems.",
    "Through my course, I've been developing a strong foundation in programming, databases, data analysis, machine learning, software design, and web development. I've worked with a range of programming languages, data tools, and development technologies, and I'm continuing to build my understanding of how data can be collected, analysed, visualised, and used within AI and software applications.",
    "I also have experience with software development tools and workflows such as Git and GitHub, as well as modelling and design tools used in software engineering.",
    "I'm particularly interested in Data Science, AI Engineering, Machine Learning, and Software Development. My goal is to keep gaining hands-on experience, contribute to meaningful projects, and grow into a skilled Data Science and AI professional.",
];

$skills = [
    'Python', 'SQL', 'C', 'R', 'PHP', 'HTML',
    'Git', 'GitHub', 'TensorFlow', 'Tableau', 'Orange', 'StarUML',
];

// Add or edit projects here — one array item per project card.
$projects = [
    [
        'title' => 'Machine Learning Project',
        'tags'  => 'Python · TensorFlow',
        'desc'  => 'A short line on what the project predicts or classifies, and the result that matters most.',
        'link'  => '#',
        'icon'  => 'ml', // ml | data
    ],
    [
        'title' => 'Tableau Analytics Project',
        'tags'  => 'Tableau · SQL',
        'desc'  => 'A short line on the dataset, the question you were answering, and what the dashboard shows.',
        'link'  => '#',
        'icon'  => 'data',
    ],
];

$education = [
    [
        'when'  => '2022 — Present',
        'title' => 'BSc (Hons) Data Science &amp; AI Engineering — TU850',
        'org'   => 'Technological University Dublin (TU Dublin)',
    ],
];

// Optional — add roles here as you gain experience; leave empty to hide the section.
$experience = [
    // [
    //     'when'  => '2025',
    //     'title' => 'Job Title',
    //     'org'   => 'Company Name',
    //     'desc'  => 'One line on what you did.',
    // ],
];
