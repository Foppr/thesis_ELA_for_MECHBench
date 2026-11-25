import numpy as np

class ChaoticRadialQuantumBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic radial basis with quantum interference terms
        r = np.sqrt(np.sum(x**2))
        chaotic_radial = np.sum(np.exp(-0.5 * (x**2) / (1.0 + 0.3 * np.sin(5.0 * r))) * 
                               np.cos(3.0 * r + 0.5 * np.sin(7.0 * r)) * 
                               np.sin(2.0 * r + 0.2 * np.cos(4.0 * r))) / self.dim
        
        # Asymmetric gradient field with fractal scaling
        asym_grad = np.sum(np.abs(x)**1.5 * np.sin(x) * np.exp(-0.1 * np.abs(x)) * 
                          (1.0 + 0.2 * np.sin(3.0 * np.sum(x**2)))) / self.dim
        
        # Dynamic noise with quantum amplitude modulation
        noise = np.sum(np.sin(x * (1.0 + 0.4 * np.sin(0.3 * r))) * 
                      np.cos(x * (1.0 + 0.3 * np.cos(0.5 * r))) * 
                      np.exp(-0.05 * r**2)) / self.dim
        
        # Cross-term interaction with quantum coupling
        cross = np.sum(np.sin(x[:-1] * x[1:] * (1.0 + 0.1 * np.sin(2.0 * np.sum(x)))) * 
                      np.cos(x[:-1] + x[1:] + 0.3 * np.cos(3.0 * r))) / (self.dim - 1)
        
        # Fractal-like self-similarity with multi-scale interference
        fractal_multi = np.sum(np.sin(5.0 * x) * np.cos(3.0 * x) * 
                              np.exp(-0.03 * np.sum(x**2)) * 
                              (1.0 + 0.1 * np.sin(2.0 * r))) / self.dim
        
        # Adaptive conditioning with quantum-inspired scaling
        adaptive_cond = np.sum((x**2) * (1.0 + 0.5 * np.sin(0.5 * np.sum(x**2))) * 
                              np.cos(2.0 * x) * np.exp(-0.1 * np.abs(x))) / self.dim
        
        # Saddle-point with quantum harmonic components
        saddle = np.sum(x**3 * np.cos(x) - x**4 * np.sin(x) + 
                       0.5 * x**2 * np.tan(x/3.0) * np.exp(-0.01 * r**2)) / (self.dim * 10.0)
        
        # Quantum interference term with phase modulation
        quantum_interference = np.sum(np.sin(x * np.cos(x)) * np.cos(x * np.sin(x)) * 
                                    np.exp(-0.02 * r**2) * 
                                    (1.0 + 0.1 * np.sin(4.0 * r))) / self.dim
        
        # Combined weighted sum of all components
        total = 0.18 * chaotic_radial + 0.15 * asym_grad + 0.12 * noise + 0.1 * cross + \
                0.13 * fractal_multi + 0.12 * adaptive_cond + 0.1 * saddle + 0.08 * quantum_interference
        
        return total