import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic phase-modulated fractal oscillatory terms
        fractal_term = 0.0
        for i in range(self.dim):
            freq1 = 3.0 + 0.5 * np.sin(i * 0.7) * np.cos(i * 0.3)
            freq2 = 2.0 + 0.4 * np.sin(i * 0.9) * np.cos(i * 0.5)
            phase1 = 0.8 * np.sin(x[i] * 1.2) + 0.3 * np.cos(x[i] * 0.9)
            phase2 = 0.6 * np.sin(x[i] * 1.5) + 0.4 * np.cos(x[i] * 0.7)
            fractal_term += (0.5 * np.sin(freq1 * x[i] + phase1) * 
                            np.cos(freq2 * x[i] + phase2) * 
                            np.exp(-0.2 * np.abs(x[i])) + 
                            0.3 * np.sin(4 * freq1 * x[i]) * 
                            np.cos(3 * freq2 * x[i]) +
                            0.15 * np.sin(7 * x[i]) * np.exp(-0.1 * x[i]**2) *
                            np.sin(0.5 * x[i]))
        
        # Hyperbolic ridge structure with exponential scaling
        ridge_term = 0.0
        for i in range(self.dim):
            ridge_height = 0.8 * (np.tanh(x[i] / (1.0 + i * 0.2)) + 
                                 np.sinh(0.5 * x[i]) / (1.0 + np.exp(-x[i]))) * \
                           (1 - np.exp(-0.4 * x[i]**2))
            ridge_term += ridge_height * np.exp(-0.2 * x[i]**2)
        
        # Long-range cross-dimensional coupling with power-law decay
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+7, self.dim)):  # Extended interaction range
                dist = np.sqrt((x[i] - x[j])**2 + 0.001)
                scale_factor = 1.0 / (dist**2.5 + 1.0) * np.exp(-0.15 * dist)
                cross_term += scale_factor * np.sin(3.0 * x[i]) * np.cos(4.0 * x[j]) * \
                              np.tanh(0.3 * (x[i] + x[j]))
        
        # Global modulation with hyperbolic and chaotic components
        global_mod = 0.0
        for i in range(self.dim):
            global_mod += 0.4 * (x[i]**5) * np.exp(-0.12 * np.abs(x[i])) * \
                         np.sin(0.7 * x[i]) * np.cos(0.3 * x[i]) + \
                         0.2 * x[i] * np.sin(1.1 * x[i]) * np.exp(-0.05 * x[i]**2) + \
                         0.1 * np.sin(10 * x[i]) * np.cos(8 * x[i])
        
        # Add chaotic noise component for increased difficulty
        noise = 0.05 * np.sum(np.sin(x * 10.0) * np.cos(x * 7.0))
        
        return fractal_term + ridge_term + cross_term + global_mod + noise + 0.02 * np.sum(x**2)