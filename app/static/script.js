const API_URL = "http://127.0.0.1:8000";

async function addQuestion() {
    const questionText = document.getElementById("questionText").value;
    const category = document.getElementById("category").value;

    const response = await fetch(`${API_URL}/questions`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            question_text: questionText,
            category: category
        })
    });

    if (response.ok) {
        alert("Question added successfully");
        document.getElementById("questionText").value = "";
        document.getElementById("category").value = "";
        loadQuestions();
    } else {
        alert("Failed to add question");
    }
}

async function addChoice() {
    const choiceText = document.getElementById("choiceText").value;
    const questionId = Number(document.getElementById("questionId").value);
    const isCorrect = document.getElementById("isCorrect").checked;

    const response = await fetch(`${API_URL}/choices`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            choice_text: choiceText,
            is_correct: isCorrect,
            question_id: questionId
        })
    });

    if (response.ok) {
        alert("Choice added successfully");
        document.getElementById("choiceText").value = "";
        document.getElementById("questionId").value = "";
        document.getElementById("isCorrect").checked = false;
        loadQuestions();
    } else {
        alert("Failed to add choice");
    }
}

async function loadQuestions() {
    const response = await fetch(`${API_URL}/questions`);
    const questions = await response.json();

    const questionsList = document.getElementById("questionsList");
    questionsList.innerHTML = "";

    questions.forEach(question => {
        const card = document.createElement("div");
        card.className = "question-card";

        let choicesHtml = "";

        question.choices.forEach(choice => {
            choicesHtml += `
                <p class="choice">
                    ${choice.choice_text}
                    ${choice.is_correct ? "(Correct)" : ""}
                </p>
            `;
        });

        card.innerHTML = `
            <h3>ID: ${question.id}</h3>
            <p><strong>Question:</strong> ${question.question_text}</p>
            <p><strong>Category:</strong> ${question.category || "None"}</p>
            <h4>Choices:</h4>
            ${choicesHtml || "<p>No choices yet</p>"}
        `;

        questionsList.appendChild(card);
    });
}

loadQuestions();