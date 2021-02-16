// copied from Teachable Machine GitHub repo and modified by Nelson Gou

const URL = "https://teachablemachine.withgoogle.com/models/2crv9wEh4/";

async function createModel() {
  const checkpointURL = URL + "model.json"; // model topology
  const metadataURL = URL + "metadata.json"; // model metadata

  const recognizer = speechCommands.create("BROWSER_FFT", undefined, checkpointURL, metadataURL);

  await recognizer.ensureModelLoaded();

  return recognizer;
}

document.getElementById("start").onclick = function() {
  init()
};

async function init() {
  const recognizer = await createModel();
  const classLabels = recognizer.wordLabels();
  const labelContainer = document.getElementById("label-container");

  for (let i = 0; i < classLabels.length; i++) {
    // create divs for classes
    labelContainer.appendChild(document.createElement("div"));
  }

  // hide start button and show stop button
  document.getElementById("start").setAttribute("style", "display:none");
  document.getElementById("stop").setAttribute("style", "visibility:visible");

  recognizer.listen(result => {
    var maxProb = -1;
    var maxClass = "";

    const scores = result.scores;

    for (let i = 0; i < classLabels.length; i++) {
      // get predictions for classes
      const classPrediction = classLabels[i] + ": " + parseInt(result.scores[i].toFixed(2) * 100) + "%";
      labelContainer.childNodes[i].innerHTML = classPrediction;

      if (parseInt(result.scores[i].toFixed(2) * 100) > maxProb) {
        // find the maximum prediction score
        maxProb = parseInt(result.scores[i].toFixed(2) * 100);
        maxClass = classLabels[i];
      }
    }

    // print out the class with the max prediction score
    document.getElementById("result").setAttribute("style", "visibility:visible");
    document.getElementById("result").innerHTML = "Result: " + maxClass;

  }, {
    includeSpectrogram: true,
    probabilityThreshold: 0.75,
    invokeCallbackOnNoiseAndUnknown: true,
    overlapFactor: 0.50
  });

  document.getElementById("stop").onclick = function() {
    recognizer.stopListening()
    document.getElementById("stop").setAttribute("style", "display:none");
    document.getElementById("start").setAttribute("style", "visibility:visible");
    document.getElementById("label-container").innerHTML = "";
    document.getElementById("result").innerHTML = "";
  };
}