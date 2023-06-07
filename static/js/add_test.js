'use strict'

window.onload = () => {
    const questionsContainer = document.getElementById('questions'),
          addQuestionButton  = document.getElementById('add_question_button'); 

    let currentQuestionNumber = 1;

    const questionTemplate = `
        <section class="question" id="question_{{current_number}} name=questions[]">
            <div class="question__title">
                Question {{current_number}}
            </div>

            <div class="options" id="options_{{current_number}}">
                <div class="option">
                    <input class="option__radiobutton" type="radio" name="question_{{current_number}}" value="question_{{current_number}}_option_1">
                    <input class="option__textfield" type="text"  name="text_{{current_number}}_1" id="">
                </div>

                <div class="option">
                    <input class="option__radiobutton" type="radio" name="question_{{current_number}}" value="question_{{current_number}}_option_1">
                    <input class="option__textfield" type="text"  name="text_{{current_number}}_2" id="">
                </div>  

                <div class="option">
                    <input class="option__radiobutton" type="radio" name="question_{{current_number}}" value="question_{{current_number}}_option_1">
                    <input class="option__textfield" type="text"  name="text_{{current_number}}_3" id="">
                </div>  

                <div class="option">
                    <input class="option__radiobutton" type="radio" name="question_{{current_number}}" value="question_{{current_number}}_option_1">
                    <input class="option__textfield" type="text"  name="text_{{current_number}}_4" id="">
                </div>  
            </div>
        </section>
    `;


    function addQuestion() {
        let newQuestion = document.createElement('div'); 
        newQuestion.innerHTML = questionTemplate.replaceAll('{{current_number}}', currentQuestionNumber);
        console.log(questionTemplate.replace('{{current_number}}', currentQuestionNumber));
        questionsContainer.appendChild(newQuestion);
        currentQuestionNumber++;
    };

    addQuestionButton.addEventListener('mousedown', addQuestion);
}
