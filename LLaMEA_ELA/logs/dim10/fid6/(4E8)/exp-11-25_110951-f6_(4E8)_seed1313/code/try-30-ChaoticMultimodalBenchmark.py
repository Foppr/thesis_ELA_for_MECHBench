import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        x = np.array(x)
        
        # Base quadratic term with adaptive scaling
        quadratic = 0.05 * np.sum(x**2)
        
        # Trigonometric multimodal components with varying frequencies
        trig_term = 0
        for i in range(self.dim):
            trig_term += np.sin(2.0 * x[i]) * np.cos(1.5 * x[i])
            trig_term += 0.5 * np.sin(5.0 * x[i]) * np.cos(3.0 * x[i])
        
        # Saddle point structure with interaction terms
        saddle = 0
        for i in range(self.dim):
            if i < self.dim - 1:
                saddle += 0.3 * x[i] * x[i+1] * np.sin(x[i] + x[i+1])
        
        # Exponential decay components to create varying curvature
        exp_term = 0
        for i in range(self.dim):
            exp_term += np.exp(-0.1 * np.abs(x[i])) * np.cos(0.5 * x[i])
        
        # Random perturbation to increase chaos
        random_pert = 0
        for i in range(self.dim):
            random_pert += 0.2 * np.sin(7.0 * x[i]) * np.random.uniform(-1, 1)
        
        # Combine all terms with different weights
        return quadratic + trig_term + saddle + exp_term + random_pert + 0.01 * np.sum(x**4)