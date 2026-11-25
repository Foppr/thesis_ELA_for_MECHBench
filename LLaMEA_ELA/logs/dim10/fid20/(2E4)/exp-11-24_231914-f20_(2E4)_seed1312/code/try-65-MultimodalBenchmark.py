import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters for scalability
        self.chaotic_params = [0.5, 1.2, 2.1, 3.4, 4.7][:min(dim, 5)]
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        base = np.sum(x**2) / self.dim
        
        # Chaotic saddle-point component with hyperbolic interactions
        chaotic = 0.0
        for i in range(self.dim):
            param = self.chaotic_params[i % len(self.chaotic_params)]
            chaotic += (np.sin(param * x[i]) * np.cos(param * x[i]**2) + 
                       np.sin(2 * param * x[i]) * np.cos(3 * param * x[i])) * np.exp(-0.1 * np.abs(x[i]))
        
        # Enhanced multimodal structure with strong hyperbolic interactions
        multimodal = 0.0
        for i in range(self.dim):
            multimodal += (np.sin(5 * x[i]) * np.cos(3 * x[i]) + 
                          0.5 * np.sin(7 * x[i]) * np.cos(4 * x[i]) + 
                          0.3 * np.sin(9 * x[i]) * np.cos(6 * x[i])) * np.exp(-0.2 * x[i]**2)
        
        # Modified correlation decay with exponential weighting
        corr_decay = 0.0
        for i in range(self.dim - 1):
            corr_decay += (np.sin(x[i]) * np.cos(x[i+1]) + 
                          np.cos(2 * x[i]) * np.sin(2 * x[i+1])) * np.exp(-0.3 * (x[i] - x[i+1])**2)
        
        # Refined global minimum shifting with asymmetric scaling
        shift = 0.0
        for i in range(self.dim):
            shift += 0.8 * np.sin(3 * x[i]) * np.cos(2 * x[i]) * np.exp(-0.15 * np.abs(x[i]))
        
        # Stronger hyperbolic interactions through higher-order terms
        hyperbolic = 0.0
        for i in range(self.dim):
            hyperbolic += (x[i]**3 + x[i]**5) * np.exp(-0.2 * x[i]**2)
        
        # Add new component: fractional chaos with adaptive weights
        fractional = 0.0
        for i in range(self.dim):
            fractional += (np.sin(4.5 * x[i]) * np.cos(2.3 * x[i]) + 
                          0.7 * np.sin(6.1 * x[i]) * np.cos(3.7 * x[i])) * np.exp(-0.25 * x[i]**2)
        
        # Add new component: coupled oscillators with phase modulation
        oscillator = 0.0
        for i in range(self.dim - 1):
            oscillator += (np.sin(x[i] + x[i+1]) * np.cos(x[i] - x[i+1]) + 
                          np.cos(2 * x[i] + x[i+1]) * np.sin(2 * x[i] - x[i+1])) * np.exp(-0.1 * (x[i]**2 + x[i+1]**2))
        
        # Combine all components with different weights to create complex landscape
        return base + 2.0 * chaotic + 1.5 * multimodal + 1.0 * corr_decay + 0.7 * shift + 0.5 * hyperbolic + 0.8 * fractional + 0.6 * oscillator