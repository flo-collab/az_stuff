import azureml.core
from azureml.core import Workspace

# ws = Workspace.from_config()
# # print('lala')


from azureml.core import Workspace
ws = Workspace.get(name="Preparation-Flo-AI102-Clermont",
                   subscription_id= "0252a218-2d27-4d77-a4f1-b638272c95e0",
                   resource_group="cloud-shell-storage-westeurope")