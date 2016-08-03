console.log(phrase);


var words = phrase.trim().split(' ');

for (i=0; i<words.length; i++) {
    $('#phrase-container').append('<span class="word' + i + '">'+ words[i] +' </span>');
}


var wordIndex = 0;

console.log(words);


// currSpan = ('word'+wordIndex);
// currSpan.setAttribut


$('#typing-box').on('keyup', function(event) {

    // Check if spacebar was pressed
    if (event.keyCode == 32) {
        // Check if input matches current word
        if ($(this).val().trim() === words[wordIndex]) {
            $(this).val = '';
            wordIndex++;
        }
    }
});


