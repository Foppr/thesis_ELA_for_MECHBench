import numpy as np

class MultiModalRidgeBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = 0.1 * np.sum(x**2)
        
        # Add multiple sinusoidal ridges
        for i in range(1, min(self.dim + 1, 6)):
            # Ridge pattern with varying frequency and amplitude
            freq = i * 0.5
            amp = 2.0 / (i * 0.5)
            
            # Create ridge along dimension i-1
            if i <= self.dim:
                ridge_value = amp * np.sin(freq * x[i-1])
                result += ridge_value**2
        
        # Add Gaussian valleys to create local minima
        for i in range(1, min(self.dim + 1, 5)):
            # Valley centers with exponential spacing
            center = i * 0.8 * np.sin(i * 0.7)
            valley_amp = 1.5 / (i * 0.3)
            
            if i <= self.dim:
                dist_from_center = x[i-1] - center
                # Gaussian valley term
                result += valley_amp * np.exp(-dist_from_center**2 / (2 * (i * 0.2)**2))
        
        # Add coupling terms between dimensions to increase complexity
        for i in range(self.dim - 1):
            for j in range(i + 1, min(self.dim, i + 3)):
                coupling = 0.5 * np.sin(x[i] * x[j] * 0.3)
                result += coupling
        
        # Add noise to increase ruggedness
        noise = 0.1 * np.sum(np.sin(10 * x))
        
        return result + noise