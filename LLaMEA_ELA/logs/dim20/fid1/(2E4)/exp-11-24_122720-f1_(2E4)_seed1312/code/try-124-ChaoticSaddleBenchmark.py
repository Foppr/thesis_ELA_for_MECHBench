import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Quantum-inspired parameters
        self.omega = 2.0 * np.pi
        self.gamma = 0.1
        self.alpha = 0.5
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum-inspired harmonic oscillator component
        quantum_sum = 0
        for i in range(self.dim):
            # Harmonic potential with quantum-like oscillations
            freq = self.omega * (1 + 0.1 * np.sin(i * np.pi / (self.dim + 1)))
            quantum_sum += 0.5 * freq**2 * x[i]**2 + 0.5 * x[i]**4
            
        # Fractional Brownian motion effects
        fbm_sum = 0
        hurst = 0.3 + 0.4 * np.sin(self.dim * np.pi / (self.dim + 2))
        for i in range(self.dim):
            # Simulate long-range dependence with fractional integration
            fbm_val = np.sum([x[j] * (i - j)**(-hurst) for j in range(i)])
            fbm_sum += fbm_val**2
            
        # Adaptive penalty landscape
        penalty_sum = 0
        for i in range(self.dim):
            # Variable penalty based on distance from center
            center = 2.0 * np.cos(i * np.pi / (self.dim + 2))
            dist = np.abs(x[i] - center)
            penalty = 10.0 * (dist > 3.0) * (dist - 3.0)**2
            penalty_sum += penalty
            
        # Nested sinusoidal modulations
        nested_sum = 0
        for i in range(self.dim):
            mod_freq = 2.0 + np.sin(i * np.pi / (self.dim + 1))
            nested_sum += np.sin(mod_freq * x[i]) * np.cos(2 * x[i])
            
        # Dynamic coupling weights with memory effect
        coupling_sum = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Memory-dependent weight based on previous dimensions
                if i > 0:
                    weight = np.sin(i * j / (self.dim + 1)) * np.cos(x[i-1] + x[j])
                else:
                    weight = np.sin(i * j / (self.dim + 1))
                coupling_sum += weight * x[i] * x[j]
                
        # Saddle point interactions
        saddle_sum = 0
        for i in range(self.dim):
            # Create saddle points with varying heights
            saddle_height = 2.0 + np.sin(i * np.pi / (self.dim + 3))
            saddle_val = (x[i]**2 - saddle_height)**2
            saddle_sum += saddle_val
            
        # Chaotic logistic map perturbations for increased complexity
        chaotic_sum = 0
        r = 3.95  # Chaos parameter
        for i in range(self.dim):
            # Logistic map with dimension-dependent control
            logistic_val = r * x[i] * (1 - x[i])
            chaotic_sum += np.sin(logistic_val) * np.cos(x[i]**3)
            
        # Global scaling factor based on dimensionality
        scale_factor = 1.0 + 0.5 * np.sin(self.dim * np.pi / 6)
        
        return scale_factor * (quantum_sum + fbm_sum + penalty_sum + nested_sum + coupling_sum + saddle_sum + chaotic_sum)