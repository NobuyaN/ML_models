import matplotlib.pyplot as plt

def lossGraph(trainingLossHistory: list, testingLossHistory: list, 
              trainingAccuracyHistory: list, testingAccuracyHistory: list, epochs: int) -> object:
  _, ax = plt.subplots(nrows=2, ncols=2, figsize=(20, 10))
  ax[0,0].set_title("Training Loss")
  ax[0,0].plot(trainingLossHistory, label="training loss")
  ax[0,0].set_xticks(range(0, epochs), range(1, epochs+1))
  ax[0,0].set_xlabel("Epochs")
  ax[0,0].set_ylabel("Loss")
  ax[0,0].legend()

  ax[0,1].set_title("Testing Loss")
  ax[0,1].plot(testingLossHistory, label="testing loss")
  ax[0,1].set_xticks(range(0, epochs), range(1, epochs+1))
  ax[0,1].set_xlabel("Epochs")
  ax[0,1].set_ylabel("Loss")
  ax[0,1].legend()

  ax[1,0].set_title("Training Accuracy")
  ax[1,0].plot(trainingAccuracyHistory, label="training accuracy")
  ax[1,0].set_xticks(range(0, epochs), range(1, epochs+1))
  ax[1,0].set_xlabel("Epochs")
  ax[1,0].set_ylabel("Accuracy")
  ax[1,0].legend()

  ax[1,1].set_title("Testing Accuracy")
  ax[1,1].plot(testingAccuracyHistory, label="testing accuracy")
  ax[1,1].set_xticks(range(0, epochs), range(1, epochs+1))
  ax[1,1].set_xlabel("Epochs")
  ax[1,1].set_ylabel("Accuracy")
  ax[1,1].legend()

  plt.show()
  

