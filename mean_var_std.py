import numpy as np

def calculate(list):
  if len(list) >= 9:
    #convert the list to an array
     np.array(list)
     list.shape = (3,3)
    
     #calculating the mean 
     mean_col = np.mean(list,axis=0)
     mean_row = np.mean(list,axis=1)
     mean_flat = np.mean(list)

    #calculating the variance
     var_col = np.var(list,axis=0)
     var_row = np.var(list,axis=1)
     var_flat = np.var(list)

     #calculating the standard deviation
     std_col = np.std(list,axis=0)
     std_row = np.std(list,axis=1)
     std_flat = np.std(list)

    #calculating the max
     max_col = np.max(list,axis=0)
     max_row = np.max(list,axis=1)
     max_flat = np.max(list)

    #calculating the min 
     min_col = np.min(list,axis=0)
     min_row = np.min(list,axis=1)
     min_flat = np.min(list)

    #calculating the sum
     sum_col = np.sum(list,axis=0)
     sum_row = np.sum(list,axis=1)
     sum_flat = np.sum(list)

     cal_dict = {'mean':[],'variance':[],'standard deviation':[],'max':[],'min':[],'sum':[]}

     cal_dict['mean'].append(mean_col)
     cal_dict['mean'].append(mean_row)
     cal_dict['mean'].append(mean_flat)

     cal_dict['variance'].append(var_col)
     cal_dict['variance'].append(var_row)
     cal_dict['variance'].append(var_flat)

     cal_dict['standard'].append(std_col)
     cal_dict['standard'].append(std_row)
     cal_dict['standard'].append(std_flat)

     cal_dict['max'].append(max_col)
     cal_dict['max'].append(max_row)
     cal_dict['max'].append(max_flat)

     cal_dict['min'].append(min_col)
     cal_dict['min'].append(min_row)
     cal_dict['min'].append(min_flat)

     cal_dict['sum'].append(sum_col)
     cal_dict['sum'].append(sum_row)
     cal_dict['sum'].append(sum_flat)
  
    
  else: 
     raise ValueError("List must contain 9 numbers")



     print(cal_dict)