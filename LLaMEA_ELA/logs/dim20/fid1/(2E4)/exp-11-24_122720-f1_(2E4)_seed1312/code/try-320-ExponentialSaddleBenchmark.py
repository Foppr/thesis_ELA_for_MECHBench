import numpy as np

class ExponentialSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize exponential decay parameters for correlation structure
        self.decay_rates = np.random.uniform(0.1, 1.0, dim)
        # Sinusoidal modulation frequencies
        self.freqs = np.random.uniform(1.0, 5.0, dim)
        # Saddle point positions and strengths
        self.saddles = np.random.uniform(-3.0, 3.0, (dim, 2))
        self.saddle_strengths = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Exponentially decaying correlation component
        corr = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x[i] - x[j])
                # Exponential decay with dimension-specific rate
                corr += np.exp(-self.decay_rates[i] * dist) * np.sin(self.freqs[i] * x[i]) * np.cos(self.freqs[j] * x[j])
        
        # Sinusoidal modulation component
        sin_mod = 0.0
        for i in range(self.dim):
            sin_mod += np.sin(self.freqs[i] * x[i]) * np.cos(2.0 * x[i]) + 0.5 * np.sin(3.0 * x[i])
            
        # Saddle point attraction component
        saddle = 0.0
        for i in range(self.dim):
            # Two saddle points per dimension
            s1 = self.saddles[i, 0]
            s2 = self.saddles[i, 1]
            # Quadratic attraction with different strengths
            saddle += self.saddle_strengths[i] * (np.exp(-0.5 * (x[i] - s1)**2) - np.exp(-0.5 * (x[i] - s2)**2))
            
        # Polynomial curvature component with varying exponents
        poly = 0.0
        for i in range(self.dim):
            # Varying polynomial degrees for each dimension
            degree = 2 + int(3 * np.sin(i)) % 3
            poly += x[i]**degree
            
        # Cross-dimension interaction with exponential coupling
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Exponentially weighted interaction
                weight = np.exp(-0.1 * (i + j))
                cross += weight * np.sin(x[i] * x[j]) * np.cos(0.5 * (x[i] + x[j]))
                
        # Combine all components with dynamic scaling
        result = 2.0 * corr + 1.5 * sin_mod + 0.8 * saddle + 1.2 * poly + 0.6 * cross
        
        # Add dimensionality-dependent normalization
        norm_factor = np.sqrt(self.dim)
        result /= norm_factor
        
        return result