const API_URL = "http://localhost:5000/api";

let modoEdicao = false;
let professorIdAtual = null;

function mostrarLoading(mostrar) {
  const loading = document.getElementById("loadingProfessores");
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

async function carregarProfessores() {
  mostrarLoading(true);

  try {
    const response = await fetch(`${API_URL}/professores`);
    const professores = await response.json();

    exibirProfessores(professores);
    atualizarEstatisticas(professores);
  } catch (error) {
    console.error("Erro ao carregar professores:", error);
    mostrarAlerta(
      "Erro ao carregar professores. Verifique se a API está rodando.",
      "error"
    );
  } finally {
    mostrarLoading(false);
  }
}

function exibirProfessores(professores) {
  const tabela = document.getElementById("tabelaProfessores");
  const corpo = document.getElementById("corpoTabela");
  const emptyState = document.getElementById("emptyState");

  corpo.innerHTML = "";

  if (professores.length === 0) {
    tabela.classList.add("hidden");
    emptyState.classList.remove("hidden");
    return;
  }

  tabela.classList.remove("hidden");
  emptyState.classList.add("hidden");

  professores.forEach((professor, index) => {
    const linha = document.createElement("tr");
    linha.innerHTML = `
            <td>${index + 1}</td>
            <td>${professor.nome}</td>
            <td>${professor.turno}</td>
            <td>${professor.materia}</td>
            <td>
                <div class="table-actions">
                    <button class="btn btn-warning btn-small" onclick="editarProfessor(${index})">✏️ Editar</button>
                    <button class="btn btn-danger btn-small" onclick="excluirProfessor(${index}, '${
      professor.nome
    }')">🗑️ Excluir</button>
                </div>
            </td>
        `;
    corpo.appendChild(linha);
  });
}

function atualizarEstatisticas(professores) {
  document.getElementById("totalProfessores").textContent = professores.length;
}

function abrirModalAdicionar() {
  modoEdicao = false;
  professorIdAtual = null;
  document.getElementById("modalTitulo").textContent = "Adicionar Professor";
  document.getElementById("formProfessor").reset();
  document.getElementById("professorId").value = "";
  document.getElementById("modalProfessor").classList.add("active");
}

function fecharModal() {
  document.getElementById("modalProfessor").classList.remove("active");
  document.getElementById("formProfessor").reset();
}

async function salvarProfessor(event) {
  event.preventDefault();

  const dados = {
    nome: document.getElementById("professorNome").value,
    turno: document.getElementById("professorTurno").value,
    materia: document.getElementById("professorMateria").value,
  };

  try {
    let response;

    if (modoEdicao && professorIdAtual !== null) {
      response = await fetch(`${API_URL}/professores/${professorIdAtual}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(dados),
      });
    } else {
      response = await fetch(`${API_URL}/professores`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(dados),
      });
    }

    if (response.ok) {
      mostrarAlerta(
        modoEdicao
          ? "Professor atualizado com sucesso!"
          : "Professor adicionado com sucesso!",
        "success"
      );
      fecharModal();
      carregarProfessores();
    } else {
      mostrarAlerta("Erro ao salvar professor", "error");
    }
  } catch (error) {
    console.error("Erro ao salvar professor:", error);
    mostrarAlerta("Erro ao salvar professor", "error");
  }
}

async function editarProfessor(id) {
  try {
    const response = await fetch(`${API_URL}/professores/${id}`);
    const professor = await response.json();

    modoEdicao = true;
    professorIdAtual = id;
    document.getElementById("modalTitulo").textContent = "Editar Professor";
    document.getElementById("professorId").value = id;
    document.getElementById("professorNome").value = professor.nome;
    document.getElementById("professorTurno").value = professor.turno;
    document.getElementById("professorMateria").value = professor.materia;

    document.getElementById("modalProfessor").classList.add("active");
  } catch (error) {
    console.error("Erro ao carregar professor:", error);
    mostrarAlerta("Erro ao carregar dados do professor", "error");
  }
}

async function excluirProfessor(id, nome) {
  if (!confirm(`Tem certeza que deseja excluir o professor ${nome}?`)) {
    return;
  }

  try {
    const response = await fetch(`${API_URL}/professores/${id}`, {
      method: "DELETE",
    });

    if (response.ok) {
      mostrarAlerta("Professor excluído com sucesso!", "success");
      carregarProfessores();
    } else {
      mostrarAlerta("Erro ao excluir professor", "error");
    }
  } catch (error) {
    console.error("Erro ao excluir professor:", error);
    mostrarAlerta("Erro ao excluir professor", "error");
  }
}

carregarProfessores();
