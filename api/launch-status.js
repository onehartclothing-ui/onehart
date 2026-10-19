// Vercel serverless function: returns authoritative launch timing for AFTER DARK — HALLOWEEN EDITION.
// Timezone: Asia/Kolkata (IST = UTC+5:30)
// Target launch: 20 October 2026, 00:00:00 Asia/Kolkata

const LAUNCH_ISO = '2026-10-20T00:00:00+05:30';
const LAUNCH_TIMESTAMP = Date.parse(LAUNCH_ISO); // 1792434600000

export default function handler(req, res) {
  // Prevent all edge and browser caching to ensure instant launch visibility
  res.setHeader('Cache-Control', 'no-store, no-cache, must-revalidate, proxy-revalidate, max-age=0');
  res.setHeader('Pragma', 'no-cache');
  res.setHeader('Expires', '0');

  // Allow optional simulated test clock via query param (e.g. ?sim_time=2026-10-20T00:00:05+05:30)
  // For staging/testing only without modifying production server clock.
  let now = Date.now();
  if (req.query && req.query.sim_time) {
    const parsed = Date.parse(req.query.sim_time);
    if (!isNaN(parsed)) now = parsed;
  }

  const isLive = now >= LAUNCH_TIMESTAMP;
  const msRemaining = Math.max(0, LAUNCH_TIMESTAMP - now);
  const secondsRemaining = Math.floor(msRemaining / 1000);

  const hours = Math.floor(secondsRemaining / 3600);
  const minutes = Math.floor((secondsRemaining % 3600) / 60);
  const seconds = secondsRemaining % 60;

  return res.status(200).json({
    collection: 'AFTER DARK — HALLOWEEN EDITION',
    launchTime: LAUNCH_ISO,
    launchTimestamp: LAUNCH_TIMESTAMP,
    serverTimestamp: now,
    timeZone: 'Asia/Kolkata',
    isLive,
    secondsRemaining,
    countdown: {
      hours: String(hours).padStart(2, '0'),
      minutes: String(minutes).padStart(2, '0'),
      seconds: String(seconds).padStart(2, '0')
    }
  });
}
