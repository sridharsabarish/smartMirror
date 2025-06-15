export default function DateTime() {

  const date = new Date();
  const current_time = date.toLocaleTimeString();
  const date_today = date.toLocaleDateString();

  return (
    <div >
    <p style={{ backgroundColor: 'ivory' }}>
        Last updated: {current_time}, {date_today}
    </p>
</div>
  );
}