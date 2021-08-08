# Machine-Learning-Projects

var copy = function(target) {
    var textArea = document.createElement('textarea')
    textArea.setAttribute('style','width:1px;border:0;opacity:0;')
    document.body.appendChild(textArea)
    textArea.value = target.innerHTML
    textArea.select()
    document.execCommand('copy')
    document.body.removeChild(textArea)
}

var pres = document.querySelectorAll(".comment-body > pre")
pres.forEach(function(pre){
  var button = document.createElement("button")
  button.className = "btn btn-sm"
  button.innerHTML = "copy"
  pre.parentNode.insertBefore(button, pre)
  button.addEventListener('click', function(e){
    e.preventDefault()
    copy(pre.childNodes[0])
  })
})
Installation

1.Clone this repository

https://github.com/DipeshDhandha07/Machine-Learning-Projects.git

2.Python

pip install opencv-python\
pip install pandas\
pip install numpy

3.Anaconda

conda install -c anaconda opencv\
conda install -c anaconda numpy\
conda install -c anaconda pandas
