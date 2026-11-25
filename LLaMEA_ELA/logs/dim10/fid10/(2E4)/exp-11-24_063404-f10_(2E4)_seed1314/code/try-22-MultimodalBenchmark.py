import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Fractal-like radial component with polynomial modulation and multiple frequency bands
        r = np.sqrt(np.sum(x_scaled**2))
        radial = (np.sin(13 * r) * np.cos(7 * r) + 
                  0.5 * np.sin(23 * r) * np.cos(11 * r) + 
                  0.2 * np.sin(31 * r) * np.cos(17 * r) +
                  0.05 * np.sin(41 * r))
        
        # Periodic wave interference with asymmetric cross-terms
        interference = 0.0
        if self.dim > 1:
            for i in range(min(4, self.dim)):
                for j in range(i+1, min(5, self.dim)):
                    dist = np.sqrt((x_scaled[i] - x_scaled[j])**2 + 0.01)
                    interference += np.sin(10 * dist) * np.cos(8 * dist) * (i + j) / (i * j + 1)
        
        # Polynomial modulation with stochastic perturbations
        polynomial = np.sum((x_scaled**4 + 0.3 * x_scaled**3 + 0.1 * x_scaled**2) * 
                           (1.0 + 0.05 * np.random.randn(self.dim)))
        
        # Stochastic perturbation to increase ruggedness and non-smoothness
        stochastic = 0.01 * np.sum(np.sin(100 * x_scaled) * np.cos(97 * x_scaled))
        
        # Cross-term interactions with asymmetric coupling
        cross_terms = 0.1 * np.sum(x_scaled[:-1] * x_scaled[1:]**2) + \
                     0.05 * np.sum(np.abs(x_scaled[:-2]) * x_scaled[1:-1] * x_scaled[2:])
        
        # Combine all components with carefully tuned weights
        return radial + 0.4 * interference + 0.3 * polynomial + 0.1 * stochastic + 0.05 * cross_terms + 0.001 * np.sum(x_scaled**6)