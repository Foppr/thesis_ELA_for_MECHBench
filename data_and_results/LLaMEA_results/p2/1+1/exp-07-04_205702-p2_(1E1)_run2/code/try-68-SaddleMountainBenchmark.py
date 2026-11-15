import numpy as np

class SaddleMountainBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with adaptive conditioning
        f1 = 0.3 * np.sum(x**2)
        
        # Multiple asymmetric Gaussian peaks with chaotic positioning and varying scales
        peaks = []
        for i in range(6):
            mu = np.array([3.0 * np.sin(0.4 * i**1.5), 2.5 * np.cos(0.6 * i**1.3)] + [0.0] * (self.dim - 2))[:self.dim]
            sigma = 0.2 + 0.6 * np.sin(0.5 * i**1.2)
            height = 2.0 + 3.0 * np.cos(0.3 * i**1.4)
            peak = height * np.exp(-0.5 * np.sum(((x - mu) / sigma)**2))
            peaks.append(peak)
        
        f2 = np.sum(peaks)
        
        # Enhanced saddle point structure with chaotic modulation and cross-dimensional coupling
        f3 = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                f3 += np.tanh(x[i]) * np.tanh(x[j]) * np.sin(2.0 * x[i] * x[j]) * np.cos(0.5 * (x[i]**2 + x[j]**2))
        
        # Introduce chaotic gradient variations through fractional exponents and trigonometric modulation
        f4 = 0.0
        for i in range(self.dim):
            f4 += (np.abs(x[i])**1.9 + 0.1 * np.sin(3.0 * x[i])) * np.cos(2.0 * x[i])
        
        # Asymmetric basin structure with multi-scale exponential decay and fractal-like modulation
        f5 = 0.0
        for i in range(self.dim):
            f5 -= np.exp(-0.2 * (x[i] - 2.0)**2) * np.cos(0.8 * x[i]) * np.sin(0.3 * x[i]**3)
        
        # Cross-dimensional interaction terms with non-linear coupling and chaotic coupling coefficients
        f6 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f6 += 0.4 * np.sin(x[i] + x[j]) * np.cos(0.7 * x[i] * x[j]) * np.exp(-0.1 * np.abs(x[i] - x[j]))
        
        # Add chaotic noise term with fractal-like characteristics
        noise = 0.08 * np.random.rand() * np.sin(10.0 * np.sum(x**2))
        
        # Add a non-linear transformation term to increase complexity
        f7 = 0.5 * np.sin(0.5 * np.sum(x**3)) * np.cos(0.3 * np.sum(x**4))
        
        # Combine all components
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + noise