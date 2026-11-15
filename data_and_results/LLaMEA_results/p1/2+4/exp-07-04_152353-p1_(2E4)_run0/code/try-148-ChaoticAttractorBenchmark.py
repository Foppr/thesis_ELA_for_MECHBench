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
        oscillation = 0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(i * 0.5)
            oscillation += np.sin(x_normalized[i] * freq * np.pi) * np.cos(x_normalized[i] * freq * np.pi / 2)
        
        # Radial basis function component with varying centers and widths
        rbf = 0
        for i in range(self.dim):
            center = np.sin(i * 0.3)
            width = 0.5 + 0.3 * np.cos(i * 0.4)
            rbf += np.exp(-0.5 * ((x_normalized[i] - center) / width)**2)
        
        # Asymmetric saddle point component with different exponents per dimension
        saddle = 0
        for i in range(self.dim):
            # Asymmetric behavior based on sign of dimension
            if x_normalized[i] >= 0:
                saddle += x_normalized[i]**(2.5 + 0.2 * np.sin(i * 0.6))
            else:
                saddle += x_normalized[i]**(3.0 + 0.1 * np.cos(i * 0.7))
        
        # Cross-term interaction with modified coupling strength
        cross = 0
        for i in range(self.dim - 1):
            cross += 0.3 * np.sin(x_normalized[i] * x_normalized[i+1] * 2) * (x_normalized[i]**2 + x_normalized[i+1]**2)
        
        # Combine all components with modified weights
        result = 0.3 * f1 + 0.25 * oscillation + 0.2 * rbf + 0.15 * saddle + 0.1 * cross
        
        # Add a small perturbation term to increase complexity
        perturbation = 0.02 * np.sum(np.sin(x_normalized * 7) * np.cos(x_normalized * 3))
        result += perturbation
        
        return result