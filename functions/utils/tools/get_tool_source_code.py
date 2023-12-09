import inspect

def get_tool_source_code(varFunction):
  source_code = inspect.sourcecode(varFunction)
  return source_code
