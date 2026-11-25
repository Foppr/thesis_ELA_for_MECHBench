import numpy as np

class ChaoticRadialPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base radial term with dynamic conditioning
        result = 0.5 * np.sum(x**2) * np.exp(-0.1 * np.sum(x**2))
        
        # Chaotic sine-wave modulation with varying frequencies
        for i in range(self.dim):
            result += 2.0 * np.sin(13 * x[i]) * np.cos(11 * x[i]) * np.sin(9 * x[i])
        
        # Radial basis functions with dynamic widths and centers
        for i in range(self.dim):
            result += 1.5 * np.exp(-0.3 * (x[i] - 2.0)**2) + 1.0 * np.exp(-0.5 * (x[i] + 3.0)**2) + 0.7 * np.exp(-0.4 * (x[i] - 1.5)**2)
        
        # Cross-dimensional polynomial coupling with dynamic exponents
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                result += 0.8 * (x[i]**3 + x[j]**3) * np.cos(7 * (x[i] - x[j]))
        
        # Asymmetric boundary penalties with hyperbolic tangent
        for i in range(self.dim):
            if x[i] < 0:
                result += 1.8 * np.tanh(2.5 * x[i]) * (1 + 0.5 * np.sin(15 * x[i]))
            else:
                result += 1.4 * np.tanh(3.0 * (x[i] - 5.0)) * (1 + 0.4 * np.cos(12 * x[i]))
        
        # High-frequency chaotic component with sine and cosine products
        chaos = 1.0
        for i in range(self.dim):
            chaos *= np.sin(20 * x[i]) * np.cos(18 * x[i]) + 1.5
        result += 1.3 * chaos
        
        # Fractal-like structure with recursive cosine terms
        for i in range(self.dim):
            result += 0.9 * np.cos(30 * x[i]) * np.sin(27 * x[i]) * np.cos(24 * x[i]**2)
        
        # Weighted polynomial and trigonometric interaction
        poly_term = 0
        for i in range(self.dim):
            poly_term += 0.8 * x[i]**6 - 0.5 * x[i]**5 + 0.3 * x[i]**4 - 0.1 * x[i]**3
        result += 1.1 * poly_term * np.cos(5 * np.sum(x))
        
        # Additional cross-dimensional exponential coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.6 * np.exp(-np.abs(x[i] - x[j]) / (1 + 0.2 * np.abs(x[i] + x[j]))) * np.sin(10 * (x[i] - x[j]))
        
        # Asymmetric wave pattern with cubic modulation
        sum_x = np.sum(x)
        result += 1.9 * np.sin(25 * sum_x) * np.cos(20 * sum_x) * (1 + 0.3 * sum_x**3)
        
        # Quintic polynomial coupling between dimensions
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                result += 0.4 * (x[i]**5 + x[j]**5) * np.cos(6 * (x[i] - x[j]))
        
        # Noise component with multiple sine waves
        noise = 0.0
        for i in range(self.dim):
            noise += 0.2 * np.sin(40 * x[i]) * np.cos(35 * x[i])
        result += noise
        
        # Enhanced multimodality through additional chaotic sine products
        for i in range(self.dim):
            for j in range(i+1, min(i+2, self.dim)):
                result += 0.3 * np.sin(30 * x[i]) * np.cos(25 * x[j]) * np.sin(20 * (x[i] + x[j]))
        
        # Additional polynomial coupling with variable coefficients
        for i in range(self.dim):
            result += 0.5 * (x[i]**4 - 2*x[i]**2 + 1) * np.cos(8 * x[i])
            
        # Cross-dimensional exponential coupling with varying strength
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                result += 0.7 * np.exp(-0.5 * (x[i] - x[j])**2) * np.sin(15 * (x[i] + x[j]))
        
        # Enhanced boundary effects
        for i in range(self.dim):
            if x[i] > 4.0:
                result += 2.0 * np.exp(-0.5 * (x[i] - 4.0)**2) * np.sin(20 * x[i])
            elif x[i] < -4.0:
                result += 1.5 * np.exp(-0.3 * (x[i] + 4.0)**2) * np.cos(18 * x[i])
        
        return result