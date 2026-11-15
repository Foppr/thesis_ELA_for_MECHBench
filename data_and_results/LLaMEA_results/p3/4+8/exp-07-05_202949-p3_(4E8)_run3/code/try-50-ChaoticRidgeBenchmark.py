import numpy as np

class ChaoticRidgeBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for fractional Brownian motion-like behavior
        self.hurst = 0.3
        self.frac_weights = np.array([1.0 / (2**i) for i in range(1, dim+1)])
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with asymmetric scaling
        result = 0.0
        for i in range(self.dim):
            asym_factor = 1.0 + 0.5 * np.sin(i)
            result += asym_factor * (x[i] - 0.5)**2 + 0.3 * (x[i] + 0.5)**4
        
        # Nested attractor terms with chaotic coupling
        for i in range(self.dim):
            attractor_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    coupling = np.exp(-0.5 * (x[i] - x[j])**2)
                    attractor_sum += coupling * np.sin(2.0 * (x[i] + x[j]))
            result += 0.2 * attractor_sum**2
        
        # Fractional Brownian motion inspired component
        fbm_term = 0.0
        for i in range(self.dim):
            fbm_sum = 0.0
            for j in range(i):
                distance = np.abs(x[i] - x[j])
                fbm_sum += self.frac_weights[j] * np.sin(distance**(2 * self.hurst))
            fbm_term += fbm_sum**2
        result += 0.1 * fbm_term
        
        # Asymmetric ridge structure with multiple peaks
        ridge_term = 0.0
        for i in range(self.dim):
            ridge_term += np.sin(3.0 * x[i]) * np.cos(2.0 * x[i]) + 0.5 * np.sin(5.0 * x[i])
            ridge_term += 0.3 * np.sin(7.0 * x[i]) * np.cos(4.0 * x[i])
        result += 0.25 * ridge_term**2
        
        # Chaotic sinusoidal modulation with varying frequencies
        chaotic_term = 0.0
        for i in range(self.dim):
            freq = 2.0 + 0.5 * np.sin(i)
            chaotic_term += np.sin(freq * x[i]) * np.cos(freq * x[i])
        result += 0.1 * chaotic_term**3
        
        # Add a global scaling factor to increase ruggedness
        result *= (1.0 + 0.1 * np.sum(np.abs(x)))
        
        return result