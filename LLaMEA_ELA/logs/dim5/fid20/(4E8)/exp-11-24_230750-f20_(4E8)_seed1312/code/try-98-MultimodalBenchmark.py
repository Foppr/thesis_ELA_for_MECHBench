import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay potentials with varying rates
        exp_potential = np.sum(np.exp(-0.5 * (x / 1.5)**2) * np.sin(2 * x))
        
        # Logarithmic barrier components creating irregular fitness landscapes
        log_barrier = 0.0
        for i in range(self.dim):
            log_barrier += np.log(1.0 + 0.1 * (x[i] - 2.0)**2) * np.cos(0.5 * x[i])
        
        # Quaternion-inspired coupling terms with complex interaction patterns
        quat_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                if j < self.dim:
                    quat_coupling += (x[i]**2 + x[j]**2) * np.sin(0.3 * x[i] * x[j])
        
        # Multi-scale sinusoidal modulation with dynamic frequency
        modulated_sine = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(0.2 * i)
            modulated_sine += np.sin(freq * x[i]) * np.cos(0.7 * x[i]**2)
        
        # Chaotic logistic map based dimension coupling
        chaotic_term = 0.0
        for i in range(self.dim - 1):
            chaotic_term += (x[i] * x[i+1]) * (1.0 - x[i]**2) * np.sin(0.4 * x[i])
        
        # Asymmetric hyperbolic tangent ridges with variable steepness
        tanh_ridge = 0.0
        for i in range(self.dim):
            steepness = 1.5 + 0.5 * np.sin(i * 0.3)
            tanh_ridge += np.tanh(steepness * (x[i] - 1.0)) * np.exp(-0.1 * x[i]**2)
        
        # Combined function with dynamic scaling factor
        base_value = np.sum(x**4) + 0.3 * np.sum(np.abs(x)**3) + 0.05 * np.sum(x**2)
        scale_factor = 1.0 + 0.3 * np.sin(self.dim * 0.1) * np.mean(np.abs(x))
        
        # Add noise component
        noise = 0.08 * np.random.rand() * np.sum(np.sin(3 * x) * np.cos(2 * x))
        
        return scale_factor * base_value + exp_potential + log_barrier + quat_coupling + modulated_sine + chaotic_term + tanh_ridge + noise