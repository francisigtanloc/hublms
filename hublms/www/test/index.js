frappe.ready(() => {
    alert('Hello World!');
    let questions = [
        {
            text: 'What is 1 + 1?',
            options: ['1', '2', '3', '4'],
            correctAnswer: '2'
        },
        {
            text: 'What is 2 + 2?',
            options: ['2', '3', '4', '5'],
            correctAnswer: '4'
        },
        {
            text: 'What is 3 + 3?',
            options: ['3', '6', '9', '12'],
            correctAnswer: '6'
        },
        {
            text: 'What is 4 + 4?',
            options: ['4', '8', '12', '16'],
            correctAnswer: '8'
        },
        {
            text: 'What is 5 + 5?',
            options: ['5', '10', '15', '20'],
            correctAnswer: '10'
        }
    ];

    let currentQuestionIndex = 0;
    let questionStatus = questions.map(() => 'unanswered');

    function renderQuestion() {
        let questionContainer = $('#quiz-container');
        questionContainer.empty();

        let question = questions[currentQuestionIndex];
        let questionElement = $('<div></div>');

        let questionText = $('<h2></h2>').text(question.text);
        questionElement.append(questionText);

        for (let i = 0; i < question.options.length; i++) {
            let option = $('<input>').attr({
                type: 'radio',
                name: `question${currentQuestionIndex}`,
                value: question.options[i]
            });
            let label = $('<label></label>').text(question.options[i]);
            questionElement.append(option, label, $('<br>'));
        
            option.on('change', function() {
                if (this.value === question.correctAnswer) {
                    questionStatus[currentQuestionIndex] = 'correct';
                } else {
                    questionStatus[currentQuestionIndex] = 'incorrect';
                }
            });
        }

       

        questionContainer.append(questionElement);
    }

    function renderPagination() {
        let paginationContainer = $('#pagination');
        paginationContainer.empty();

        for (let i = 0; i < questions.length; i++) {
            let button = $('<button></button>');

            if (questionStatus[i] === 'unanswered') {
                button.css('background-color', 'gray');
            } else if (questionStatus[i] === 'correct') {
                button.css('background-color', 'green');
            } else {
                button.css('background-color', 'red');
            }

            button.on('click', function () {
                currentQuestionIndex = i;
                renderQuestion();
                renderPagination();
            });

            paginationContainer.append(button);
        }
    }

    $('#prev').on('click', function () {
        if (currentQuestionIndex > 0) {
            currentQuestionIndex--;
            renderQuestion();
            renderPagination();
        }
    });

    $('#next').on('click', function () {
        if (currentQuestionIndex < questions.length - 1 && questionStatus[currentQuestionIndex] !== 'unanswered') {
            currentQuestionIndex++;
            renderQuestion();
            renderPagination();
        }
    });

    renderQuestion();
    renderPagination();
});