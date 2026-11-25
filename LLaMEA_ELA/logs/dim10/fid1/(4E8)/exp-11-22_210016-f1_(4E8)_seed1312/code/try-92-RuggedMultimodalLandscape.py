import numpy as np

class RuggedMultimodalLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Global minimum at origin
        result = 0.0
        
        # Sinusoidal wave components with varying frequencies and amplitudes
        for i in range(self.dim):
            result += (1.0 + 0.5 * np.sin(2.0 * x[i]) + 0.3 * np.cos(3.0 * x[i])) * \
                     (0.8 + 0.2 * np.sin(5.0 * x[i]) + 0.1 * np.cos(7.0 * x[i]))
        
        # Polynomial barrier terms with increasing degree
        for i in range(self.dim):
            result += 0.1 * x[i]**6 + 0.05 * x[i]**8 + 0.02 * x[i]**10
        
        # Exponential decay components modulated by radial distance
        r = np.sqrt(np.sum(x**2))
        result += np.exp(-r / 3.0) * (1.0 + 0.3 * np.sin(r * 2.0) + 0.2 * np.cos(r * 4.0))
        
        # Cross-dimensional coupling with interaction terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.05 * np.sin(x[i] * x[j]) * np.cos(x[i] + x[j]) * \
                         (1.0 + 0.1 * (x[i]**2 + x[j]**2))
        
        # Additional ruggedness through high-frequency chaotic components
        chaotic_component = 0.0
        for i in range(self.dim):
            chaotic_component += np.sin(10.0 * x[i]) * np.cos(8.0 * x[i]) * \
                               np.exp(-x[i]**2 / 2.0) + \
                               0.05 * np.tanh(x[i])**3
        
        result += 0.3 * chaotic_component
        
        # Normalize by dimensionality to maintain scalability
        result /= self.dim
        
        return result