const API_URL = "http://localhost:5000/api";

let modoEdicao = false;

function mostrarLoading(mostrar) {
  const loading = document.getElementById("loadingAlunos");
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

async function carregarAlunos() {
  mostrarLoading(true);

  try {
    const response = await fetch(`${API_URL}/alunos`);
    const alunos = await response.json();

    exibirAlunos(alunos);
    atualizarEstatisticas();
  } catch (error) {
    console.error("Erro ao carregar alunos:", error);
    mostrarAlerta(
      "Erro ao carregar alunos. Verifique se a API está rodando.",
      "error"
    );
  } finally {
    mostrarLoading(false);
  }
}

function exibirAlunos(alunos) {
  const tabela = document.getElementById("tabelaAlunos");
  const corpo = document.getElementById("corpoTabela");
  const emptyState = document.getElementById("emptyState");

  corpo.innerHTML = "";

  if (alunos.length === 0) {
    tabela.classList.add("hidden");
    emptyState.classList.remove("hidden");
    return;
  }

  tabela.classList.remove("hidden");
  emptyState.classList.add("hidden");

  alunos.forEach((aluno) => {
    const linha = document.createElement("tr");
    linha.innerHTML = `
            <td>${aluno.Matricula}</td>
            <td>${aluno.Nome}</td>
            <td>${aluno.Idade}</td>
            <td>${aluno.Genero}</td>
            <td>${aluno.Curso}</td>
            <td>${aluno.Periodo}</td>
            <td>
                <div class="table-actions">
                    <button class="btn btn-warning btn-small" onclick="editarAluno(${aluno.Matricula})">✏️ Editar</button>
                    <button class="btn btn-danger btn-small" onclick="excluirAluno(${aluno.Matricula}, '${aluno.Nome}')">🗑️ Excluir</button>
                </div>
            </td>
        `;
    corpo.appendChild(linha);
  });
}

async function atualizarEstatisticas() {
  try {
    const response = await fetch(`${API_URL}/alunos/relatorio`);
    const relatorio = await response.json();

    document.getElementById("totalAlunos").textContent = relatorio.total;
    document.getElementById("mediaIdade").textContent =
      relatorio.media_idade.toFixed(1);
  } catch (error) {
    console.error("Erro ao carregar estatísticas:", error);
  }
}

function abrirModalAdicionar() {
  modoEdicao = false;
  document.getElementById("modalTitulo").textContent = "Adicionar Aluno";
  document.getElementById("formAluno").reset();
  document.getElementById("alunoMatricula").value = "";
  document.getElementById("modalAluno").classList.add("active");
}

function fecharModal() {
  document.getElementById("modalAluno").classList.remove("active");
  document.getElementById("formAluno").reset();
}

async function salvarAluno(event) {
  event.preventDefault();

  const dados = {
    Nome: document.getElementById("alunoNome").value,
    Idade: document.getElementById("alunoIdade").value,
    Genero: document.getElementById("alunoGenero").value,
    Curso: document.getElementById("alunoCurso").value,
    Periodo: document.getElementById("alunoPeriodo").value,
  };

  try {
    let response;

    if (modoEdicao) {
      const matricula = document.getElementById("alunoMatricula").value;
      response = await fetch(`${API_URL}/alunos/${matricula}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(dados),
      });
    } else {
      response = await fetch(`${API_URL}/alunos`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(dados),
      });
    }

    if (response.ok) {
      mostrarAlerta(
        modoEdicao
          ? "Aluno atualizado com sucesso!"
          : "Aluno adicionado com sucesso!",
        "success"
      );
      fecharModal();
      carregarAlunos();
    } else {
      mostrarAlerta("Erro ao salvar aluno", "error");
    }
  } catch (error) {
    console.error("Erro ao salvar aluno:", error);
    mostrarAlerta("Erro ao salvar aluno", "error");
  }
}

async function editarAluno(matricula) {
  try {
    const response = await fetch(`${API_URL}/alunos/${matricula}`);
    const aluno = await response.json();

    modoEdicao = true;
    document.getElementById("modalTitulo").textContent = "Editar Aluno";
    document.getElementById("alunoMatricula").value = aluno.Matricula;
    document.getElementById("alunoNome").value = aluno.Nome;
    document.getElementById("alunoIdade").value = aluno.Idade;
    document.getElementById("alunoGenero").value = aluno.Genero;
    document.getElementById("alunoCurso").value = aluno.Curso;
    document.getElementById("alunoPeriodo").value = aluno.Periodo;

    document.getElementById("modalAluno").classList.add("active");
  } catch (error) {
    console.error("Erro ao carregar aluno:", error);
    mostrarAlerta("Erro ao carregar dados do aluno", "error");
  }
}

async function excluirAluno(matricula, nome) {
  if (!confirm(`Tem certeza que deseja excluir o aluno ${nome}?`)) {
    return;
  }

  try {
    const response = await fetch(`${API_URL}/alunos/${matricula}`, {
      method: "DELETE",
    });

    if (response.ok) {
      mostrarAlerta("Aluno excluído com sucesso!", "success");
      carregarAlunos();
    } else {
      mostrarAlerta("Erro ao excluir aluno", "error");
    }
  } catch (error) {
    console.error("Erro ao excluir aluno:", error);
    mostrarAlerta("Erro ao excluir aluno", "error");
  }
}

async function buscarAlunos() {
  const termo = document.getElementById("searchInput").value;

  if (!termo) {
    carregarAlunos();
    return;
  }

  mostrarLoading(true);

  try {
    const response = await fetch(
      `${API_URL}/alunos/buscar?termo=${encodeURIComponent(termo)}`
    );
    const alunos = await response.json();

    exibirAlunos(alunos);

    if (alunos.length === 0) {
      mostrarAlerta("Nenhum aluno encontrado", "info");
    }
  } catch (error) {
    console.error("Erro ao buscar alunos:", error);
    mostrarAlerta("Erro ao buscar alunos", "error");
  } finally {
    mostrarLoading(false);
  }
}

async function gerarRelatorio() {
  try {
    const response = await fetch(`${API_URL}/alunos/relatorio`);
    const relatorio = await response.json();

    let mensagem = `📊 RELATÓRIO GERAL DE ALUNOS\n\n`;
    mensagem += `Total de alunos: ${relatorio.total}\n`;
    mensagem += `Média de idade: ${relatorio.media_idade} anos\n\n`;
    mensagem += `Alunos por curso:\n`;

    for (const [curso, qtd] of Object.entries(relatorio.cursos)) {
      mensagem += `  • ${curso}: ${qtd} aluno(s)\n`;
    }

    alert(mensagem);
  } catch (error) {
    console.error("Erro ao gerar relatório:", error);
    mostrarAlerta("Erro ao gerar relatório", "error");
  }
}

document.addEventListener("DOMContentLoaded", () => {
  const searchInput = document.getElementById("searchInput");
  if (searchInput) {
    searchInput.addEventListener("keypress", (e) => {
      if (e.key === "Enter") {
        buscarAlunos();
      }
    });
  }
});

carregarAlunos();
