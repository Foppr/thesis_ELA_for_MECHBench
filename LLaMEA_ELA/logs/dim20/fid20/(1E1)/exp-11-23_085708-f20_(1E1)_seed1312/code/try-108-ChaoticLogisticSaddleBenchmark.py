import numpy as np

class ChaoticLogisticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute logistic map parameters for chaotic behavior
        self.logistic_r = 3.95
        self.noise_scale = 0.1
        
    def f(self, x):
        x = np.array(x)
        
        # Scale to [-5, 5]
        x_scaled = x / 5.0
        
        # Chaotic logistic map component for each dimension
        chaotic_term = 0.0
        for i in range(self.dim):
            # Use previous dimensions to create chaotic coupling
            if i == 0:
                chaotic_value = x_scaled[i] * self.logistic_r * (1 - x_scaled[i])
            else:
                chaotic_value = x_scaled[i] * self.logistic_r * (1 - x_scaled[i-1])
            chaotic_term += chaotic_value**2
        
        # Fractional Brownian motion-like roughness with Hurst parameter
        fbm_roughness = 0.0
        hurst = 0.3
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                distance = abs(x_scaled[i] - x_scaled[j])
                fbm_roughness += (distance**(2*hurst)) * np.sin(10 * distance)
        
        # Saddle-point dominant structure with alternating peaks and valleys
        saddle_term = 0.0
        for i in range(self.dim):
            # Create alternating pattern of peaks and valleys
            saddle_term += (x_scaled[i]**4 - 2*x_scaled[i]**2) * np.cos(2 * x_scaled[i])
        
        # Cross-dimensional interaction with exponential decay
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction = np.exp(-abs(x_scaled[i] - x_scaled[j]) / (i + j + 1))
                cross_term += interaction * (np.sin(3 * x_scaled[i]) * np.cos(2 * x_scaled[j]) + 
                                           np.cos(5 * x_scaled[i]) * np.sin(4 * x_scaled[j]))
        
        # Add noise with varying amplitude
        noise = np.sum(np.random.normal(0, self.noise_scale, self.dim) * (x_scaled + 1))
        
        # Global minimum at origin with added complexity
        result = chaotic_term + fbm_roughness + saddle_term + cross_term + noise
        
        # Ensure global minimum is at zero with proper scaling
        return result + 5.0