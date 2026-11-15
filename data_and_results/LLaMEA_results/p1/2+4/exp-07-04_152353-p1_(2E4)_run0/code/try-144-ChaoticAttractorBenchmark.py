import numpy as np

class ChaoticAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for better numerical stability
        x_normalized = x / 5.0
        
        # Base quadratic term
        f1 = np.sum(x_normalized**2)
        
        # Sinusoidal oscillation component with varying frequencies
        sin_term = 0
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(i * 0.5)
            sin_term += np.sin(freq * x_normalized[i])**2
            
        # Radial basin component with different scaling per dimension
        radial = 0
        for i in range(self.dim):
            scale = 1.0 + 0.5 * np.cos(i * 0.3)
            radial += scale * (x_normalized[i]**2 + 0.1 * np.sin(10 * x_normalized[i])**2)
            
        # Cross-term interaction with varying coupling strength
        cross = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.3 + 0.2 * np.sin(i * 0.4 + j * 0.3)
                cross += coupling * x_normalized[i] * x_normalized[j] * np.cos(x_normalized[i] + x_normalized[j])
                
        # Non-smooth component with varying exponents
        nonsmooth = 0
        for i in range(self.dim):
            exp = 1.5 + 0.8 * np.sin(i * 0.6)
            nonsmooth += np.abs(x_normalized[i])**exp
            
        # Combined result with modified weights
        result = 0.3 * f1 + 0.25 * sin_term + 0.2 * radial + 0.15 * cross + 0.1 * nonsmooth
        
        # Add a small perturbation term
        perturbation = 0.02 * np.sum(np.sin(7 * x_normalized) * np.cos(3 * x_normalized))
        result += perturbation
        
        return result