import numpy as np

class HyperbolicCosineFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Hyperbolic tangent radial basis with sine modulation
        r = np.sqrt(np.sum(x**2))
        tanh_radial = np.sum(np.tanh(0.3 * (x**2)) * 
                           np.sin(2.0 * r + 0.4 * np.cos(3.0 * r)) * 
                           np.cos(1.5 * r + 0.3 * np.sin(5.0 * r))) / self.dim
        
        # Asymmetric sine gradient field with fractal scaling
        sin_grad = np.sum(np.sin(x)**2 * np.exp(-0.2 * np.abs(x)) * 
                         (1.0 + 0.3 * np.cos(4.0 * np.sum(x**2)))) / self.dim
        
        # Dynamic phase-coupled noise with hyperbolic decay
        phase_noise = np.sum(np.sin(x * (1.0 + 0.5 * np.sin(0.4 * r))) * 
                           np.cos(x * (1.0 + 0.3 * np.cos(0.6 * r))) * 
                           np.tanh(-0.08 * r**2)) / self.dim
        
        # Cross-dimensional interaction with harmonic coupling (modified frequency)
        cross = np.sum(np.sin(x[:-1] * x[1:] * (1.0 + 0.2 * np.sin(5.0 * np.sum(x)))) * 
                      np.cos(x[:-1] + x[1:] + 0.4 * np.cos(3.0 * r))) / (self.dim - 1)
        
        # Fractal self-similarity with multi-scale sine patterns
        fractal_multi = np.sum(np.sin(4.0 * x) * np.cos(2.0 * x) * 
                              np.tanh(-0.05 * np.sum(x**2)) * 
                              (1.0 + 0.15 * np.sin(3.0 * r))) / self.dim
        
        # Adaptive conditioning with harmonic scaling
        adaptive_cond = np.sum((x**2) * (1.0 + 0.4 * np.sin(0.6 * np.sum(x**2))) * 
                              np.cos(2.0 * x) * np.tanh(-0.15 * np.abs(x))) / self.dim
        
        # Saddle-point with harmonic components
        saddle = np.sum(x**3 * np.cos(x) - x**4 * np.sin(x) + 
                       0.3 * x**2 * np.log(1.0 + np.abs(x)) * np.tanh(-0.02 * r**2)) / (self.dim * 15.0)
        
        # Quantum harmonic interference term
        quantum_harmonic = np.sum(np.sin(x * np.cos(x)) * np.cos(x * np.sin(x)) * 
                                np.tanh(-0.03 * r**2) * 
                                (1.0 + 0.2 * np.sin(5.0 * r)) * 
                                np.cos(0.5 * r)) / self.dim
        
        # Combined weighted sum of all components
        total = 0.2 * tanh_radial + 0.18 * sin_grad + 0.15 * phase_noise + 0.12 * cross + \
                0.13 * fractal_multi + 0.12 * adaptive_cond + 0.08 * saddle + 0.07 * quantum_harmonic
        
        return total