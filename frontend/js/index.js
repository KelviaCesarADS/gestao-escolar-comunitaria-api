const API_URL = "http://localhost:5000/api";

async function gerarRelatorioGeral() {
  try {
    const response = await fetch(`${API_URL}/relatorio-geral`);
    const relatorio = await response.json();

    let mensagem = ` RELATÓRIO GERAL DO SISTEMA\n`;

    mensagem += `RESUMO GERAL\n`;
    mensagem += `Total de alunos: ${relatorio.resumo.total_alunos}\n`;
    mensagem += `Total de turmas: ${relatorio.resumo.total_turmas}\n`;
    mensagem += `Média de idade: ${relatorio.resumo.media_idade} anos\n`;
    mensagem += `Alunos com turma: ${relatorio.resumo.alunos_com_turma}\n`;
    mensagem += `Alunos sem turma: ${relatorio.resumo.alunos_sem_turma}\n\n`;

    mensagem += `ALUNOS POR TURMA\n`;

    if (relatorio.turmas.length === 0) {
      mensagem += `Nenhuma turma cadastrada.\n\n`;
    } else {
      for (const turma of relatorio.turmas) {
        mensagem += `\nTurma ${turma.cod_turma} - ${turma.periodo}\n`;
        mensagem += `  Sala: ${turma.sala} | Turno: ${turma.turno}\n`;
        mensagem += `  Capacidade: ${turma.capacidade} | Matriculados: ${turma.total_alunos}\n`;

        if (turma.alunos.length > 0) {
          mensagem += `  Alunos:\n`;
          for (const aluno of turma.alunos) {
            mensagem += `    • Mat. ${aluno.matricula}: ${aluno.nome} (${aluno.curso})\n`;
          }
        } else {
          mensagem += `  Nenhum aluno matriculado\n`;
        }
      }
    }

    if (relatorio.alunos_sem_turma.length > 0) {
      mensagem += `\n ALUNOS SEM TURMA (${relatorio.alunos_sem_turma.length})\n`;
      for (const aluno of relatorio.alunos_sem_turma) {
        mensagem += `  • Mat. ${aluno.matricula}: ${aluno.nome} (${aluno.curso})\n`;
      }
    }

    alert(mensagem);
  } catch (error) {
    console.error("Erro ao gerar relatório geral:", error);
    alert("Erro ao gerar relatório geral. Verifique se a API está rodando.");
  }
}
