import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Hyperbolic tangent basin terms with varying steepness
        basin_term = 0.0
        for i in range(self.dim):
            steepness = 1.0 + 0.5 * np.sin(i * 0.7)
            basin_term += (np.tanh(steepness * x[i])**2) * np.exp(-0.2 * x[i]**2)
        
        # Polynomial gradient flow components with mixed exponents
        grad_term = 0.0
        for i in range(self.dim):
            # Mix of quadratic, quartic, and exponential scaling
            grad_term += (0.5 * x[i]**2 + 0.3 * x[i]**4 + 0.1 * np.exp(0.5 * x[i])) * np.cos(0.3 * x[i])
        
        # Logarithmic energy interactions between dimensions
        energy_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 0.01)
                energy_term += (np.log(dist + 1.0) / (dist + 1.0)) * np.sin(2.0 * x[i]) * np.cos(1.5 * x[j])
        
        # Chaotic saddle-point modulation with sinusoidal perturbations
        chaotic_term = 0.0
        for i in range(self.dim):
            chaotic_term += (np.sin(x[i]) * np.cos(x[i]) * 
                           np.exp(-0.1 * np.abs(x[i])) * 
                           np.sin(3.0 * x[i] + np.sin(2.0 * x[i])))
        
        # Combined global scaling with polynomial and exponential components
        global_term = 0.0
        for i in range(self.dim):
            global_term += (0.4 * x[i]**3 * np.exp(-0.1 * x[i]**2) + 
                          0.2 * x[i] * np.sin(0.5 * x[i]) + 
                          0.1 * np.log(np.abs(x[i]) + 2.0))
        
        # Return the combined function value with small regularization
        return basin_term + grad_term + energy_term + chaotic_term + global_term + 0.005 * np.sum(x**2)