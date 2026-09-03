<?php require __DIR__ . '/data.php'; ?>
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title><?= htmlspecialchars($profile['name']) ?> — Portfolio</title>
<meta name="description" content="<?= htmlspecialchars($profile['tagline']) ?>">
<link rel="stylesheet" href="style.css">
</head>
<body>

<nav class="nav">
  <div class="wrap">
    <a class="nav-mark" href="#top"><?= htmlspecialchars($profile['name']) ?></a>
    <ul class="nav-links">
      <li><a href="#about">About</a></li>
      <li><a href="#skills">Skills</a></li>
      <li><a href="#projects">Projects</a></li>
      <li><a href="#education">Education</a></li>
      <li><a href="#contact">Contact</a></li>
    </ul>
  </div>
</nav>

<header class="hero" id="top">
  <div class="wrap">
    <svg class="hero-axis" viewBox="0 0 320 320" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
      <line x1="20" y1="20" x2="20" y2="300" stroke="#DAD7CE" stroke-width="1"/>
      <line x1="20" y1="300" x2="300" y2="300" stroke="#DAD7CE" stroke-width="1"/>
      <circle cx="70" cy="230" r="4" fill="#2B4FE0"/>
      <circle cx="110" cy="180" r="4" fill="#2B4FE0" opacity="0.7"/>
      <circle cx="150" cy="205" r="4" fill="#2B4FE0" opacity="0.5"/>
      <circle cx="185" cy="120" r="4" fill="#E2A33D"/>
      <circle cx="225" cy="150" r="4" fill="#2B4FE0" opacity="0.6"/>
      <circle cx="260" cy="80" r="4" fill="#2B4FE0"/>
      <circle cx="140" cy="260" r="4" fill="#2B4FE0" opacity="0.4"/>
      <path d="M70 230 L110 180 L150 205 L185 120 L225 150 L260 80" stroke="#1B1D22" stroke-width="1" stroke-dasharray="3 4" opacity="0.35"/>
    </svg>

    <div class="eyebrow-line">TU Dublin · TU850</div>
    <h1><?= htmlspecialchars($profile['name']) ?></h1>
    <p class="role"><?= $profile['role'] ?> &mdash; <?= htmlspecialchars($profile['tagline']) ?></p>

    <div class="hero-cta">
      <a class="btn btn-solid" href="#projects">View Projects</a>
      <a class="btn btn-outline" href="<?= htmlspecialchars($profile['cv_path']) ?>" download>Download CV</a>
    </div>
  </div>
</header>

<hr class="hairline">

<section id="about">
  <div class="wrap about">
    <div class="section-head">
      <h2>About</h2>
    </div>
    <?php foreach ($about as $para): ?>
      <p><?= $para ?></p>
    <?php endforeach; ?>
  </div>
</section>

<hr class="hairline">

<section id="skills">
  <div class="wrap">
    <div class="section-head">
      <h2>Skills</h2>
    </div>
    <ul class="skills-list">
      <?php foreach ($skills as $skill): ?>
        <li><?= htmlspecialchars($skill) ?></li>
      <?php endforeach; ?>
    </ul>
  </div>
</section>

<hr class="hairline">

