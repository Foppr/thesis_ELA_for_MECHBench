import numpy as np

class ChaoticDynamicalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic system parameters with significant modifications
        self.chebyshev_coeffs = np.random.uniform(-2.0, 2.0, (dim, 7))
        self.delay_lengths = np.random.randint(2, 12, dim)
        self.feedback_gains = np.random.uniform(0.1, 3.0, dim)
        self.bifurcation_params = np.random.uniform(0.2, 4.0, dim)
        self.saddle_points = np.random.uniform(-3.0, 3.0, (dim, 5))
        self.noise_levels = np.random.uniform(0.01, 0.2, dim)
        self.transition_regions = np.random.uniform(0.1, 2.0, dim)
        # Additional chaotic parameters for increased complexity
        self.fractal_dimensions = np.random.uniform(1.1, 2.5, dim)
        self.coupling_strengths = np.random.uniform(0.5, 1.5, (dim, dim))
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic dynamical system with time-delayed feedback and fractal components
        result = 0.0
        for i in range(self.dim):
            # Base chaotic map with modified Chebyshev polynomials (higher degree)
            base_value = np.sum([
                self.chebyshev_coeffs[i, j] * np.cos(j * np.arccos(np.clip(x_norm[i], -1, 1))) 
                for j in range(7)
            ])
            
            # Time-delayed feedback component with increased complexity and fractal scaling
            delay_sum = 0.0
            for k in range(self.delay_lengths[i]):
                idx = (i - k - 1) % self.dim
                delay_sum += self.feedback_gains[i] * np.sin(x_norm[idx] * (k + 1)) * \
                            np.exp(-0.5 * (x_norm[idx] - x_norm[i])**2)
            
            # Saddle-node bifurcation terms with modified exponents and fractal scaling
            bifurcation_term = self.bifurcation_params[i] * (x_norm[i]**3 - x_norm[i])**2 * \
                              np.sin(self.fractal_dimensions[i] * x_norm[i])
            
            # Non-smooth transition regions with additional exponential terms and more saddle points
            transition = 0.0
            for j in range(5):
                transition += np.exp(-self.transition_regions[i] * (x_norm[i] - self.saddle_points[i, j])**2) + \
                              0.3 * np.exp(-2 * self.transition_regions[i] * (x_norm[i] - self.saddle_points[i, j])**2) + \
                              0.1 * np.exp(-3 * self.transition_regions[i] * (x_norm[i] - self.saddle_points[i, j])**2)
            
            # Add noise and combine components
            noise = np.random.normal(0, self.noise_levels[i])
            chaotic_value = base_value + delay_sum + bifurcation_term + transition + noise
            
            result += chaotic_value * np.exp(-0.5 * x_norm[i]**2) * \
                     (1.0 + 0.3 * np.sin(self.fractal_dimensions[i] * x_norm[i]))
            
        # Enhanced cross-dimensional coupling with fractal and non-linear interaction terms
        coupling_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = self.coupling_strengths[i, j] * \
                                   (1.0 + np.tanh(x_norm[i] * x_norm[j])) * \
                                   np.cos(0.3 * (x_norm[i] - x_norm[j])**2) * \
                                   np.exp(-0.1 * (x_norm[i] - x_norm[j])**2)
                coupling_terms += coupling_strength * np.sin(x_norm[i] + x_norm[j]) * \
                                 np.cos(0.5 * (x_norm[i] - x_norm[j]))
                
        # Additional harmonic components with modified amplitudes, frequencies and fractal scaling
        harmonic_sum = 0.0
        for i in range(self.dim):
            harmonic_sum += (np.sin(4 * x_norm[i]) + 
                           0.7 * np.cos(5 * x_norm[i]) + 
                           0.5 * np.sin(8 * x_norm[i]) + 
                           0.2 * np.cos(10 * x_norm[i]) *
                           np.exp(-0.2 * x_norm[i]**2))
            
        # Combine all components with optimized weights and fractal scaling
        total = 0.4 * result + 0.35 * coupling_terms + 0.25 * harmonic_sum
        
        return total