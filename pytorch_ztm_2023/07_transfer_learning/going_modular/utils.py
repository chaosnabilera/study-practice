"""
Contains various utility functions for PyTorch model training and saving.
"""

import matplotlib.pyplot
import mlxtend
import mlxtend.plotting
import torch
import torchmetrics

from pathlib import Path

__all__=['save_model', 'plot_loss_curves', 'display_confusion_matrix']

def save_model(
        model: torch.nn.Module,
        target_dir: str,
        model_name: str
    ):
    """Saves a PyTorch model to a target directory.

    Args:
        model: A target PyTorch model to save.
        target_dir: A directory for saving the model to.
        model_name: A filename for the saved model. Should include
            either ".pth" or ".pt" as the file extension.

    Example usage:
        save_model(model=model_0,
        target_dir="models",
        model_name="05_going_modular_tingvgg_model.pth")
    """
    # Create target directory
    target_dir_path = Path(target_dir)
    target_dir_path.mkdir(parents=True, exist_ok=True)

    # Create model save path
    assert model_name.endswith(".pth") or model_name.endswith(".pt"), "model_name should end with '.pt' or '.pth'"
    model_save_path = target_dir_path / model_name

    # Save the model state_dict()
    print(f"[INFO] Saving model to: {model_save_path}")
    torch.save(obj=model.state_dict(),
                         f=model_save_path)

def plot_loss_curves(results: dict[str, list[float]]):
    """Plots training curves of a results dictionary.

    Args:
        results (dict): dictionary containing list of values, e.g.
            {"train_loss": [...],
             "train_acc": [...],
             "test_loss": [...],
             "test_acc": [...]}
    """
        
    # Get the loss values of the results dictionary (training and test)
    loss = results['train_loss']
    test_loss = results['test_loss']

    # Get the accuracy values of the results dictionary (training and test)
    accuracy = results['train_acc']
    test_accuracy = results['test_acc']

    # Figure out how many epochs there were
    epochs = range(len(results['train_loss']))

    # Setup a plot 
    matplotlib.pyplot.figure(figsize=(15, 7))

    # Plot loss
    matplotlib.pyplot.subplot(1, 2, 1)
    matplotlib.pyplot.plot(epochs, loss, label='train_loss')
    matplotlib.pyplot.plot(epochs, test_loss, label='test_loss')
    matplotlib.pyplot.title('Loss')
    matplotlib.pyplot.xlabel('Epochs')
    matplotlib.pyplot.legend()

    # Plot accuracy
    matplotlib.pyplot.subplot(1, 2, 2)
    matplotlib.pyplot.plot(epochs, accuracy, label='train_accuracy')
    matplotlib.pyplot.plot(epochs, test_accuracy, label='test_accuracy')
    matplotlib.pyplot.title('Accuracy')
    matplotlib.pyplot.xlabel('Epochs')
    matplotlib.pyplot.legend()

def display_confusion_matrix(
        data_loader: torch.utils.data.DataLoader,
        model: torch.nn.Module,
        class_names: list[str],
        device: torch.device
    ):
    model.to(device)
    y_pred_list    = []
    y_label_list = []
    with torch.inference_mode():
        for X,y in data_loader:
            X,y = X.to(device), y.to(device)
            y_logit = model(X)
            y_pred = torch.softmax(y_logit, dim=1).argmax(dim=1)
            y_pred_list.append(y_pred.cpu())
            y_label_list.append(y.cpu())
        
        y_pred_tensor = torch.cat(y_pred_list)
        y_label_tensor = torch.cat(y_label_list)

        confusion_matrix = torchmetrics.ConfusionMatrix(num_classes = len(class_names), task='multiclass')
        confusion_matrix_tensor = confusion_matrix(preds=y_pred_tensor, target=y_label_tensor)

        fig, ax = mlxtend.plotting.plot_confusion_matrix(
                conf_mat=confusion_matrix_tensor.numpy(),
                class_names = class_names,
                figsize=(10,7)
        )
        matplotlib.pyplot.show()