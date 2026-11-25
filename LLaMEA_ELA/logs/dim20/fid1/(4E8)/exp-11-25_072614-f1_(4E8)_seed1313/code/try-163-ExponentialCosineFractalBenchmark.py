import numpy as np

class ExponentialCosineFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential radial basis with cosine modulation
        r = np.sqrt(np.sum(x**2))
        exp_radial = np.sum(np.exp(-0.3 * (x**2)) * 
                           np.cos(2.0 * r + 0.4 * np.sin(3.0 * r)) * 
                           np.sin(1.5 * r + 0.3 * np.cos(5.0 * r))) / self.dim
        
        # Asymmetric cosine gradient field with fractal scaling
        cos_grad = np.sum(np.cos(x)**2 * np.exp(-0.2 * np.abs(x)) * 
                         (1.0 + 0.3 * np.sin(4.0 * np.sum(x**2)))) / self.dim
        
        # Dynamic phase-coupled noise with exponential decay
        phase_noise = np.sum(np.cos(x * (1.0 + 0.5 * np.cos(0.4 * r))) * 
                           np.sin(x * (1.0 + 0.3 * np.sin(0.6 * r))) * 
                           np.exp(-0.08 * r**2)) / self.dim
        
        # Cross-dimensional interaction with harmonic coupling
        cross = np.sum(np.cos(x[:-1] * x[1:] * (1.0 + 0.2 * np.cos(3.0 * np.sum(x)))) * 
                      np.sin(x[:-1] + x[1:] + 0.4 * np.sin(2.0 * r))) / (self.dim - 1)
        
        # Fractal self-similarity with multi-scale cosine patterns
        fractal_multi = np.sum(np.cos(4.0 * x) * np.sin(2.0 * x) * 
                              np.exp(-0.05 * np.sum(x**2)) * 
                              (1.0 + 0.15 * np.cos(3.0 * r))) / self.dim
        
        # Adaptive conditioning with harmonic scaling
        adaptive_cond = np.sum((x**2) * (1.0 + 0.4 * np.cos(0.6 * np.sum(x**2))) * 
                              np.sin(2.0 * x) * np.exp(-0.15 * np.abs(x))) / self.dim
        
        # Saddle-point with harmonic components
        saddle = np.sum(x**3 * np.sin(x) - x**4 * np.cos(x) + 
                       0.3 * x**2 * np.log(1.0 + np.abs(x)) * np.exp(-0.02 * r**2)) / (self.dim * 15.0)
        
        # Quantum harmonic interference term
        quantum_harmonic = np.sum(np.cos(x * np.sin(x)) * np.sin(x * np.cos(x)) * 
                                np.exp(-0.03 * r**2) * 
                                (1.0 + 0.2 * np.cos(5.0 * r))) / self.dim
        
        # Combined weighted sum of all components
        total = 0.2 * exp_radial + 0.18 * cos_grad + 0.15 * phase_noise + 0.12 * cross + \
                0.13 * fractal_multi + 0.12 * adaptive_cond + 0.08 * saddle + 0.07 * quantum_harmonic
        
        return total