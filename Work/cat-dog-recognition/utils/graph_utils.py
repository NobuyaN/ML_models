import matplotlib.pyplot as plt

def lossGraph(trainingLossHistory: list, testingLossHistory: list, epochs: int) -> object:
  _, ax = plt.subplots(nrows=1, ncols=2, figsize=(20, 5))
  ax[0].set_title("Training Loss")
  ax[0].plot(trainingLossHistory, label="training loss")
  ax[0].set_xticks(range(0, epochs+1))
  ax[0].set_xlabel("Epochs")
  ax[0].set_ylabel("Loss")
  ax[0].legend()

  ax[1].set_title("Testing Loss")
  ax[1].plot(testingLossHistory, label="testing loss")
  ax[1].set_xticks(range(1, epochs+1))
  ax[1].set_xlabel("Epochs")
  ax[1].set_ylabel("Loss")
  ax[1].legend()

  plt.show()
  

