import numpy as np

class ChaoticEllipticBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base elliptic term with adaptive condition number
        f1 = 0.0
        for i in range(self.dim):
            f1 += (10 ** (2 * i / (self.dim - 1))) * x[i]**2
        
        # Add periodic modulations with chaotic frequency ratios
        f2 = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(0.3 * i + 1.2 * np.sum(x))
            amp = 1.0 + 0.3 * np.cos(0.7 * i + 0.8 * np.sum(x))
            f2 += amp * np.sin(freq * x[i]) * np.cos(freq * x[i]**2)
        
        # Introduce cross-dimensional coupling with chaotic interaction
        f3 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction = np.sin(0.5 * x[i] * x[j] + 0.2 * np.sin(1.3 * x[i]))
                f3 += interaction * (x[i]**2 + x[j]**2) / (1.0 + np.abs(x[i] - x[j]))
        
        # Add asymmetric saddle structures with varying steepness
        f4 = 0.0
        for i in range(self.dim):
            steepness = 1.0 + 0.5 * np.sin(0.4 * i)
            f4 += steepness * x[i] * np.tanh(x[i]) * np.cos(0.3 * x[i]**2)
        
        # Include high-order polynomial terms with chaotic coefficients
        f5 = 0.0
        for i in range(self.dim):
            coeff = 0.5 + 0.5 * np.sin(0.6 * i + 0.9 * np.sum(x))
            f5 += coeff * x[i]**4 * np.sin(0.2 * x[i])
        
        # Add chaotic noise component with dynamic amplitude
        noise_amp = 0.1 + 0.05 * np.sin(0.8 * np.sum(x))
        noise = noise_amp * np.random.rand() * np.sin(3.0 * np.sum(x))
        
        # Combine all components
        return f1 + f2 + f3 + f4 + f5 + noise