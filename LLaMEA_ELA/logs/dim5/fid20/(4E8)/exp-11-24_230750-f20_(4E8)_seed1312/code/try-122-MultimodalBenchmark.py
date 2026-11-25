import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic logistic map component with dynamic parameter
        logistic_sum = 0.0
        r = 3.95
        for i in range(self.dim):
            if i == 0:
                x_prev = 0.5
            else:
                x_prev = x[i-1]
            logistic_sum += r * x_prev * (1 - x_prev)
        
        # Spectral clustering inspired energy terms with adaptive weights
        spectral_energy = 0.0
        for i in range(self.dim):
            weight = 1.0 + 0.5 * np.sin(i * 0.3)
            spectral_energy += weight * np.sin(2.0 * x[i]) * np.cos(1.5 * x[i])
        
        # Fractional Brownian motion inspired component with Hurst parameter
        hurst = 0.7 + 0.1 * np.sin(self.dim * 0.2)
        fbm_term = 0.0
        for i in range(self.dim):
            fbm_term += np.random.normal(0, 1) * (i + 1)**(-hurst)
        
        # Quantum-like interference pattern with phase modulation
        quantum_interference = 0.0
        for i in range(self.dim):
            phase = 2.0 * np.pi * (i + 1) / self.dim
            quantum_interference += np.sin(x[i] + phase) * np.cos(x[i] - phase)
        
        # Non-local interaction term with multi-scale coupling
        nonlocal_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                distance = np.abs(x[i] - x[j])
                nonlocal_interaction += np.exp(-distance**2 / (2 * (i + j + 1)**2))
        
        # Polynomial cross-terms with dynamic exponents
        poly_cross = 0.0
        for i in range(self.dim - 2):
            exponent = 2.0 + 0.5 * np.sin(i * 0.4)
            poly_cross += x[i]**exponent * x[i+1]**(exponent + 0.5) * x[i+2]**(exponent + 1.0)
        
        # Final combined function value with dynamic scaling
        total = (logistic_sum + spectral_energy + fbm_term + quantum_interference + 
                nonlocal_interaction + poly_cross)
        
        return total * (1.0 + 0.1 * np.sin(self.dim * 0.5))