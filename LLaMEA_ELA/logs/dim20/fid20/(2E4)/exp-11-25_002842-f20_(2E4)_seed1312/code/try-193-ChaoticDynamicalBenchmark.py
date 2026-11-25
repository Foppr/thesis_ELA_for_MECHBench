import numpy as np

class ChaoticDynamicalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic system parameters with slight modifications
        self.chebyshev_coeffs = np.random.uniform(-1.5, 1.5, (dim, 5))
        self.delay_lengths = np.random.randint(1, 8, dim)
        self.feedback_gains = np.random.uniform(0.2, 2.5, dim)
        self.bifurcation_params = np.random.uniform(0.3, 3.5, dim)
        self.saddle_points = np.random.uniform(-2.5, 2.5, (dim, 3))
        self.noise_levels = np.random.uniform(0.02, 0.15, dim)
        self.transition_regions = np.random.uniform(0.2, 1.5, dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic dynamical system with time-delayed feedback
        result = 0.0
        for i in range(self.dim):
            # Base chaotic map with modified Chebyshev polynomials
            base_value = np.sum([
                self.chebyshev_coeffs[i, j] * np.cos(j * np.arccos(np.clip(x_norm[i], -1, 1))) 
                for j in range(5)
            ])
            
            # Time-delayed feedback component with increased complexity
            delay_sum = 0.0
            for k in range(self.delay_lengths[i]):
                idx = (i - k - 1) % self.dim
                delay_sum += self.feedback_gains[i] * np.sin(x_norm[idx] * (k + 1))
            
            # Saddle-node bifurcation terms with modified exponents
            bifurcation_term = self.bifurcation_params[i] * (x_norm[i]**3 - x_norm[i])**2
            
            # Non-smooth transition regions with additional exponential terms
            transition = 0.0
            for j in range(3):
                transition += np.exp(-self.transition_regions[i] * (x_norm[i] - self.saddle_points[i, j])**2) + \
                              0.5 * np.exp(-2 * self.transition_regions[i] * (x_norm[i] - self.saddle_points[i, j])**2)
            
            # Add noise and combine components
            noise = np.random.normal(0, self.noise_levels[i])
            chaotic_value = base_value + delay_sum + bifurcation_term + transition + noise
            
            result += chaotic_value * np.exp(-0.5 * x_norm[i]**2)
            
        # Enhanced cross-dimensional coupling with additional interaction terms
        coupling_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = 0.7 * (1.0 + np.tanh(x_norm[i] * x_norm[j])) * \
                                   np.cos(0.5 * (x_norm[i] - x_norm[j])**2)
                coupling_terms += coupling_strength * np.sin(x_norm[i] + x_norm[j])
                
        # Additional harmonic components with modified amplitudes and frequencies
        harmonic_sum = 0.0
        for i in range(self.dim):
            harmonic_sum += (np.sin(3 * x_norm[i]) + 
                           0.6 * np.cos(4 * x_norm[i]) + 
                           0.4 * np.sin(7 * x_norm[i]))
            
        # Combine all components with optimized weights
        total = 0.5 * result + 0.3 * coupling_terms + 0.2 * harmonic_sum
        
        return total