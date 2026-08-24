import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component
        result = np.sum(x**2)
        
        # Radial basis function with multiple centers
        centers = np.linspace(-4.0, 4.0, min(5, self.dim))
        rbf = 0.0
        for i in range(len(centers)):
            rbf += np.exp(-0.5 * np.sum((x - centers[i])**2))
        result += 1.5 * rbf
        
        # Sinusoidal modulations with varying frequencies and amplitudes
        sin_mod = 0.0
        for i in range(self.dim):
            sin_mod += np.sin(2.0 * np.pi * x[i]) * np.cos(3.0 * np.pi * x[i])
        result += 0.8 * sin_mod
        
        # Asymmetric gradient flow terms
        asym = 0.0
        for i in range(self.dim - 1):
            asym += (x[i] - x[i+1])**2 * np.sin(x[i] + x[i+1])
        result += 0.6 * asym
        
        # Polynomial coupling with exponential decay
        poly_coupling = 0.0
        for i in range(self.dim - 1):
            poly_coupling += (x[i]**3 + x[i+1]**3) * np.exp(-0.1 * (x[i] - x[i+1])**2)
        result += 0.5 * poly_coupling
        
        # Saddle point perturbations using hyperbolic functions
        saddle = 0.0
        for i in range(self.dim):
            saddle += np.tanh(x[i]) * np.cos(2.0 * x[i])
        result += 0.3 * saddle
        
        # High-frequency oscillatory component with amplitude modulation
        high_freq = 0.0
        for i in range(self.dim):
            high_freq += np.sin(15.0 * x[i]) * np.cos(12.0 * x[i]) * (1.0 + 0.1 * np.sin(5.0 * x[i]))
        result += 0.2 * high_freq
        
        # Additional multimodal structure using exponential and trigonometric combinations
        multimodal = 0.0
        for i in range(self.dim):
            multimodal += np.exp(-0.5 * (x[i] - 2.0)**2) * np.sin(3.0 * x[i])
        result += 0.4 * multimodal
        
        return result