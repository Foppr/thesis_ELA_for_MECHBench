import numpy as np

class MultimodalSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Input dimension mismatch")
        
        # Base quadratic term with strong conditioning
        f = np.sum(x**2) * 0.8
        
        # Add chaotic sinusoidal grid pattern with high-frequency interactions
        for i in range(self.dim):
            f += 0.3 * np.sin(11 * x[i]) * np.cos(9 * x[i]) * np.sin(5 * x[i])
            
        # Add nested multi-scale interactions with exponential coupling
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Extended range for complexity
                f += 0.15 * np.sin(4 * x[i] + 3 * x[j]) * np.cos(7 * x[i] - 2 * x[j]) * np.sin(2 * x[i] + x[j])
                
        # Add fractal-like self-similar structure with recursive pattern
        for i in range(self.dim):
            f += 0.08 * np.sin(15 * np.sin(4 * x[i])) * np.cos(10 * np.cos(3 * x[i])) * np.sin(6 * np.sin(2 * x[i]))
            
        # Add higher-order polynomial interactions with non-linear coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, min(j+4, self.dim)):
                    f += 0.03 * x[i]**3 * np.sin(x[j] + x[k]) * np.cos(x[i] * x[j])
                    
        # Add multiple global minima at non-origin locations with varying scales
        global_minima = np.array([[-3.0, 3.0], [3.0, -3.0], [-3.0, -3.0], [3.0, 3.0], 
                                 [-1.5, 1.5], [1.5, -1.5], [-1.5, -1.5], [1.5, 1.5]])
        if self.dim >= 2:
            minima_term = 0
            for min_point in global_minima:
                if self.dim >= len(min_point):
                    diff = x[:len(min_point)] - min_point
                    minima_term += np.exp(-0.3 * np.sum(diff**2))
            f += 0.4 * minima_term
            
        # Add noise component with non-uniform distribution for additional challenge
        f += 0.02 * np.sum(np.sin(15 * x)**2 + np.cos(8 * x)**2)
        
        # Add dimensional coupling with cross-terms that increase complexity exponentially
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f += 0.05 * np.sin(2 * x[i] * x[j]) * np.cos(3 * x[i] + x[j]) * np.sin(x[i] - x[j])
                
        # Add chaotic phase modulation for increased non-linearity
        phase_mod = 0
        for i in range(self.dim):
            phase_mod += np.sin(2 * np.pi * x[i] * (i + 1) * 0.1)
        f += 0.1 * np.sin(phase_mod)
        
        # Add enhanced higher-order interactions for increased complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    for l in range(k+1, min(k+3, self.dim)):
                        f += 0.02 * x[i]**2 * x[j]**2 * np.sin(x[k] + x[l]) * np.cos(x[i] * x[j] * x[k])
        
        # Add multi-scale fractal-like pattern with self-similarity at different levels
        for i in range(self.dim):
            f += 0.04 * np.sin(20 * np.sin(5 * np.sin(2 * x[i]))) * np.cos(15 * np.cos(4 * np.cos(3 * x[i]))) * np.sin(10 * np.sin(3 * np.sin(2 * x[i])))
        
        # Add enhanced dimensional coupling with non-linear interaction terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f += 0.08 * np.sin(3 * x[i] * x[j] + x[i]**2) * np.cos(2 * x[i] + x[j]**2) * np.sin(x[i] * x[j] - x[i]**3)
                
        # Add chaotic oscillation with dynamic frequency modulation
        freq_mod = 0
        for i in range(self.dim):
            freq_mod += np.sin(2 * np.pi * x[i] * (i + 1) * 0.2) * np.cos(2 * np.pi * x[i] * (i + 1) * 0.3)
        f += 0.12 * np.sin(freq_mod)
        
        return f