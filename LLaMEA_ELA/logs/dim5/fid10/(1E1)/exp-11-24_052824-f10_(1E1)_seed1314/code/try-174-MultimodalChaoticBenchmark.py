import numpy as np

class MultimodalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial base with mixed degrees
        poly_base = np.sum(x**4) + 0.5 * np.sum(x**6) + 0.1 * np.sum(x**8)
        
        # Trigonometric interactions with varying frequencies
        trig_interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                trig_interaction += np.sin(2 * x[i]) * np.cos(3 * x[j]) * np.exp(-0.1 * (x[i] - x[j])**2)
                
        # Exponential decay with sinusoidal modulation
        exp_modulated = 0
        for i in range(self.dim):
            exp_modulated += np.exp(-0.5 * x[i]**2) * np.sin(4 * x[i]) * np.cos(2 * x[i])
            
        # Coupled chaotic sine waves
        chaotic_sine = 0
        for i in range(self.dim):
            chaotic_sine += np.sin(x[i] + 0.3 * np.sin(5 * x[i])) * np.cos(0.7 * x[i])
            
        # High-dimensional correlation with polynomial coupling
        correlation_term = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                correlation_term += (x[i]**2 + x[j]**2) * np.sin(0.5 * x[i] * x[j])
                
        # Sharp local minima using high-frequency sinusoids
        sharp_minima = 0
        for i in range(self.dim):
            sharp_minima += np.sin(10 * x[i]) * np.cos(8 * x[i]) + 0.5 * np.sin(15 * x[i])
            
        # Asymmetric saddle points
        asymmetric_saddle = 0
        for i in range(self.dim):
            asymmetric_saddle += (x[i]**2 - 1) * (x[i]**4 - 1) * np.exp(-0.3 * x[i]**2)
            
        # Combined weighted landscape
        return (0.4 * poly_base + 
                0.3 * trig_interaction + 
                0.15 * exp_modulated + 
                0.1 * chaotic_sine + 
                0.2 * correlation_term + 
                0.1 * sharp_minima + 
                0.25 * asymmetric_saddle + 
                3 * np.sum(np.sin(x)**3))