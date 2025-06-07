const viewport = document.getElementById('viewport');
const nodesContainer = document.getElementById('nodes');
const linksContainer = document.getElementById('links');

// Сетка турнира в виде дерева
const treeData = buildTournamentTree(8); // 8 участников

// Настройки камеры
let camera = {
  x: 0,
  y: 0,
  scale: 1,
  isDragging: false,
  lastX: 0,
  lastY: 0
};

// Рисуем узлы и связи
renderTree(treeData);

// Управление камерой
viewport.addEventListener('mousedown', e => {
  if (e.button === 2) { // ПКМ
    camera.isDragging = true;
    camera.lastX = e.clientX;
    camera.lastY = e.clientY;
  }
});

window.addEventListener('mouseup', () => {
  camera.isDragging = false;
});

window.addEventListener('mousemove', e => {
  if (camera.isDragging) {
    const dx = e.clientX - camera.lastX;
    const dy = e.clientY - camera.lastY;
    camera.x += dx;
    camera.y += dy;

    updateCamera();
    camera.lastX = e.clientX;
    camera.lastY = e.clientY;
  }
});

window.addEventListener('wheel', e => {
  const zoomFactor = 0.1;
  const oldScale = camera.scale;
  camera.scale += e.deltaY * -0.001 * zoomFactor;
  camera.scale = Math.max(0.3, Math.min(3, camera.scale));

  // Центрируем масштаб относительно курсора
  const mouseX = e.clientX;
  const mouseY = e.clientY;

  camera.x = mouseX - (mouseX - camera.x) * (camera.scale / oldScale);
  camera.y = mouseY - (mouseY - camera.y) * (camera.scale / oldScale);

  updateCamera();
}, { passive: false });

function updateCamera() {
  viewport.style.transform = `translate(${camera.x}px, ${camera.y}px) scale(${camera.scale})`;
}

// Функция построения турнирной сетки
function buildTournamentTree(participantsCount) {
  const participants = Array.from({ length: participantsCount }, (_, i) => ({
    id: `player${i + 1}`,
    name: `Игрок ${i + 1}`,
    depth: Math.log2(participantsCount)
  }));

  let nodes = [...participants];
  let links = [];

  let currentRound = participants;
  let roundIndex = Math.log2(participantsCount) - 1;

  while (roundIndex >= 0) {
    const nextRound = [];
    for (let i = 0; i < currentRound.length; i += 2) {
      const parent = {
        id: `match${Math.random().toString(36).substr(2, 9)}`,
        name: `Матч ${roundIndex + 1}`,
        depth: roundIndex
      };
      nextRound.push(parent);
      links.push({ source: currentRound[i], target: parent });
      links.push({ source: currentRound[i + 1], target: parent });
    }
    nodes = [...nodes, ...nextRound];
    currentRound = nextRound;
    roundIndex--;
  }

  return { nodes, links };
}

function renderTree(data) {
  const nodeElements = {};
  const widthStep = 200;
  const heightStep = 100;

  data.nodes.forEach(node => {
    const div = document.createElement('div');
    div.className = 'node';
    div.textContent = node.name;
    nodesContainer.appendChild(div);
    node.x = node.depth * widthStep;
    node.y = 0;
    nodeElements[node.id] = div;
  });

  // Распределяем по вертикали
  const depthGroups = {};
  data.nodes.forEach(n => {
    if (!depthGroups[n.depth]) depthGroups[n.depth] = [];
    depthGroups[n.depth].push(n);
  });

  Object.values(depthGroups).forEach(group => {
    group.sort((a, b) => a.id.localeCompare(b.id));
    group.forEach((n, idx) => {
      n.y = idx * heightStep;
    });
  });

  // Обновляем позиции
  data.nodes.forEach(n => {
    const el = nodeElements[n.id];
    el.style.left = `${n.x}px`;
    el.style.top = `${n.y}px`;
  });

  // Рисуем линии
  const svgNS = "http://www.w3.org/2000/svg";
  data.links.forEach(link => {
    const line = document.createElementNS(svgNS, 'line');
    line.setAttribute('class', 'link');
    linksContainer.appendChild(line);
    updateLinkPosition(line, link.source, link.target);
  });

  function updateLinkPosition(line, source, target) {
    line.setAttribute('x1', source.x + 100);
    line.setAttribute('y1', source.y + 20);
    line.setAttribute('x2', target.x);
    line.setAttribute('y2', target.y + 20);
  }
}