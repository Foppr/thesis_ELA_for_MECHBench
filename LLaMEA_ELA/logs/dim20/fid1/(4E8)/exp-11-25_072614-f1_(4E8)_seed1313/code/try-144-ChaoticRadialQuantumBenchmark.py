import numpy as np

class ChaoticRadialQuantumBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic radial basis with quantum interference
        r = np.sqrt(np.sum(x**2))
        chaotic_radial = np.sum(np.exp(-0.5 * (x**2) / (1.0 + 0.1 * np.sin(5.0 * r))) * 
                               np.cos(3.0 * r + 0.5 * np.sin(7.0 * r)) * 
                               np.sin(2.0 * r + 0.3 * np.cos(4.0 * r))) / self.dim
        
        # Asymmetric gradient field with fractal scaling
        asym_grad = np.sum(np.abs(x)**1.5 * np.sin(x) * np.exp(-0.1 * np.abs(x)) * 
                          (1.0 + 0.2 * np.sin(3.0 * np.sum(x**2)))) / self.dim
        
        # Dynamic noise with quantum amplitude modulation
        noise = np.sum(np.sin(x * (1.0 + 0.3 * np.sin(0.5 * r))) * 
                      np.cos(x * (1.0 + 0.4 * np.cos(0.7 * r))) * 
                      np.exp(-0.05 * r**2)) / self.dim
        
        # Cross-term interactions with quantum entanglement
        cross_terms = 0
        for i in range(self.dim - 1):
            cross_terms += (np.sin(x[i] * x[i+1]) * np.cos(x[i] + x[i+1]) * 
                           np.exp(-0.1 * np.abs(x[i] - x[i+1])) * 
                           (1.0 + 0.1 * np.sin(2.0 * (x[i]**2 + x[i+1]**2))))
        cross_term = cross_terms / (self.dim - 1)
        
        # Fractal-like self-similarity with quantum scaling
        fractal_self = np.sum(np.cos(2.0 * np.pi * r * (1.0 + 0.1 * np.sin(3.0 * r))) * 
                             np.exp(-0.05 * r**2) * 
                             np.sin(4.0 * r)) / self.dim
        
        # Adaptive conditioning with quantum-inspired scaling
        cond_factor = 1.0 + 0.8 * np.mean(np.abs(x))**2.2
        adaptive_cond = np.sum((x**2) * cond_factor * np.cos(3.0 * x)) / self.dim
        
        # Quantum interference terms
        quantum_interf = np.sum(np.sin(x * np.pi) * np.cos(x * np.pi) * 
                               np.exp(-0.1 * np.abs(x))) / self.dim
        
        # Combined weighted sum of all components
        total = 0.25 * chaotic_radial + 0.2 * asym_grad + 0.15 * noise + 0.15 * cross_term + \
                0.1 * fractal_self + 0.1 * adaptive_cond + 0.05 * quantum_interf
        
        return total