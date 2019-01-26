import numpy as np
import pickle
import sys


if __name__ == '__main__':
  if len(sys.argv) != 3:
    print('Specify input and output path')
    exit(-1)
  src_path = sys.argv[1]
  output_path = sys.argv[2]
  with open(src_path, 'rb') as f:
    src_data = pickle.load(f)
  model = {
    'J_regressor': src_data['J_regressor'],
    'weights': np.array(src_data['weights']),
    'posedirs': np.array(src_data['posedirs']),
    'v_template': np.array(src_data['v_template']),
    'shapedirs': np.array(src_data['shapedirs']),
    'f': np.array(src_data['f']),
    'kintree_table': src_data['kintree_table']
  }
  with open(output_path, 'wb') as f:
    pickle.dump(model, f)
