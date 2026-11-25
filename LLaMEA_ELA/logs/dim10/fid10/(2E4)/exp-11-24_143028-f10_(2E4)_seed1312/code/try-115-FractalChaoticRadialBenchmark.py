import numpy as np

class FractalChaoticRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base radial component with fractal scaling
        result = 0.3 * np.sum(x**2) * np.exp(-0.05 * np.sum(x**2))
        
        # Chaotic radial basis functions with varying scales and offsets
        for i in range(self.dim):
            result += 1.2 * np.exp(-0.2 * (x[i] - 1.0)**2) + 0.8 * np.exp(-0.3 * (x[i] + 2.0)**2)
        
        # Trigonometric coupling with fractal frequency patterns
        for i in range(self.dim):
            result += 0.9 * np.sin(5 * x[i]) * np.cos(7 * x[i]) * np.sin(3 * x[i]**2)
        
        # Cross-dimensional chaotic interaction using sine products
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                result += 0.6 * np.sin(8 * x[i]) * np.cos(9 * x[j]) * np.sin(4 * (x[i] + x[j]))
        
        # Fractal-like self-similarity with recursive cosine terms
        for i in range(self.dim):
            result += 0.7 * np.cos(15 * x[i]) * np.cos(20 * x[i]**2) * np.cos(25 * x[i]**3)
        
        # Asymmetric boundary effects with exponential penalties
        for i in range(self.dim):
            if x[i] < 0:
                result += 1.1 * np.exp(-0.5 * x[i]) * (1 + 0.3 * np.sin(20 * x[i]))
            else:
                result += 0.9 * np.exp(-0.3 * (x[i] - 5.0)) * (1 + 0.2 * np.cos(18 * x[i]))
        
        # Multi-scale chaotic modulation using product of sine waves
        chaos = 1.0
        for i in range(self.dim):
            chaos *= np.sin(12 * x[i]) * np.cos(14 * x[i]) + 1.2
        result += 1.5 * chaos
        
        # Polynomial-trigonometric hybrid with dynamic coefficients
        poly_term = 0
        for i in range(self.dim):
            poly_term += 0.6 * x[i]**4 - 0.4 * x[i]**3 + 0.2 * x[i]**2
        result += 1.2 * poly_term * np.cos(6 * np.sum(x))
        
        # Additional fractal structure with nested sine waves
        for i in range(self.dim):
            result += 0.5 * np.sin(25 * x[i]) * np.sin(30 * x[i]**2) * np.sin(35 * x[i]**3)
        
        # Cross-dimensional exponential coupling with varying strengths
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.4 * np.exp(-np.abs(x[i] - x[j]) / (1 + 0.1 * np.abs(x[i] + x[j]))) * np.cos(8 * (x[i] - x[j]))
        
        # Asymmetric wave pattern with cubic modulation
        sum_x = np.sum(x)
        result += 1.3 * np.cos(18 * sum_x) * np.sin(15 * sum_x) * (1 + 0.2 * sum_x**3)
        
        # Quintic coupling with chaotic phase shifts
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                result += 0.3 * (x[i]**5 + x[j]**5) * np.sin(5 * (x[i] - x[j]))
        
        # Noise component with fractal frequency spectrum
        noise = 0.0
        for i in range(self.dim):
            noise += 0.15 * np.sin(30 * x[i]) * np.cos(25 * x[i])
        result += noise
        
        return result