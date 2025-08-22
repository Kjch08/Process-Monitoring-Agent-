
async function fetchProcesses() {
    try {
        const response = await fetch('http://127.0.0.1:8000/api/process-data/');
        const data = await response.json();
        buildTreeTable(data);
    } catch (error) {
        console.error("Error fetching processes:", error);
    }
}

function buildTreeTable(processes) {
    const tbody = document.getElementById('process-table-body');
    tbody.innerHTML = '';

    const processMap = {};
    processes.forEach(proc => processMap[proc.pid] = {...proc, children: []});

    // Build hierarchy
    processes.forEach(proc => {
        if (proc.ppid && processMap[proc.ppid]) {
            processMap[proc.ppid].children.push(processMap[proc.pid]);
        }
    });

    // Render root processes
    Object.values(processMap).forEach(proc => {
        if (!processMap[proc.ppid]) {
            renderRow(proc, tbody, 0);
        }
    });
}

function renderRow(proc, tbody, level, parentRowId = null) {
    const row = document.createElement('tr');
    if (parentRowId) {
        row.classList.add('child');
        row.dataset.parent = parentRowId;
    }

    const rowId = `proc-${proc.pid}`;
    row.dataset.id = rowId;

    // Name with toggle if has children
    const nameCell = document.createElement('td');
    if (proc.children.length > 0) {
        const toggle = document.createElement('span');
        toggle.textContent = '+';
        toggle.className = 'toggle-btn';
        toggle.addEventListener('click', () => toggleChildren(rowId, toggle));
        nameCell.appendChild(toggle);
    } else {
        nameCell.innerHTML = '&nbsp;&nbsp;&nbsp;'; // align with toggle
    }
    const nameText = document.createElement('span');
    nameText.textContent = proc.name;
    nameText.className = 'indent';
    nameText.style.paddingLeft = `${level * 20}px`;
    nameCell.appendChild(nameText);
    row.appendChild(nameCell);

    // Other columns
    const pidCell = document.createElement('td'); pidCell.textContent = proc.pid; row.appendChild(pidCell);
    const ppidCell = document.createElement('td'); ppidCell.textContent = proc.ppid; row.appendChild(ppidCell);
    const hostCell = document.createElement('td'); hostCell.textContent = proc.hostname; row.appendChild(hostCell);
    const cpuCell = document.createElement('td'); cpuCell.textContent = proc.cpu; row.appendChild(cpuCell);
    const memCell = document.createElement('td'); memCell.textContent = proc.memory; row.appendChild(memCell);

    tbody.appendChild(row);

    // Recursively render children
    proc.children.forEach(child => renderRow(child, tbody, level + 1, rowId));
}

function toggleChildren(parentId, toggleBtn) {
    const children = document.querySelectorAll(`tr.child[data-parent='${parentId}']`);
    const isVisible = children.length > 0 && children[0].classList.contains('expanded');
    children.forEach(child => {
        if (isVisible) {
            child.classList.remove('expanded');
            // Also collapse grandchildren
            const grandChildren = document.querySelectorAll(`tr.child[data-parent='${child.dataset.id}']`);
            grandChildren.forEach(gc => gc.classList.remove('expanded'));
        } else {
            child.classList.add('expanded');
        }
    });
    toggleBtn.textContent = isVisible ? '+' : '−';
}

// Start
fetchProcesses();