<section id="projects">
  <div class="wrap">
    <div class="section-head">
      <h2>Featured Projects</h2>
    </div>
    <div class="projects-grid">
      <?php foreach ($projects as $p): ?>
        <div class="project-card">
          <div class="project-thumb">
            <?php if ($p['icon'] === 'ml'): ?>
              <svg viewBox="0 0 120 90" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
                <circle cx="20" cy="20" r="6" fill="none" stroke="#1B1D22" stroke-width="1.5"/>
                <circle cx="20" cy="45" r="6" fill="none" stroke="#1B1D22" stroke-width="1.5"/>
                <circle cx="20" cy="70" r="6" fill="none" stroke="#1B1D22" stroke-width="1.5"/>
                <circle cx="60" cy="30" r="6" fill="none" stroke="#2B4FE0" stroke-width="1.5"/>
                <circle cx="60" cy="60" r="6" fill="none" stroke="#2B4FE0" stroke-width="1.5"/>
                <circle cx="100" cy="45" r="6" fill="#E2A33D"/>
                <g stroke="#5B5F6B" stroke-width="1" opacity="0.6">
                  <line x1="26" y1="20" x2="54" y2="30"/>
                  <line x1="26" y1="20" x2="54" y2="60"/>
                  <line x1="26" y1="45" x2="54" y2="30"/>
                  <line x1="26" y1="45" x2="54" y2="60"/>
                  <line x1="26" y1="70" x2="54" y2="30"/>
                  <line x1="26" y1="70" x2="54" y2="60"/>
                  <line x1="66" y1="30" x2="94" y2="45"/>
                  <line x1="66" y1="60" x2="94" y2="45"/>
                </g>
              </svg>
            <?php else: ?>
              <svg viewBox="0 0 120 90" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
                <line x1="10" y1="10" x2="10" y2="80" stroke="#1B1D22" stroke-width="1.5"/>
                <line x1="10" y1="80" x2="112" y2="80" stroke="#1B1D22" stroke-width="1.5"/>
                <rect x="22" y="50" width="12" height="30" fill="#2B4FE0"/>
                <rect x="42" y="30" width="12" height="50" fill="#2B4FE0" opacity="0.75"/>
                <rect x="62" y="42" width="12" height="38" fill="#2B4FE0" opacity="0.55"/>
                <rect x="82" y="20" width="12" height="60" fill="#E2A33D"/>
              </svg>
            <?php endif; ?>
          </div>
          <div class="project-body">
            <h3><?= htmlspecialchars($p['title']) ?></h3>
            <div class="project-tags"><?= htmlspecialchars($p['tags']) ?></div>
            <p><?= htmlspecialchars($p['desc']) ?></p>
            <a class="project-link" href="<?= htmlspecialchars($p['link']) ?>">View Project &rarr;</a>
          </div>
        </div>
      <?php endforeach; ?>
    </div>
  </div>
</section>

<hr class="hairline">

<section id="education">
  <div class="wrap">
    <div class="section-head">
      <h2>Education</h2>
    </div>
    <ul class="timeline">
      <?php foreach ($education as $e): ?>
        <li>
          <div class="when"><?= htmlspecialchars($e['when']) ?></div>
          <h3><?= $e['title'] ?></h3>
          <p><?= htmlspecialchars($e['org']) ?></p>
        </li>
      <?php endforeach; ?>
    </ul>
  </div>
</section>

<?php if (!empty($experience)): ?>
<hr class="hairline">
<section id="experience">
  <div class="wrap">
    <div class="section-head">
      <h2>Experience</h2>
    </div>
    <ul class="timeline">
      <?php foreach ($experience as $e): ?>
        <li>
          <div class="when"><?= htmlspecialchars($e['when']) ?></div>
          <h3><?= htmlspecialchars($e['title']) ?></h3>
          <p><?= htmlspecialchars($e['org']) ?><?= !empty($e['desc']) ? ' — ' . htmlspecialchars($e['desc']) : '' ?></p>
        </li>
      <?php endforeach; ?>
    </ul>
  </div>
</section>
<?php endif; ?>

<hr class="hairline">

<section id="contact">
  <div class="wrap">
    <div class="section-head">
      <h2>Contact</h2>
    </div>
    <div class="contact-row">
      <a href="<?= htmlspecialchars($profile['linkedin']) ?>" target="_blank" rel="noopener">LinkedIn</a>
      <a href="<?= htmlspecialchars($profile['github']) ?>" target="_blank" rel="noopener">GitHub</a>
      <a href="mailto:<?= htmlspecialchars($profile['email']) ?>"><?= htmlspecialchars($profile['email']) ?></a>
    </div>
  </div>
</section>

<footer>
  <div class="wrap">
    &copy; <?= date('Y') ?> <?= htmlspecialchars($profile['name']) ?>
  </div>
</footer>

</body>
</html>
