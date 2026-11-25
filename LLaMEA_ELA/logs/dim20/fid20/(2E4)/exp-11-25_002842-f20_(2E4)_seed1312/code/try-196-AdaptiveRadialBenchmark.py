import numpy as np

class AdaptiveRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize cluster centers with adaptive spacing
        self.centers = np.random.uniform(-4.0, 4.0, (dim, 10))
        self.cluster_radii = np.random.uniform(0.5, 2.0, 10)
        self.frequency_modulation = np.random.uniform(1.0, 5.0, dim)
        self.amplitude_scaling = np.random.uniform(0.5, 2.5, dim)
        self.penalty_weights = np.random.uniform(0.1, 1.0, dim)
        self.gradient_thresholds = np.random.uniform(0.1, 0.5, dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial basis function components with adaptive centers
        result = 0.0
        for i in range(10):
            distance = np.sum((x_norm - self.centers[:, i])**2)
            rb_value = self.cluster_radii[i] * np.exp(-distance / (2.0 * self.cluster_radii[i]**2))
            result += rb_value
            
        # Frequency modulation with adaptive scaling
        freq_mod = 0.0
        for i in range(self.dim):
            freq_mod += self.frequency_modulation[i] * np.sin(self.amplitude_scaling[i] * x_norm[i])
            
        # Gradient-dependent penalty terms
        penalty = 0.0
        for i in range(self.dim):
            grad_mag = np.abs(np.cos(x_norm[i])) * self.penalty_weights[i]
            if grad_mag > self.gradient_thresholds[i]:
                penalty += grad_mag * (x_norm[i]**2)
                
        # Additional harmonic components with varying amplitudes
        harmonics = 0.0
        for i in range(self.dim):
            harmonics += (0.5 * np.sin(2 * x_norm[i]) + 
                         0.3 * np.cos(3 * x_norm[i]) + 
                         0.2 * np.sin(5 * x_norm[i]))
            
        # Combine all components with dynamic weighting
        total = result + 0.3 * freq_mod + 0.2 * harmonics - 0.1 * penalty
        
        return total