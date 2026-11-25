import numpy as np

class ChaoticLogisticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters
        self.r = 3.9  # Logistic map parameter
        self.beta = 0.5  # Fractional Brownian motion scaling
        
    def f(self, x):
        x = np.array(x)
        
        # Scale to [-5, 5]
        x_scaled = x / 5.0
        
        # Chaotic logistic map component for each dimension
        chaotic_term = 0.0
        for i in range(self.dim):
            # Use previous dimensions to create chaotic interaction
            if i == 0:
                chaotic_value = self.r * x_scaled[i] * (1 - x_scaled[i])
            else:
                chaotic_value = self.r * x_scaled[i] * (1 - x_scaled[i]) + 0.1 * x_scaled[i-1]
            chaotic_term += chaotic_value ** 2
        
        # Fractional Brownian motion-like component using Hurst exponent concept
        fbm_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                distance = np.abs(x_scaled[i] - x_scaled[j])
                fbm_term += (distance ** (2 * self.beta)) * np.sin(5 * distance)
        
        # Dynamic phase-shifted sinusoidal terms with varying frequencies
        phase_shifted_term = 0.0
        for i in range(self.dim):
            # Apply dynamic phase shift based on other coordinates
            phase = np.sum(x_scaled[:i]) if i > 0 else 0.0
            phase_shifted_term += (np.sin(2 * x_scaled[i] + phase) + 
                                 0.5 * np.cos(3 * x_scaled[i] + phase) +
                                 0.3 * np.sin(4 * x_scaled[i] + phase))
        
        # Non-separable interaction terms with dynamic weights
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction_term += (np.sin(x_scaled[i] * x_scaled[j]) * 
                                   np.cos(0.5 * (x_scaled[i] + x_scaled[j])) *
                                   (i + j + 1) * (1 + 0.2 * np.sin(x_scaled[i] * x_scaled[j])))
        
        # Add a dynamic global minimum modulation
        coord_sum = np.sum(x_scaled)
        global_mod = 1.0 + 0.3 * np.sin(2 * coord_sum) * np.cos(1.5 * coord_sum)
        
        # Combine all terms with different weights and add constant offset
        return (chaotic_term * 2.0 + 
                fbm_term * 0.5 + 
                phase_shifted_term * 1.5 + 
                interaction_term * 0.8 + 
                global_mod * 0.3 + 
                3.0)