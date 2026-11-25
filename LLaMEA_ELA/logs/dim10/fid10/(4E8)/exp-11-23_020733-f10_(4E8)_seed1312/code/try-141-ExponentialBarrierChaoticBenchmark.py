import numpy as np

class ExponentialBarrierChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute exponential decay parameters
        self.decay_rates = np.random.uniform(0.1, 1.5, dim)
        self.barrier_centers = np.random.uniform(-4.0, 4.0, dim)
        self.barrier_heights = np.random.uniform(1.0, 3.0, dim)
        # Chaotic modulation parameters
        self.chaotic_freqs = np.random.uniform(2.0, 8.0, dim)
        self.chaotic_ampls = np.random.uniform(0.5, 1.5, dim)
        # Logarithmic barrier parameters
        self.log_barrier_params = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Base exponential decay potential
        for i in range(self.dim):
            decay_term = np.exp(-self.decay_rates[i] * np.abs(x[i]))
            result += decay_term
            
        # Logarithmic barrier functions with adaptive scaling
        for i in range(self.dim):
            # Distance to barrier center
            dist = np.abs(x[i] - self.barrier_centers[i])
            # Logarithmic barrier with dynamic scaling
            log_barrier = self.barrier_heights[i] * np.log(1.0 + 
                                                         self.log_barrier_params[i] * dist)
            result += log_barrier
            
        # Chaotic sine-wave modulations
        for i in range(self.dim):
            # Chaotic modulation using sine waves with varying frequencies
            chaotic_mod = self.chaotic_ampls[i] * np.sin(self.chaotic_freqs[i] * x[i])
            # Add higher-order chaotic components
            chaotic_mod += 0.5 * np.sin(2 * self.chaotic_freqs[i] * x[i])
            chaotic_mod += 0.3 * np.sin(3 * self.chaotic_freqs[i] * x[i])
            result += chaotic_mod
            
        # Cross-dimensional exponential coupling
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                # Exponential coupling with distance-dependent strength
                coupling_dist = np.abs(x[i] - x[j])
                coupling_strength = np.exp(-0.5 * coupling_dist)
                result += coupling_strength * (x[i]**2 + x[j]**2)
                
        # Adaptive conditioning based on chaotic dynamics
        chaotic_sum = np.sum(np.sin(self.chaotic_freqs * x))
        condition_factor = 1.0 + 0.4 * np.sin(chaotic_sum)
        result *= condition_factor
        
        # Add noise with chaotic amplitude modulation
        noise_amplitude = 0.2 * (1.0 + 0.3 * np.sin(np.sum(x**2)))
        noise = noise_amplitude * np.random.uniform(-1, 1)
        result += noise
        
        # Higher-order polynomial terms for additional complexity
        for i in range(self.dim):
            result += 0.1 * (x[i]**4 - 2*x[i]**2 + 1)
            
        return result