const API_URL = "http://localhost:5000/api";

let modoEdicao = false;

function mostrarLoading(mostrar) {
  const loading = document.getElementById("loadingTurmas");
  if (loading) {
    loading.classList.toggle("hidden", !mostrar);
  }
}

function mostrarAlerta(mensagem, tipo = "success") {
  const container = document.getElementById("alertContainer");
  const alert = document.createElement("div");
  alert.className = `alert alert-${tipo}`;
  alert.textContent = mensagem;

  container.appendChild(alert);

  setTimeout(() => {
    alert.remove();
  }, 3000);
}

async function carregarTurmas() {
  mostrarLoading(true);

  try {
    const response = await fetch(`${API_URL}/turmas`);
    const turmas = await response.json();

    exibirTurmas(turmas);
    atualizarEstatisticas(turmas);
  } catch (error) {
    console.error("Erro ao carregar turmas:", error);
    mostrarAlerta(
      "Erro ao carregar turmas. Verifique se a API está rodando.",
      "error"
    );
  } finally {
    mostrarLoading(false);
  }
}

function exibirTurmas(turmas) {
  const tabela = document.getElementById("tabelaTurmas");
  const corpo = document.getElementById("corpoTabela");
  const emptyState = document.getElementById("emptyState");

  corpo.innerHTML = "";

  if (turmas.length === 0) {
    tabela.classList.add("hidden");
    emptyState.classList.remove("hidden");
    return;
  }

  tabela.classList.remove("hidden");
  emptyState.classList.add("hidden");

  turmas.forEach((turma) => {
    const linha = document.createElement("tr");
    linha.innerHTML = `
            <td>${turma.cod_turma}</td>
            <td>${turma.periodo}</td>
            <td>${turma.sala}</td>
            <td>${turma.turno}</td>
            <td>${turma.capacidade}</td>
            <td>
                <div class="table-actions">
                    <button class="btn btn-warning btn-small" onclick="editarTurma(${turma.cod_turma})">✏️ Editar</button>
                    <button class="btn btn-danger btn-small" onclick="excluirTurma(${turma.cod_turma}, '${turma.periodo}')">🗑️ Excluir</button>
                </div>
            </td>
        `;
    corpo.appendChild(linha);
  });
}

function atualizarEstatisticas(turmas) {
  document.getElementById("totalTurmas").textContent = turmas.length;
}

function abrirModalAdicionar() {
  modoEdicao = false;
  document.getElementById("modalTitulo").textContent = "Adicionar Turma";
  document.getElementById("formTurma").reset();
  document.getElementById("turmaCodigo").value = "";
  document.getElementById("modalTurma").classList.add("active");
}

function fecharModal() {
  document.getElementById("modalTurma").classList.remove("active");
  document.getElementById("formTurma").reset();
}

async function salvarTurma(event) {
  event.preventDefault();

  const dados = {
    periodo: document.getElementById("turmaPeriodo").value,
    sala: document.getElementById("turmaSala").value,
    turno: document.getElementById("turmaTurno").value,
    capacidade: parseInt(document.getElementById("turmaCapacidade").value),
  };

  try {
    let response;

    if (modoEdicao) {
      const codigo = document.getElementById("turmaCodigo").value;
      response = await fetch(`${API_URL}/turmas/${codigo}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(dados),
      });
    } else {
      response = await fetch(`${API_URL}/turmas`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(dados),
      });
    }

    if (response.ok) {
      mostrarAlerta(
        modoEdicao
          ? "Turma atualizada com sucesso!"
          : "Turma adicionada com sucesso!",
        "success"
      );
      fecharModal();
      carregarTurmas();
    } else {
      mostrarAlerta("Erro ao salvar turma", "error");
    }
  } catch (error) {
    console.error("Erro ao salvar turma:", error);
    mostrarAlerta("Erro ao salvar turma", "error");
  }
}

async function editarTurma(codigo) {
  try {
    const response = await fetch(`${API_URL}/turmas/${codigo}`);
    const turma = await response.json();

    modoEdicao = true;
    document.getElementById("modalTitulo").textContent = "Editar Turma";
    document.getElementById("turmaCodigo").value = turma.cod_turma;
    document.getElementById("turmaPeriodo").value = turma.periodo;
    document.getElementById("turmaSala").value = turma.sala;
    document.getElementById("turmaTurno").value = turma.turno;
    document.getElementById("turmaCapacidade").value = turma.capacidade;

    document.getElementById("modalTurma").classList.add("active");
  } catch (error) {
    console.error("Erro ao carregar turma:", error);
    mostrarAlerta("Erro ao carregar dados da turma", "error");
  }
}

async function excluirTurma(codigo, periodo) {
  if (!confirm(`Tem certeza que deseja excluir a turma ${periodo}?`)) {
    return;
  }

  try {
    const response = await fetch(`${API_URL}/turmas/${codigo}`, {
      method: "DELETE",
    });

    if (response.ok) {
      mostrarAlerta("Turma excluída com sucesso!", "success");
      carregarTurmas();
    } else {
      mostrarAlerta("Erro ao excluir turma", "error");
    }
  } catch (error) {
    console.error("Erro ao excluir turma:", error);
    mostrarAlerta("Erro ao excluir turma", "error");
  }
}

carregarTurmas();
