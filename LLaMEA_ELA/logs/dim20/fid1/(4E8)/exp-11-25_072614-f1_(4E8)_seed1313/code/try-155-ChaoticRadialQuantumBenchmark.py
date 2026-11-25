import numpy as np

class ChaoticRadialQuantumBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic radial basis with improved quantum interference
        r = np.sqrt(np.sum(x**2))
        chaotic_radial = np.sum(np.exp(-0.3 * (x**2) / (1.0 + 0.4 * np.sin(6.0 * r))) * 
                               np.cos(4.0 * r + 0.6 * np.sin(8.0 * r)) * 
                               np.sin(2.5 * r + 0.3 * np.cos(5.0 * r))) / self.dim
        
        # Enhanced asymmetric gradient field with multi-scale fractal patterns
        asym_grad = np.sum(np.abs(x)**1.7 * np.sin(x) * np.exp(-0.15 * np.abs(x)) * 
                          (1.0 + 0.25 * np.sin(4.0 * np.sum(x**2)))) / self.dim
        
        # Improved dynamic noise with enhanced quantum amplitude modulation
        noise = np.sum(np.sin(x * (1.0 + 0.5 * np.sin(0.4 * r))) * 
                      np.cos(x * (1.0 + 0.4 * np.cos(0.6 * r))) * 
                      np.exp(-0.08 * r**2)) / self.dim
        
        # Refined cross-term interaction with enhanced quantum coupling
        cross = np.sum(np.sin(x[:-1] * x[1:] * (1.0 + 0.15 * np.sin(3.0 * np.sum(x)))) * 
                      np.cos(x[:-1] + x[1:] + 0.4 * np.cos(4.0 * r))) / (self.dim - 1)
        
        # Enhanced fractal-like self-similarity with multi-scale interference
        fractal_multi = np.sum(np.sin(6.0 * x) * np.cos(4.0 * x) * 
                              np.exp(-0.05 * np.sum(x**2)) * 
                              (1.0 + 0.15 * np.sin(3.0 * r))) / self.dim
        
        # Enhanced adaptive conditioning with quantum-inspired scaling
        adaptive_cond = np.sum((x**2) * (1.0 + 0.6 * np.sin(0.6 * np.sum(x**2))) * 
                              np.cos(2.5 * x) * np.exp(-0.12 * np.abs(x))) / self.dim
        
        # Enhanced saddle-point with quantum harmonic components
        saddle = np.sum(x**3 * np.cos(x) - x**4 * np.sin(x) + 
                       0.6 * x**2 * np.tan(x/4.0) * np.exp(-0.015 * r**2)) / (self.dim * 12.0)
        
        # Enhanced quantum interference term with phase modulation
        quantum_interference = np.sum(np.sin(x * np.cos(x)) * np.cos(x * np.sin(x)) * 
                                    np.exp(-0.03 * r**2) * 
                                    (1.0 + 0.15 * np.sin(5.0 * r))) / self.dim
        
        # Combined weighted sum of all components with optimized weights
        total = 0.20 * chaotic_radial + 0.18 * asym_grad + 0.14 * noise + 0.12 * cross + \
                0.15 * fractal_multi + 0.14 * adaptive_cond + 0.11 * saddle + 0.06 * quantum_interference
        
        return total