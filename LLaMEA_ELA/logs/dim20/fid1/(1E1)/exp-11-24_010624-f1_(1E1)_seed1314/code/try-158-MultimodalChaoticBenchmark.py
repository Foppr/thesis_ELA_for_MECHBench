import numpy as np

class MultimodalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute frequency parameters for oscillatory components
        self.freq_params = np.array([1.0 + 0.5 * np.sin(i * 0.8) for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Sinusoidal oscillation component with varying frequencies
        for i in range(self.dim):
            result += np.sin(self.freq_params[i] * x[i]) * np.cos(self.freq_params[i] * x[i]**2)
            
        # Radial basis function component with exponential decay
        for i in range(self.dim):
            result += 0.1 * np.exp(-0.5 * (x[i] / (1.0 + 0.1 * i))**2) * np.sin(3 * x[i])
            
        # Cross-dimensional coupling with trigonometric interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(x[i] * x[j]) * np.cos((x[i] + x[j])**2)
                result += 0.05 * coupling / (1.0 + np.abs(x[i] - x[j]))
                
        # Add a modified Rastrigin-like component with dynamic amplitude
        rastrigin_term = 0.0
        for i in range(self.dim):
            rastrigin_term += x[i]**2 - 10 * np.cos(2 * np.pi * x[i])
        result += 0.5 * rastrigin_term
        
        # Add a chaotic logistic map component with dynamic parameter
        for i in range(self.dim):
            chaos_param = 3.9 + 0.1 * np.sin(i * 0.5)
            result += 0.02 * chaos_param * x[i] * (1 - x[i]**2)
            
        # Add a periodic component with varying periods
        periodic_term = 0.0
        for i in range(self.dim):
            periodic_term += np.sin(2 * np.pi * x[i] / (1.0 + 0.1 * i)) * np.cos(3 * np.pi * x[i] / (1.0 + 0.2 * i))
        result += 0.03 * periodic_term
        
        # Add a modified Schwefel-like component
        schwefel_term = 0.0
        for i in range(self.dim):
            schwefel_term += -x[i] * np.sin(np.sqrt(np.abs(x[i])))
        result += 0.015 * schwefel_term
        
        # Add noise to increase irregularity
        noise = 0.005 * np.sum(np.sin(10 * x))
        result += noise
        
        return result