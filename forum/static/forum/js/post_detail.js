document.addEventListener("DOMContentLoaded", () => {
    const tooltip = document.querySelector('#tooltip');
    const url = tooltip.dataset.url;

    tooltip.onclick = copyToClipboard;

    function copyToClipboard() {
        navigator.clipboard.writeText(url);
        tooltip.title = 'Copied!!';

        setTimeout(() => {
            tooltip.title = 'Click to copy';
        }, 3000);
    }
});
