import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term with conditioning
        result = np.sum(x_norm**2)
        
        # Chaotic interaction terms using sine and cosine with dynamic frequencies
        for i in range(self.dim):
            freq = 5.0 + 3.0 * np.sin(x_norm[i])
            result += 0.8 * np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[(i+1) % self.dim])
            
        # Fractional polynomial penalties for increased complexity
        result += 0.1 * np.sum(np.abs(x_norm)**1.7) + 0.05 * np.sum(np.abs(x_norm)**2.3)
        
        # Dynamic coupling with chaotic modulation
        for i in range(self.dim):
            mod = 1.0 + 0.5 * np.sin(2.0 * x_norm[i])
            result += 0.4 * np.sin(mod * x_norm[i]) * np.cos(mod * x_norm[(i+2) % self.dim]) * np.sin(x_norm[(i+3) % self.dim])
        
        # Add a complex multi-modal structure with exponential interactions
        exp_term = 0.0
        for i in range(self.dim):
            exp_term += np.exp(-x_norm[i]**2) * np.cos(10 * x_norm[i])
        result += 0.6 * exp_term
        
        # Cross-dimensional coupling with varying strengths
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += 0.2 * np.sin(x_norm[i]) * np.cos(x_norm[j]) * (i + j)
        result += cross_term
        
        # Add a global minimum shift with penalty for convergence
        shift = np.array([np.sin(i * 0.5) for i in range(self.dim)])
        result += 0.1 * np.sum((x_norm - shift)**3)
        
        return result