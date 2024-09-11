document.addEventListener("DOMContentLoaded", function () {
	const quizScore = JSON.parse(localStorage.getItem("quizScore"));
	const userAnswers = JSON.parse(localStorage.getItem("userAnswers"));

	if (quizScore && userAnswers) {
		document.getElementById("total-questions").textContent =
			quizScore.totalQuestions;
		document.getElementById("correct-answers").textContent =
			quizScore.correctAnswers;
		document.getElementById("score").textContent = Math.round(quizScore.score);

		// 문제와 정답 목록 표시
		const questionsAnswersList = document.getElementById(
			"questions-answers-list"
		);
		userAnswers.forEach((answer, index) => {
			if (answer) {
				// null 체크 추가
				const questionElement = document.createElement("div");
				questionElement.innerHTML = `
                    <h3>Q${index + 1}. ${answer.question}</h3>
                    <p>답안: ${answer.correctAnswer}</p>
                    <p>선택: ${answer.selectedAnswer} <span class="${
					answer.isCorrect
						? "correct-answer-indicator"
						: "incorrect-answer-indicator"
				}">${answer.isCorrect ? "O" : "X"}</span></p>
                    <hr>
                `;
				questionsAnswersList.appendChild(questionElement);
			}
		});

		// 결과 표시 후 로컬 스토리지 초기화
		localStorage.removeItem("userAnswers");
		localStorage.removeItem("quizScore");
	} else {
		document.querySelector(".result-container").innerHTML =
			"<p>점수 정보를 찾을 수 없습니다.</p>" +
			"<button id='home-button'>메인으로</button>";
	}

	// 홈으로 버튼 이벤트 리스너 추가
	const homeButton = document.getElementById("home-button");
	if (homeButton) {
		homeButton.addEventListener("click", function () {
			window.location.href = "/"; // 메인 페이지 URL로 변경해주세요
		});
	}
});
