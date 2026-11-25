import numpy as np

class ChaoticQuaternionBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Enhanced quaternion-inspired coupling with chaotic modulation
        for i in range(self.dim):
            xi = x[i]
            # Chaotic sine modulation based on previous dimensions
            chaotic_mod = 1.0 + 0.4 * np.sin(xi) * np.cos(2.0 * xi)
            if i > 0:
                chaotic_mod *= (1.0 + 0.3 * np.sin(x[i-1]) * np.cos(x[i-1]))
            
            # Enhanced quaternion-like interaction term
            quaternion_term = np.sin(xi) * np.cos(xi) * np.exp(-xi**2 / 8.0)
            result += chaotic_mod * quaternion_term
            
        # Fractal sinusoidal landscape with multi-scale frequency
        r = np.sqrt(np.sum(x**2))
        if r > 1e-8:
            for scale in [1, 2, 3]:
                freq = scale * (1.5 + np.sin(r / 4.0)) * np.cos(r / 2.0)
                fractal_harmonic = np.sin(freq * r) * np.cos(freq * r)
                result += 0.6 * fractal_harmonic * np.exp(-r**2 / (8.0 * scale))
        
        # Saddle-point dominance with polynomial perturbations
        saddle_sum = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Enhanced polynomial with alternating signs to create saddle points
            poly_term = xi**5 - 12*xi**3 + 30*xi
            saddle_sum += poly_term * np.exp(-abs(xi) / 2.5)
        result += 0.9 * saddle_sum
        
        # Cross-dimensional chaotic coupling with exponential weights
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                # Enhanced chaotic weight based on both variables
                weight = 1.0 + 0.5 * np.sin(xi) * np.cos(xj) * np.exp(-abs(xi - xj) / 3.0)
                coupling = weight * (np.sin(xi) * np.cos(xj) - np.cos(xi) * np.sin(xj))
                result += coupling * np.exp(-((xi - xj)**2) / 4.0)
        
        # Multi-modal component with complex angular interactions
        angular_sum = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Enhanced angular modulation
            angular_mod = np.sin(4.0 * xi) * np.cos(3.0 * xi) + 0.6 * np.sin(xi)
            angular_sum += angular_mod * np.exp(-xi**2 / 6.0)
        result += 0.7 * angular_sum
        
        # Additional chaotic oscillation with radial dependency
        if r > 1e-8:
            chaos_freq = 10.0 * np.sin(r / 3.0) + 4.0 * np.cos(r / 1.5)
            chaos_component = np.sin(chaos_freq * r) * np.cos(chaos_freq * r) * np.exp(-r**2 / 20.0)
            result += 0.5 * chaos_component
            
        # Final normalization and scaling
        result = result / (1.0 + 0.15 * r)
        
        return result