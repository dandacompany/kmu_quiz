document.addEventListener("DOMContentLoaded", function () {
	const nextButton = document.getElementById("next-button");
	const submitButton = document.getElementById("submit-button");
	const questionSlides = document.querySelectorAll(".question-slide");
	let currentQuestionIndex = 0;
	let userAnswers = [];
	const totalQuestions = questionSlides.length;

	function showQuestion(index, direction = "right") {
		const currentSlide = questionSlides[currentQuestionIndex];
		const nextSlide = questionSlides[index];

		// 현재 슬라이드 이동
		currentSlide.classList.add(
			direction === "right" ? "slide-left" : "slide-right"
		);
		currentSlide.classList.remove("active", "slide-center");

		// 다음 슬라이드 준비
		nextSlide.classList.add(
			direction === "right" ? "slide-right" : "slide-left"
		);
		nextSlide.style.display = "block";

		// 강제 리플로우
		nextSlide.offsetWidth;

		// 다음 슬라이드 이동
		nextSlide.classList.add("active", "slide-center");
		nextSlide.classList.remove("slide-right", "slide-left");

		currentQuestionIndex = index;

		if (index === totalQuestions - 1) {
			nextButton.style.display = "none";
			submitButton.style.display = "block";
		} else {
			nextButton.style.display = "block";
			submitButton.style.display = "none";
		}
	}

	function saveAnswer() {
		const currentSlide = questionSlides[currentQuestionIndex];
		const selectedRadio = currentSlide.querySelector(
			'input[type="radio"]:checked'
		);
		if (!selectedRadio) {
			alert("정답을 선택해주세요.");
			return false;
		}
		const currentQuestion =
			currentSlide.querySelector(".question-text").textContent;
		const correctAnswerInput = currentSlide.querySelector(
			'input[type="radio"][data-is-correct="true"]'
		);
		const correctAnswer = correctAnswerInput.dataset.content;
		userAnswers[currentQuestionIndex] = {
			questionId: currentSlide
				.querySelector('input[type="radio"]')
				.name.split("_")[1],
			selectedId: selectedRadio.value,
			selectedAnswer: selectedRadio.dataset.content,
			isCorrect: selectedRadio.dataset.isCorrect === "true",
			question: currentQuestion,
			correctAnswer: correctAnswer,
		};
		return true;
	}

	nextButton.addEventListener("click", function () {
		if (saveAnswer() && currentQuestionIndex < totalQuestions - 1) {
			showQuestion(currentQuestionIndex + 1, "right");
		}
	});

	submitButton.addEventListener("click", function () {
		saveAnswer();
		const correctAnswers = userAnswers.filter(
			(answer) => answer && answer.isCorrect
		).length;
		const score = (correctAnswers / totalQuestions) * 100;

		localStorage.setItem(
			"quizScore",
			JSON.stringify({
				correctAnswers: correctAnswers,
				totalQuestions: totalQuestions,
				score: score,
			})
		);
		localStorage.setItem("userAnswers", JSON.stringify(userAnswers));

		const testId = document.getElementById("test_id").value;
		const sessionId = document.getElementById("session_id").value;
		window.location.href = `/quiz/${testId}/result/${sessionId}/`;
	});

	// 선택지 클릭 시 시각적 피드백 제공
	document.querySelectorAll(".selection-box").forEach((box) => {
		box.addEventListener("click", function () {
			const currentSlide = this.closest(".question-slide");
			currentSlide
				.querySelectorAll(".selection-box")
				.forEach((b) => b.classList.remove("selected"));
			this.classList.add("selected");
			this.querySelector('input[type="radio"]').checked = true;
		});
	});

	// 초기 질문 표시
	showQuestion(currentQuestionIndex);
});
