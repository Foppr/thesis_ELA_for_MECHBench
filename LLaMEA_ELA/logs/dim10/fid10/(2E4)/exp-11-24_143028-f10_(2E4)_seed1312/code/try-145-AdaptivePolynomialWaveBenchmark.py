import numpy as np

class AdaptivePolynomialWaveBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial valley components with varying degrees
        result = 0.0
        for i in range(self.dim):
            result += 0.5 * (x[i]**4 - 6*x[i]**2 + 8*x[i]) + 0.3 * x[i]**6
        
        # Sinusoidal wave components with adaptive frequencies
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(x[i])
            result += 1.2 * np.sin(freq * x[i]) * np.cos(freq * x[i])
        
        # Radial basis functions with dynamic centers and widths
        centers = np.linspace(-4, 4, min(5, self.dim))
        widths = 0.5 + 0.3 * np.abs(x)
        for i in range(min(5, self.dim)):
            result += 2.0 * np.exp(-0.5 * ((x[i] - centers[i]) / (widths[i] + 0.1))**2)
        
        # Cross-dimensional coupling with polynomial interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.8 * (x[i]**2 + x[j]**2) * np.sin(0.5 * (x[i] - x[j]))
        
        # Adaptive conditioning based on dimensionality
        cond_factor = 1.0
        for i in range(self.dim):
            cond_factor *= (1.0 + 0.2 * np.abs(x[i]))
        result *= cond_factor
        
        # Asymmetric penalty near boundaries with wave modulation
        for i in range(self.dim):
            if x[i] < -4:
                result += 1.5 * np.exp(-0.3 * (x[i] + 5.0)**2) * (1 + 0.3 * np.sin(10 * x[i]))
            elif x[i] > 4:
                result += 1.5 * np.exp(-0.3 * (x[i] - 5.0)**2) * (1 + 0.3 * np.cos(10 * x[i]))
        
        # Additional harmonic structure with varying amplitudes
        for i in range(self.dim):
            result += 0.6 * np.sin(3 * x[i]) * np.cos(2 * x[i]) * (1 + 0.1 * x[i]**2)
        
        # Cross-dimensional polynomial coupling with higher-order terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.3 * (x[i]**3 + x[j]**3) * np.cos(0.3 * (x[i] + x[j]))
        
        # Enhanced boundary handling with exponential damping
        for i in range(self.dim):
            if abs(x[i]) > 4.5:
                result += 2.0 * np.exp(-2.0 * (abs(x[i]) - 4.5)**2)
        
        # Add a small Gaussian noise term to increase robustness
        result += 0.01 * np.random.rand()
        
        return result