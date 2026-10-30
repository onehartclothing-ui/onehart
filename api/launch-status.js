// Vercel serverless function: returns status for AFTER DARK — HALLOWEEN EDITION (drop ended).

const LAUNCH_ISO = '2026-10-20T00:00:00+05:30';
const LAUNCH_TIMESTAMP = Date.parse(LAUNCH_ISO); // 1792434600000

export default function handler(req, res) {
  res.setHeader('Cache-Control', 'no-store, no-cache, must-revalidate, proxy-revalidate, max-age=0');
  res.setHeader('Pragma', 'no-cache');
  res.setHeader('Expires', '0');

  const now = Date.now();

  return res.status(200).json({
    collection: 'AFTER DARK — HALLOWEEN EDITION',
    launchTime: LAUNCH_ISO,
    launchTimestamp: LAUNCH_TIMESTAMP,
    serverTimestamp: now,
    timeZone: 'Asia/Kolkata',
    isLive: false,
    ended: true,
    secondsRemaining: 0,
    countdown: {
      hours: '00',
      minutes: '00',
      seconds: '00'
    }
  });
}
