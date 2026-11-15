import numpy as np

class HybridChaoticTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Separable quadratic component
        quadratic = np.sum(x**2)
        
        # Non-separable trigonometric coupling with varying frequencies
        trig_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                trig_coupling += np.sin(2 * x[i]) * np.cos(3 * x[j]) * np.sin(0.5 * (x[i] + x[j]))
        
        # Chaotic logarithmic perturbations with interdimensional coupling
        log_perturbation = 0
        for i in range(self.dim):
            log_perturbation += np.log(1 + np.abs(x[i])) * np.sin(5 * x[i]) * np.cos(2 * x[i]**2)
        
        # Mixed polynomial and exponential terms
        mixed_terms = 0
        for i in range(self.dim):
            mixed_terms += (x[i]**4 + 0.5 * np.exp(-x[i]**2)) * np.sin(0.3 * x[i]**3)
        
        # Saddle point structure with high-order polynomial interactions
        saddle = 0
        for i in range(self.dim):
            saddle += (x[i]**6 - 5 * x[i]**4 + 6 * x[i]**2) * np.cos(0.2 * x[i])
        
        # Interdimensional chaotic coupling with tanh and logarithmic damping
        chaotic_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                chaotic_coupling += np.tanh(x[i] * x[j]) * np.log(1 + np.abs(x[i] * x[j])) * np.sin(0.1 * (x[i]**2 + x[j]**2))
        
        # High-frequency chaotic oscillations
        high_freq = 0
        for i in range(self.dim):
            high_freq += np.sin(10 * x[i]) * np.cos(7 * x[i]) * np.tan(0.2 * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Cross-dimensional polynomial interactions
        cross_poly = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_poly += 0.1 * (x[i]**3 + x[j]**3) * np.cos(0.4 * (x[i] - x[j]))
        
        # Final combined function
        return quadratic + trig_coupling + log_perturbation + mixed_terms + saddle + chaotic_coupling + high_freq + cross_poly