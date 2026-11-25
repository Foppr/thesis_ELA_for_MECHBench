import numpy as np

class ChaoticDynamicalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic system parameters
        self.chebyshev_coeffs = np.random.uniform(-1.0, 1.0, (dim, 5))
        self.delay_lengths = np.random.randint(1, 6, dim)
        self.feedback_gains = np.random.uniform(0.1, 2.0, dim)
        self.bifurcation_params = np.random.uniform(0.5, 3.0, dim)
        self.saddle_points = np.random.uniform(-2.0, 2.0, (dim, 3))
        self.noise_levels = np.random.uniform(0.01, 0.1, dim)
        self.transition_regions = np.random.uniform(0.1, 1.0, dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic dynamical system with time-delayed feedback
        result = 0.0
        for i in range(self.dim):
            # Base chaotic map with Chebyshev polynomials
            base_value = np.sum([
                self.chebyshev_coeffs[i, j] * np.cos(j * np.arccos(np.clip(x_norm[i], -1, 1))) 
                for j in range(5)
            ])
            
            # Time-delayed feedback component
            delay_sum = 0.0
            for k in range(self.delay_lengths[i]):
                idx = (i - k - 1) % self.dim
                delay_sum += self.feedback_gains[i] * np.sin(x_norm[idx])
            
            # Saddle-node bifurcation terms
            bifurcation_term = self.bifurcation_params[i] * (x_norm[i]**2 - 1.0)**2
            
            # Non-smooth transition regions
            transition = 0.0
            for j in range(3):
                transition += np.exp(-self.transition_regions[i] * (x_norm[i] - self.saddle_points[i, j])**2)
            
            # Add noise and combine components
            noise = np.random.normal(0, self.noise_levels[i])
            chaotic_value = base_value + delay_sum + bifurcation_term + transition + noise
            
            result += chaotic_value * np.exp(-0.5 * x_norm[i]**2)
            
        # Cross-dimensional coupling with emergent patterns
        coupling_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = 0.5 * (1.0 + np.tanh(x_norm[i] * x_norm[j]))
                coupling_terms += coupling_strength * np.sin(x_norm[i] + x_norm[j])
                
        # Additional harmonic components with varying amplitudes
        harmonic_sum = 0.0
        for i in range(self.dim):
            harmonic_sum += (np.sin(2 * x_norm[i]) + 
                           0.5 * np.cos(3 * x_norm[i]) + 
                           0.3 * np.sin(5 * x_norm[i]))
            
        # Combine all components with optimized weights
        total = 0.6 * result + 0.2 * coupling_terms + 0.2 * harmonic_sum
        
        return total