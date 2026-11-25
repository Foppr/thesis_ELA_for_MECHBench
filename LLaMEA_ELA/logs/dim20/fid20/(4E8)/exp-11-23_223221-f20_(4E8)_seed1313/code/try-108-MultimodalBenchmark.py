import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced hyperbolic tangent basin terms with increased nonlinearity
        basin_term = 0.0
        for i in range(self.dim):
            steepness = 1.5 + 0.8 * np.sin(i * 0.9)
            basin_term += (np.tanh(steepness * x[i])**3) * np.exp(-0.3 * x[i]**2)
        
        # Modified polynomial gradient flow with higher-order terms
        grad_term = 0.0
        for i in range(self.dim):
            # Increased complexity with quintic and exponential scaling
            grad_term += (0.3 * x[i]**2 + 0.2 * x[i]**5 + 0.15 * np.exp(0.6 * x[i])) * np.cos(0.4 * x[i])
        
        # Enhanced logarithmic energy interactions with additional coupling
        energy_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 0.02)
                energy_term += (np.log(dist + 1.5) / (dist + 0.5)) * np.sin(2.5 * x[i]) * np.cos(2.0 * x[j])
        
        # Chaotic saddle-point modulation with increased frequency
        chaotic_term = 0.0
        for i in range(self.dim):
            chaotic_term += (np.sin(x[i]) * np.cos(x[i]) * 
                           np.exp(-0.15 * np.abs(x[i])) * 
                           np.sin(4.0 * x[i] + np.sin(2.5 * x[i])))
        
        # Modified global scaling with additional sinusoidal components
        global_term = 0.0
        for i in range(self.dim):
            global_term += (0.5 * x[i]**3 * np.exp(-0.15 * x[i]**2) + 
                          0.3 * x[i] * np.sin(0.6 * x[i]) + 
                          0.15 * np.log(np.abs(x[i]) + 2.5))
        
        # Return the combined function value with increased regularization
        return basin_term + grad_term + energy_term + chaotic_term + global_term + 0.01 * np.sum(x**2)