from prefect import flow, task
from prefect.blocks.system import String

string_block = String.load("apexy")

@task
def create_message():
    msg = string_block.value
    return msg

#subflow
@flow
def something_else():
    result = 10
    return result

#main flow
@flow
def hello_world():
    tsk_msg=create_message()
    print(f"hello from prefect flow and {tsk_msg} and their value is {str(something_else())} ")

if __name__ == "__main__":
    hello_world()
