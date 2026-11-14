document.querySelector('#toggle_header').addEventListener('click', () => {
  const header = document.querySelector('header');
  header.className = header.classList.contains('red') ? 'green' : 'red';
});
