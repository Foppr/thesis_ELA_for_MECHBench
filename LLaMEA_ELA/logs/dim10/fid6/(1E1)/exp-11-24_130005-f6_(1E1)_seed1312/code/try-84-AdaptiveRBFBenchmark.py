import numpy as np

class AdaptiveRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute condition numbers for each dimension
        self.condition_numbers = 10**(np.linspace(0, 3, dim))
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Radial Basis Functions with varying condition numbers
        rbf_sum = 0.0
        for i in range(self.dim):
            # Adaptive conditioning based on dimension
            cond = self.condition_numbers[i]
            # Asymmetric RBF centers
            center = np.sin(i * 0.5) * 0.8
            rbf_sum += np.exp(-cond * (x_scaled[i] - center)**2)
        
        # Periodic oscillation component with varying frequencies
        periodic_term = 0.0
        for i in range(self.dim):
            freq = 2.0 + 0.5 * np.cos(i * 0.3)
            periodic_term += np.sin(freq * x_scaled[i]) * np.cos(1.5 * x_scaled[i])
        
        # Asymmetric saddle point structure
        saddle_term = 0.0
        for i in range(self.dim):
            # Create asymmetric regions using cubic terms
            saddle_term += (x_scaled[i]**3 - 0.5 * x_scaled[i]**2) * np.sin(i)
        
        # Cross-dimensional interaction with adaptive weights
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Adaptive coupling based on dimension indices
                coupling = 0.5 + 0.3 * np.sin(i * 0.2) * np.cos(j * 0.3)
                cross_term += coupling * (x_scaled[i]**2 + x_scaled[j]**2) * \
                             np.sin(2.0 * x_scaled[i] + 1.5 * x_scaled[j])
        
        # Combined landscape with dynamic weighting
        return 1.2 * rbf_sum + 0.9 * periodic_term + 0.7 * saddle_term + 0.8 * cross_term + 3.1