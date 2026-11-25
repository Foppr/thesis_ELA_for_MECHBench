import numpy as np

class HybridMultimodalFunction:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Polynomial base with adaptive scaling
        result = np.sum(x**6) / 6.0
        
        # Exponential coupling terms with varying intensities
        for i in range(self.dim):
            result += np.exp(-0.5 * x[i]**2) * np.sin(2.0 * x[i])**2 * (1.0 / (i + 1)**1.5)
            
        # Logarithmic interaction terms with boundary effects
        for i in range(self.dim):
            log_term = np.log(1.0 + abs(x[i]))
            result += 0.3 * log_term * np.cos(3.0 * x[i]) * (1.0 / (i + 1)**0.5)
            
        # Cross-dimensional exponential coupling with adaptive strengths
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 1.0 / (1.0 + np.abs(x[i] - x[j]))
                result += coupling * np.exp(-0.1 * (x[i]**2 + x[j]**2)) * np.sin(x[i] * x[j])
                
        # Periodic boundary effect terms
        for i in range(self.dim):
            result += 0.2 * np.sin(4.0 * x[i]) * np.cos(4.0 * x[i]) * (1.0 / (i + 1)**2)
            
        # Adaptive ridge terms with varying frequencies
        for i in range(self.dim):
            result += 0.5 * np.exp(-0.5 * x[i]**2) * np.sin(8.0 * x[i])**2
            
        # Multi-scale oscillation components
        for i in range(self.dim):
            result += 0.1 * np.sin(16.0 * x[i]) * np.cos(16.0 * x[i]) * (1.0 / (i + 1)**1.2)
            
        # Central repulsion term to prevent convergence at origin
        dist = np.sqrt(np.sum(x**2))
        if dist > 0:
            result += 0.4 * np.exp(-dist) / (dist + 1.0)
            
        return result