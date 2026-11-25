import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Polynomial term with high degree to create many local minima
        poly_term = np.sum(x_scaled**8)
        
        # Trigonometric term with multiple frequencies
        trig_term = 0.0
        for i in range(self.dim):
            trig_term += np.sin(20 * x_scaled[i]) + np.cos(15 * x_scaled[i])
            
        # Exponential barrier terms to create complex landscape
        exp_term = 0.0
        for i in range(self.dim):
            exp_term += np.exp(-5 * (x_scaled[i] - 0.2)**2) + np.exp(-3 * (x_scaled[i] + 0.3)**2)
            
        # Interaction terms between dimensions
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction_term += np.sin(5 * x_scaled[i]) * np.cos(3 * x_scaled[j])
                
        # Combine all terms with different weights
        result = 0.5 * poly_term + 0.3 * trig_term + 0.2 * exp_term + 0.1 * interaction_term
        
        return result